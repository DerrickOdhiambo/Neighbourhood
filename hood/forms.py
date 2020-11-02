from django.forms import ModelForm
from .models import Neighborhood, Business


class CreateNeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class CreateBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'neighborhood', 'business_email']
