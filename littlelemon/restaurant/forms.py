from django.forms import ModelForm
from .models import booking

class BookingForm(ModelForm):
    class Meta:
        model = booking
        fields = "__all__"