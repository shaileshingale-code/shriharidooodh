from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import requests
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.db import transaction
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from django import template
from datetime import date
from django.utils import timezone

# from .models import Users
from .models import Products
from .models import Delievery_Management
from .models import Package
from .models import Customer_list
from .models import orders
from .models import daily_orders
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from .forms import AddProductForm
from .forms import PackageForm
from .forms import CustomeraddForm
from .forms import OrderForm
from .forms import OrderFormtwo
from .forms import UserEditForm
from .forms import ChangeDetailsForm
from .forms import Delievery_ManagementForm











# class UserRegistrationView(CreateView):
#     model = Customer_list
#     form_class = UserRegistrationForm
#     template_name = 'shrihariapp/registration.html'
#     success_url = reverse_lazy('admin_login')

#     def form_valid(self, form):
        
#         response = super().form_valid(form)
       
#         messages.success(self.request, 'Registration successful!')

#         return response

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         if self.request.method == 'POST' and self.object:
#             context['registration_successful'] = True
#         return context



# class UserRegistrationView(CreateView):
#     model = Customer_list
#     form_class = UserRegistrationForm
#     template_name = 'shrihariapp/registration.html'
#     # success_url = reverse_lazy('admin_login')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, 'Registration successful!')

       
#         whatsapp_api_url = 'http://wa.dreamztechnolgy.org/api/v1/sendMessage'
#         whatsapp_api_params = {
#             'key': 'd7abcb9dd2a34f2b9e1cd40145144ae1',
#             'to': '919284546933',  
#             'message': 'Hello, welcome!',  
#             'IsUrgent': 'False',
#             'isDeleteAfterSend': 'False',
#             'isGroupMsg': 'False',
#             'ExpiryTime': '00:00:00',
#             'IsFailMessage': 'False',
#             'SenderId': 'AB-111213',
#             'ContentTemplate': 'Hello, This is text message.',
#             'SendingMessageType': '1'
#         }
#         whatsapp_response = requests.get(whatsapp_api_url, params=whatsapp_api_params)

#         print("WhatsApp API Response:", whatsapp_response.text)

#         self.request.session['whatsapp_response'] = whatsapp_response.text

#         return response

#         subject = 'Welcome to Shri hari doodh !'
#         message = 'Thank you for registering to Shri Hari doodh. We hope you enjoy using our platform.'
#         from_email = 'shailesh.i@dreamztechnology.com'  # Change to your email
#         to_email = form.cleaned_data['username']  # Assuming your form has an email field
#         send_mail(subject, message, from_email, [to_email])

#         return response

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.method == 'POST' and self.object:
#             context['registration_successful'] = True
#         return context



class UserRegistrationView(CreateView):
    model = Customer_list
    form_class = UserRegistrationForm
    template_name = 'shrihariapp/registration.html'
    success_url = reverse_lazy('admin_login')

    def form_valid(self, form):
        whatsapp_api_url = 'http://wa.dreamztechnolgy.org/api/v1/sendMessage'
        whatsapp_api_params = {
            'key': 'd7abcb9dd2a34f2b9e1cd40145144ae1',
            'to': '919284546933',  
            'message': 'Hello, welcome!',  
            'IsUrgent': 'False',
            'isDeleteAfterSend': 'False',
            'isGroupMsg': 'False',
            'ExpiryTime': '00:00:00',
            'IsFailMessage': 'False',
            'SenderId': 'AB-111213',
            'ContentTemplate': 'Hello, This is text message.',
            'SendingMessageType': '1'
        }

        try:
            whatsapp_response = requests.get(whatsapp_api_url, params=whatsapp_api_params)
            print("WhatsApp API Response:", whatsapp_response.text)
            self.request.session['whatsapp_response'] = whatsapp_response.text
            messages.success(self.request, whatsapp_response.text)
        except requests.RequestException as e:
            print("Error sending WhatsApp message:", e)
            self.request.session['whatsapp_response'] = "Error: Failed to send WhatsApp message."
            messages.error(self.request, "Error: Failed to send WhatsApp message.")

        response = super().form_valid(form)

        subject = 'Welcome to Shri hari doodh !'
        message = 'Thank you for registering to Shri Hari doodh. We hope you enjoy using our platform.'
        from_email = 'shailesh.i@dreamztechnology.com'  # Change to your email
        to_email = form.cleaned_data['username']  # Assuming your form has an email field
        send_mail(subject, message, from_email, [to_email])

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST' and self.object:
            context['registration_successful'] = True
        return context
        

class UserLoginView(LoginView):
   
    form_class = UserLoginForm
    template_name = 'shrihariapp/login.html'  
    # authentication_form = CustomeraddForm    

@never_cache
@login_required    
def Dashboard(request):
    
    return render(request, 'shrihariapp/Dashboard.html')



def custom_logout(request):
   
    logout(request)

    
    return redirect('admin_login')  
    


@method_decorator([login_required, never_cache], name='dispatch')
class ProductAddFormView(CreateView):
    model = Products
    form_class = AddProductForm
    template_name = 'shrihariapp/addproduct.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page'))      


@never_cache
@login_required 
def ProductListView(request):
    products = Products.objects.all()
    return render(request, 'shrihariapp/product_list.html', {'products': products})      



def Product_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('product_list')  


# @never_cache
# @login_required 
# def Product_edit(request, pk):
#     product = get_object_or_404(Products, pk=pk)
#     if request.method == "POST":
#         form = AddProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             new_product = form.save(commit=False)
#             if 'product_image' in request.FILES:
#                 new_product.product_image.save(request.FILES['product_image'].name, request.FILES['product_image'], save=False)
#                 new_product.save()
#             return redirect('product_list')
           
#     else:
#         form = AddProductForm(instance=product)
#     return render(request, 'shrihariapp/addproduct.html', {'form': form})


@never_cache
@login_required 
def Product_edit(request, pk):
    product = get_object_or_404(Products, pk=pk)
    
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            new_product = form.save(commit=False)
            
            # Save the product image if it's changed
            if 'product_image' in request.FILES:
                new_product.product_image.save(request.FILES['product_image'].name, request.FILES['product_image'], save=False)
            
            # If the image is not changed, just save the form without image processing
            else:
                new_product.save()

            return redirect('product_list')
    else:
        form = AddProductForm(instance=product)
    
    return render(request, 'shrihariapp/addproduct.html', {'form': form})






@method_decorator([login_required, never_cache], name='dispatch')
class create_package(CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'shrihariapp/package_form.html'
    success_url = reverse_lazy('package_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context



@never_cache
@login_required 
def PackageListView(request):
    packages = Package.objects.all()
    return render(request, 'shrihariapp/package_list.html', {'packages': packages})  


def Packagedelete(request, pk):
    package = get_object_or_404(Package, pk=pk)
    package.delete()
    return redirect('package_list')


# @never_cache
# @login_required 
# def Packageedit(request, pk):
#     package = get_object_or_404(Package, pk=pk)
#     if request.method == "POST":
#         form = PackageForm(request.POST, instance=package)
#         if form.is_valid():
#             package = form.save(commit=False)
#             package.save()
#             return redirect('package_list')
           
#     else:
#         form = PackageForm(instance=package)
#     return render(request, 'shrihariapp/package_form.html', {'form': form})


# @never_cache
# @login_required 
# def complaint_edit(request, pk):
#     complaint = get_object_or_404(Complaints, pk=pk)
#     if request.method == "POST":
#         form = ComplaintApplyForm(request.POST, request.FILES, instance=complaint)
#         if form.is_valid():
#             new_complaint = form.save(commit=False)
           
#             if 'complaint_image' in request.FILES:
#                 new_complaint.complaint_image.save(request.FILES['complaint_image'].name, request.FILES['complaint_image'], save=False)
#             new_complaint.save()
#             return redirect('complaint_list')
#     else:
#         form = ComplaintApplyForm(instance=complaint)
#     return render(request, 'employeeapp/raisecomplaint.html', {'form': form})


# @never_cache
# @login_required 
# def Packageedit(request, pk):
#     package = get_object_or_404(Package, pk=pk)
#     if request.method == "POST":
#         form = PackageForm(request.POST, request.FILES, instance=package)
#         if form.is_valid():
#             new_package = form.save(commit=False)
#             if 'package_image' in request.FILES:
#                 new_package.package_image.save(request.FILES['package_image'].name, request.FILES['package_image'], save=False)
#             new_package.save()
#             return redirect('package_list')
#     else:
       
#         form = PackageForm(instance=package, initial={'products': package.products.all()})
    
#     products = Products.objects.all()
    
#     return render(request, 'shrihariapp/package_form.html', {'form': form, 'products': products})


@never_cache
@login_required 
def Packageedit(request, pk):
    package = get_object_or_404(Package, pk=pk)
    
    if request.method == "POST":
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            new_package = form.save(commit=False)
            
            # Save the package image if it's changed
            if 'package_image' in request.FILES:
                new_package.package_image.save(request.FILES['package_image'].name, request.FILES['package_image'], save=False)
            
            # If the image is not changed, just save the form without image processing
            else:
                new_package.save()

            return redirect('package_list')
    else:
        form = PackageForm(instance=package, initial={'products': package.products.all()})
    
    products = Products.objects.all()
    
    return render(request, 'shrihariapp/package_form.html', {'form': form, 'products': products})


@method_decorator([login_required, never_cache], name='dispatch')
class AddCustomerView(CreateView):
    model = Customer_list
    form_class = CustomeraddForm
    template_name = 'shrihariapp/addcustomer.html'
    success_url = reverse_lazy('customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['packages'] = Package.objects.all()
        return context 


@never_cache
@login_required 
def CustomerListView(request):
    customers = Customer_list.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/customer_list.html', {'customers': customers,'today': today})   




def Customerdelete(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    customer.delete()
    return redirect('customer_list')


@never_cache
@login_required 
def Customeredit(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=customer)
        if form.is_valid():
            new_customer = form.save(commit=False)
            
            # Check if the username has changed
            if new_customer.username != customer.username:
                if User.objects.filter(username=new_customer.username).exists():
                    form.add_error('username', "A customer with this username already exists.")
                    return render(request, 'shrihariapp/editcustomer.html', {'form': form})
            
            new_customer.save()
            return redirect('customer_list')
    else:
        form = UserEditForm(instance=customer)
    
    packages = Package.objects.all()
    
    return render(request, 'shrihariapp/editcustomer.html', {'form': form, 'packages': packages})



@never_cache
@login_required 
def ChangeDetails(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    
    if request.method == "POST":
        form = ChangeDetailsForm(request.POST, instance=customer)
        if form.is_valid():
            new_customer = form.save(commit=False)
            
            # Check if the username has changed
            if new_customer.username != customer.username:
                if User.objects.filter(username=new_customer.username).exists():
                    form.add_error('username', "A customer with this username already exists.")
                    return render(request, 'shrihariapp/changedetails.html', {'form': form})
            
            new_customer.save()
            return redirect('customer_list')
    else:
        form = ChangeDetailsForm(instance=customer)
    
    packages = Package.objects.all()
    
    return render(request, 'shrihariapp/changedetails.html', {'form': form, 'packages': packages})




def order_create(request, product_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.instance.product_id_id = product_id
            form.save()
            return redirect('order_list')  # Redirect to a success page
    else:
        form = OrderForm(product_id=product_id)
    return render(request, 'shrihariapp/order_create.html', {'form': form,'product_id': product_id})



@never_cache
@login_required 
def OrderListView(request):
    orderss = orders.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/order_list.html', {'orderss': orderss,'today': today}) 



def order_createtwo(request, package_id):
    if request.method == 'POST':
        form = OrderFormtwo(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            # form.instance.package_id = package_id
            form.save()
            return redirect('daily_list')  # Redirect to a success page
    else:
        form = OrderFormtwo(package_id=package_id)
    return render(request, 'shrihariapp/order_createtwo.html', {'form': form,'package_id': package_id})



@never_cache
@login_required 
def DailyOrderListView(request):
    ordersss = daily_orders.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/dailyorder_list.html', {'ordersss': ordersss,'today': today})     




def Orderdelete(request, pk):
    orderd = get_object_or_404(daily_orders, pk=pk)
    orderd.delete()
    return redirect('daily_list')


@never_cache
@login_required 
def Orderedit(request, pk):
    customer = get_object_or_404(daily_orders, pk=pk)
    if request.method == "POST":
        form = OrderFormtwo(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('daily_list')
           
    else:
        form = OrderFormtwo(instance=customer)
    
    
    packages = Package.objects.all()
    
    return render(request, 'shrihariapp/order_createtwo.html', {'form': form, 'packages': packages})             

def add_days(value, days):
    return value + timedelta(days=days)

# Register the custom filter function
register = template.Library()
register.filter('add_days', add_days)    


@method_decorator([login_required, never_cache], name='dispatch')
class AddBoyView(CreateView):
    model = Customer_list
    form_class = CustomeraddForm
    template_name = 'shrihariapp/addboy.html'
    success_url = reverse_lazy('Boy_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['packages'] = Package.objects.all()
        return context 


@never_cache
@login_required 
def BoyListView(request):
    customers = Customer_list.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/boy_list.html', {'customers': customers,'today': today}) 



def Boydelete(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    customer.delete()
    return redirect('Boy_list')



@never_cache
@login_required 
def Boyedit(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=customer)
        if form.is_valid():
            new_customer = form.save(commit=False)
            
            # Check if the username has changed
            if new_customer.username != customer.username:
                if User.objects.filter(username=new_customer.username).exists():
                    form.add_error('username', "A customer with this username already exists.")
                    return render(request, 'shrihariapp/editboy.html', {'form': form})
            
            new_customer.save()
            return redirect('Boy_list')
    else:
        form = UserEditForm(instance=customer)
    
    packages = Package.objects.all()
    
    return render(request, 'shrihariapp/editboy.html', {'form': form, 'packages': packages})




@never_cache
@login_required 
def ChangeDetailss(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    
    if request.method == "POST":
        form = ChangeDetailsForm(request.POST, instance=customer)
        if form.is_valid():
            new_customer = form.save(commit=False)
            
            # Check if the username has changed
            if new_customer.username != customer.username:
                if User.objects.filter(username=new_customer.username).exists():
                    form.add_error('username', "A customer with this username already exists.")
                    return render(request, 'shrihariapp/changedetailss.html', {'form': form})
            
            new_customer.save()
            return redirect('Boy_list')
    else:
        form = ChangeDetailsForm(instance=customer)
    
    packages = Package.objects.all()
    
    return render(request, 'shrihariapp/changedetailss.html', {'form': form, 'packages': packages})    



@method_decorator([login_required, never_cache], name='dispatch')
class DelieverySetupTwo(CreateView):
    model = Delievery_Management
    form_class = Delievery_ManagementForm
    template_name = 'shrihariapp/delievrysetuptwo.html'
    success_url = reverse_lazy('Delievery_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderss'] = orders.objects.all()
        context['dailyorderss'] = daily_orders.objects.all()
        context['customers'] = Customer_list.objects.all()
        return context        


# class DelieverySetup(FormView):
#     template_name = 'shrihariapp/delievrysetup.html'
#     form_class = Delievery_ManagementForm
#     success_url = reverse_lazy('Delievery_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['orderss'] = orders.objects.all()
#         context['dailyorderss'] = daily_orders.objects.all()
#         context['customers'] = Customer_list.objects.all()
#         return context

#     def form_valid(self, form):
#         delivery_management = form.save(commit=False)
#         orderidofdo = delivery_management.daily_order_id
        
#         selected_package = daily_orders.objects.get(pk=orderidofdo.pk)  
#         package_id = selected_package.package_id

#         packagedays = Package.objects.get(pk=package_id.pk) 
#         gap_days = packagedays.gap_days
#         package_days = packagedays.package_days
        
#         multiplication_result = package_days *1
 
#         with transaction.atomic():
#             for i in range(multiplication_result):
#                 delivery_management.pk = None  
#                 delivery_management.save()

#         return redirect(self.success_url)
        

class DelieverySetup(FormView):
    template_name = 'shrihariapp/delievrysetup.html'
    form_class = Delievery_ManagementForm
    success_url = reverse_lazy('Delievery_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderss'] = orders.objects.all()
        context['dailyorderss'] = daily_orders.objects.all()
        context['customers'] = Customer_list.objects.all()
        return context

    def form_valid(self, form):
        delivery_management = form.save(commit=False)
        orderidofdo = delivery_management.daily_order_id
        
        selected_package = daily_orders.objects.get(pk=orderidofdo.pk)  
        package_id = selected_package.package_id

        packagedays = Package.objects.get(pk=package_id.pk) 
        gap_days = packagedays.gap_days
        package_days = packagedays.package_days

        start_date_str = self.request.POST.get('Date') 
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None  # Assuming start date is submitted via form
        
        multiplication_result = package_days * 1
        current_date = start_date  # Initial current date

        with transaction.atomic():
            for i in range(multiplication_result):
                delivery_management.pk = None  

                # Set the date for each row with different gap days
                delivery_management.Date = current_date  
                delivery_management.save()

                # Update current date for the next iteration
                current_date += timedelta(days=gap_days + 1)

        return redirect(self.success_url)


@never_cache
@login_required 
def DelieverylistView(request):
    customers = Delievery_Management.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/delievery_list.html', {'customers': customers,'today': today}) 







def ScheduleDelete(request, pk):
    customer = get_object_or_404(Delievery_Management, pk=pk)
    customer.delete()
    return redirect('Delievery_list')



@never_cache
@login_required 
def ScheduleEdit(request, pk):
    customer = get_object_or_404(Delievery_Management, pk=pk)
    if request.method == "POST":
        form = Delievery_ManagementForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('Delievery_list')
           
    else:
        form = Delievery_ManagementForm(instance=customer)
    
    orderss = orders.objects.all()
    dailyorderss = daily_orders.objects.all()
    customers = Customer_list.objects.all()
    
    return render(request, 'shrihariapp/delievrysetup.html', {'form': form, 'orderss': orderss,'dailyorderss': dailyorderss,'customers': customers})      


@csrf_exempt
def delievered(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Delievery_Management, id=leave_id)
        leave_instance.delievery_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'Item status Changed to Delievered'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def stop(request):
    if request.method == 'POST':
        leave_id = request.POST.get('order_id')
        leave_instance = get_object_or_404(daily_orders, id=leave_id)
        leave_instance.approved_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'Service Has Been Paused'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



# @csrf_exempt
# def resume(request):
#     if request.method == 'POST':
#         leave_id = request.POST.get('leave_idd')
#         leave_instance = get_object_or_404(daily_orders, id=leave_id)
#         leave_instance.approved_status = 0
#         leave_instance.save()
#         return JsonResponse({'message': 'Service  Resume'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)                




@csrf_exempt
def resume(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_idd')
        leave_instance = get_object_or_404(daily_orders, id=leave_id)
        leave_instance.approved_status = 0
        leave_instance.save()
        
        # Update delivery dates
        delivery_management = Delievery_Management.objects.filter(daily_order_id=leave_instance)
        current_date = timezone.now().date()
        gap_days = 3
        
        with transaction.atomic():
            for i, dm in enumerate(delivery_management):
                dm.Date = current_date
                dm.save()
                current_date += timedelta(days=gap_days + 1)

        return JsonResponse({'message': 'Service Resume'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)