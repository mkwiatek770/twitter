from django.contrib import admin
from .models import Tweet, TweetLike, TweetShare, ProfileUser
# Register your models here.


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass


@admin.register(TweetLike)
class TweetLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(TweetShare)
class TweetShareAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    pass
