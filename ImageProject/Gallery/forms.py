from django import forms
from .models import ImageData
class ImageRegister(forms.ModelForm):
    class Meta:
        model = ImageData
        fields = '__all__'
        labels = {'Img':''}