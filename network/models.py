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
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    userID = models.IntegerField()
    phoneNumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    profilePicture = models.ImageField(upload_to='profileImages')
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    profession = models.CharField(max_length=100)
    country = CountryField(blank_label="(select country)")
    location = models.CharField(max_length=200)
    about = models.TextField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkEdin = models.URLField(max_length=200)
    gitHub = models.URLField(max_length=200)

    def __str__(self):
        return self.username


