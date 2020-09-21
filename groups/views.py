from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView,DetailView,RedirectView
from django.contrib.auth import mixins 
from .models import Group,GroupMember
from django.contrib import messages
from django.shortcuts import reverse
# Create your views here.

class Creategroup(mixins.LoginRequiredMixin,CreateView):
    # template_name = 'groups\group_form.html'
    fields = ('name','description')
    model = Group
 
class SingleGroup(DetailView):
    model = Group

class ListGroup(ListView):
    model = Group


class JoinGroup(mixins.LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(mixins.LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)