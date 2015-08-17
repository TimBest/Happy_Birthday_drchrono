from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

class ProfileView(TemplateView):
    template_name='accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

profile = login_required(ProfileView.as_view())
