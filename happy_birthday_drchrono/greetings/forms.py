from django import forms

from greetings.models import HappyBirthday


class HappyBirthdayForm(forms.ModelForm):

    class Meta:
        model = HappyBirthday
        widgets = {
          'email_body' : forms.Textarea(attrs={'rows': 2, 'cols': 19}),
        }
        fields = ('notification_type', 'sms', 'email_subject','email_body', 'is_active',)
