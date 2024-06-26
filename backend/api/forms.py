from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User ,trackedProducts

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']



class TrackingForm(ModelForm):
    class Meta:
        model=trackedProducts
        fields=['url']
