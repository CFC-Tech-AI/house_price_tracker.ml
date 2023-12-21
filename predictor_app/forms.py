from django import forms
from .models import House
import pandas as pd

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['bedrooms', 'location', 'square_footage']

    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)

        # Load your dataset to get unique location options
        dataset = pd.read_csv('predictor_app/price_data.csv')
        unique_locations = dataset['location'].unique()

        # Set choices for the 'location' field
        self.fields['location'].widget = forms.Select(choices=[(location, location) for location in unique_locations])
