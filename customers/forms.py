from django.forms import ModelForm
from customers.models import Customers

class CustomerForm(ModelForm):

    class Meta:
        model = Customers
        fields = '__all__'
        exclude = ()
        widgets = {}


