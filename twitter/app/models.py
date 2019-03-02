from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class ProfileUser(AbstractUser):
    tweets = models.IntegerField(default=0)
    followers = models.ManyToManyField("self")

    def __str__(self):
        return self.username


class Tweet(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.last_modification = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} - {} ...".format(self.author, self.content[:20])


class TweetLike(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} ..".format(self.user.username, self.tweet.content[:20])


class TweetShare(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} ..".format(self.user.username, self.tweet.content[:20])
