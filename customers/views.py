from django.shortcuts import redirect, render
from django.views import View
from customers.forms import CustomerForm
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .models import Customers

class CreateCustomer(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'create_customer.html', {'form': form})
    def post(self, request):
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/')


class ViewCustomers(ListView):
    model = Customers
    fields = '__all__'
    template_name = 'view_customers.html'
    paginate_by = 25


class EditCustomer(UpdateView):
    model = Customers
    fields = '__all__'
    template_name = 'create_customer.html'
    success_url = "/"