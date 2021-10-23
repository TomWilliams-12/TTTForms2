from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('user_name', 'first_name', 'last_name', 'email', 'reg', 'signature')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False

        self.helper.add_input(Submit('submit', 'Submit'))


class EditProfile(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'reg', 'signature')