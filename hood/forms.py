from django.forms import ModelForm
from .models import Neighborhood


class CreateNeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'
