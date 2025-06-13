from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services.twitter import post_tweet_api

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def post_tweet(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        token = request.user.profile.twitter_token
        post_tweet_api(token, message)
    return redirect('dashboard')
