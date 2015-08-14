from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')
