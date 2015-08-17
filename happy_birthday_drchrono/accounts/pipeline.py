import string, random
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from accounts.models import Profile


def create_profile(request, strategy, backend, uid, response={}, details={}, user=None, social=None, *args, **kwargs):
    """
        if user has profile skip else create new profile
    """
    if not hasattr(user, 'profile'):
        user.profile = Profile(user=user)
        user.profile.save()
    return None

USERNAME_LENGTH = User._meta.get_field('username').max_length

def get_username(username):
    username = username.replace (" ", "_")
    username = slugify(username)[:USERNAME_LENGTH]
    try:
        User.objects.get(username=username)
        if len(username) >= USERNAME_LENGTH:
            return get_username(random.choice(string.letters+string.digits))
        else:
            return get_username(username+random.choice(string.letters+string.digits))
    except User.DoesNotExist:
        return username;
