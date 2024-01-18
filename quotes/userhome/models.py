from django.db import models

# Create your models here.
# userhome/models.py

from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s UserInfo"
    
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     # Add this field if you want to store the username in the Video model
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    video_id = models.AutoField(primary_key=True, unique=True)
    video_file = models.FileField(upload_to='videos/',default='path/to/default_video.mp4')
    
    def __str__(self):
       return self.title

class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.posted_date}"
    
class ImagePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imgfile = models.ImageField(upload_to='images/')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.posted_date}"