from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        print('Hello, I am working...')
