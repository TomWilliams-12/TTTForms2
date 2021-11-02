from django.forms import Form
from django.forms.fields import CharField

class InductionForm(Form):
    name = CharField(label='Your name', max_length=100)


class ReviewForm(Form):
    test = CharField(label='test', max_length=100)