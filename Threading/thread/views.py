from django.shortcuts import render
# mysignalapp/views.py
from django.http import HttpResponse
from django.contrib.auth.models import User
import threading

def create_user_view(request):
    print(f"Main thread: {threading.current_thread().name}")
    user = User(username="testuser")
    user.save()  # This will trigger the post_save signal
    return HttpResponse("User created, check console for thread details.")
