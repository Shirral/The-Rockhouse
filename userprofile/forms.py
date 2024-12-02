from allauth.account.forms import SignupForm, LoginForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'remember':
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            else:
                self.fields[field].widget.attrs['class'] = 'custom-checkbox'
