from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from PIL import Image
import uuid
from datetime import datetime

# Create your models here.

class Profile(models.Model):

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.IntegerField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=100,  null=True, blank=True)
    profilePicture = models.ImageField(upload_to='profileImages',  null=True, blank=True)
    coverPhoto = models.ImageField(upload_to='profileImages',  null=True, blank=True)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False,  null=True, blank=True)
    age = models.IntegerField( null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER_CHOICES)
    profession = models.CharField(max_length=100,  null=True, blank=True)
    country = CountryField(blank_label="Select Country")
    location = models.CharField(max_length=200,  null=True, blank=True)
    homeAddress = models.CharField(max_length=200,  null=True, blank=True)
    about = models.TextField(max_length=200,  null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200,  null=True, blank=True)
    instagram = models.URLField(max_length=200,  null=True, blank=True)
    linkEdin = models.URLField(max_length=200,  null=True, blank=True)
    gitHub = models.URLField(max_length=200,  null=True, blank=True)
    website = models.URLField(max_length=200,  null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'



class Post(models.Model):
    postID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    postUser = models.CharField(max_length=50)
    postImage = models.ImageField(upload_to='post Images')
    postCaption = models.TextField()
    postCreatedAt = models.DateTimeField(default=datetime.now)
    postNumberOfLikes = models.IntegerField(default=0)

    def __str__(self):
        return self.postUser
    

class LikePost(models.Model):
    postID = models.CharField(max_length=500)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class FollwersCount(models.Model):
    user = models.CharField(max_length=150)
    follower = models.CharField(max_length=160)

    def __str__(self):
        return self.user

class Issue(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Group(models.Model):
    groupAdmin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:70]
 





    


