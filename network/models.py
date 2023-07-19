from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100,  null=True, blank=True)
    lastName = models.CharField(max_length=100,  null=True, blank=True)
    userName = models.CharField(max_length=100,  null=True, blank=True)
    userID = models.IntegerField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=100,  null=True, blank=True)
    email = models.EmailField(max_length=254,  null=True, blank=True)
    profilePicture = models.ImageField(upload_to='profileImages',  null=True, blank=True)
    coverPhoto = models.ImageField(upload_to='profileImages',  null=True, blank=True)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False,  null=True, blank=True)
    age = models.IntegerField( null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER_CHOICES)
    profession = models.CharField(max_length=100,  null=True, blank=True)
    country = CountryField(blank_label="(select country)")
    location = models.CharField(max_length=200,  null=True, blank=True)
    about = models.TextField(max_length=200,  null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200,  null=True, blank=True)
    instagram = models.URLField(max_length=200,  null=True, blank=True)
    linkEdin = models.URLField(max_length=200,  null=True, blank=True)
    gitHub = models.URLField(max_length=200,  null=True, blank=True)
    website = models.URLField(max_length=200,  null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


