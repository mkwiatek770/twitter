from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,

)
from .models import Tweet, ProfileUser
from .forms import TweetCreateForm


class HomeView(ListView):
    model = Tweet
    context_object_name = 'tweets'
    template_name = 'app/home.html'


class TweetCreateView(View):
    def get(self, request):
        form = TweetCreateForm()
        return render(request, "app/create_tweet.html", {
            'form': form
        })

    def post(self, request):
        form = TweetCreateForm(request.POST)

        if form.is_valid():
            author = request.user
            content = form.cleaned_data['content']

            Tweet.objects.create(
                author=author,
                content=content
            )

            return redirect(reverse("home"))


class UserDetailView(View):
    def get(self, request, username):
        user = ProfileUser.objects.get(username=username)
