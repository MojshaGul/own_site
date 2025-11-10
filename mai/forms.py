from django.forms import Form,ModelForm
from .models import Product
class createproduct(ModelForm):
    class Meta:
        model=Product
        fields=["name","price","description","count","categori"]