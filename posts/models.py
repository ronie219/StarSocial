from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
from groups.models import Group
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    create_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = self.message_html
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("posts:single",kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-create_at']
        unique_together = ['user','message']