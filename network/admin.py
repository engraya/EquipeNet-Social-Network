from django.contrib import admin
from .models import Profile, Post, LikePost, FollwersCount, Issue, Group, Message


# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollwersCount)
admin.site.register(Issue)
admin.site.register(Group)
admin.site.register(Message)

