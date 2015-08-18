from django.contrib.auth.models import User

from greetings.models import HappyBirthday


def create_greetings(request, strategy, backend, uid, response={}, details={}, user=None, social=None, *args, **kwargs):
    """
        if user has greetings skip else create new greetings
    """
    if not hasattr(user, 'happy_birthday'):
        user.happy_birthday = HappyBirthday(user=user)
        user.happy_birthday.save()
    return None

USERNAME_LENGTH = User._meta.get_field('username').max_length
