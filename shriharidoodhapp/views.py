from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import requests
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
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
import json
from datetime import datetime
from datetime import date
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
import random
from django.db.models import Count
from django.conf import settings
import requests
import hashlib
import json
import base64
import razorpay
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

from .forms import UsernameForm, CustomSetPasswordForm










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



# class UserRegistrationView(CreateView):
#     model = Customer_list
#     form_class = UserRegistrationForm
#     template_name = 'shrihariapp/registration.html'
#     success_url = reverse_lazy('admin_login')

#     def form_valid(self, form):
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

#         try:
#             whatsapp_response = requests.get(whatsapp_api_url, params=whatsapp_api_params)
#             print("WhatsApp API Response:", whatsapp_response.text)
#             self.request.session['whatsapp_response'] = whatsapp_response.text
#             messages.success(self.request, whatsapp_response.text)
#         except requests.RequestException as e:
#             print("Error sending WhatsApp message:", e)
#             self.request.session['whatsapp_response'] = "Error: Failed to send WhatsApp message."
#             messages.error(self.request, "Error: Failed to send WhatsApp message.")

#         response = super().form_valid(form)

#         subject = 'Welcome to Shri hari doodh !'
#         message = 'Thank you for registering to Shri Hari doodh. We hope you enjoy using our platform.'
#         from_email = 'info@shreeharidoodh.in'  # Change to your email
#         to_email = form.cleaned_data['username']  # Assuming your form has an email field
#         send_mail(subject, message, from_email, [to_email])

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
#     success_url = reverse_lazy('admin_login')

#     def form_valid(self, form):
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

#         try:
#             whatsapp_response = requests.get(whatsapp_api_url, params=whatsapp_api_params)
#             print("WhatsApp API Response:", whatsapp_response.text)
#             self.request.session['whatsapp_response'] = whatsapp_response.text
#             messages.success(self.request, whatsapp_response.text)
#         except requests.RequestException as e:
#             print("Error sending WhatsApp message:", e)
#             self.request.session['whatsapp_response'] = "Error: Failed to send WhatsApp message."
#             messages.error(self.request, "Error: Failed to send WhatsApp message.")

      
#         messages.success(self.request, "Registration successful!")

#         subject = 'Welcome to Shri hari doodh !'
#         message = 'Thank you for registering to Shri Hari doodh. We hope you enjoy using our platform.'
#         from_email = 'info@shreeharidoodh.in'  # Change to your email
#         to_email = form.cleaned_data['username']  # Assuming your form has an email field
#         send_mail(subject, message, from_email, [to_email])

#         response = super().form_valid(form)

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
        # Prepare SMS API request details
        phone_number = form.cleaned_data.get('phone')
        sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
        sms_api_params = {
            'mobile': '9987952450',
            'pass': 'Dreamz@2024',
            'senderid': 'SWATKH',
            'to': phone_number,  # The recipient's phone number
            'msg': f'We acknowledge that you want to pause/hold your order ID: {phone_number} - SWATI Shree Hari Doodh'  # The message to send
        }

        try:
            sms_response = requests.get(sms_api_url, params=sms_api_params)
            sms_response.raise_for_status()  # Raise an exception for HTTP errors
            response_message = sms_response.text
            print("SMS API Response:", response_message)
            self.request.session['sms_response'] = response_message
            # messages.success(self.request, response_message)

        except requests.RequestException as e:
            print("Error sending SMS:", e)
            error_message = f"Error: Failed to send SMS. {e}"
            self.request.session['sms_response'] = error_message
            messages.error(self.request, error_message)

      

        phone_number = form.cleaned_data.get('phone')
        sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
        sms_api_params = {
            'mobile': '9987952450',
            'pass': 'Dreamz@2024',
            'senderid': 'SWATKH',
            'to': '8421263364',  # The recipient's phone number
            'msg': f'We acknowledge that you want to pause/hold your order ID: {phone_number} - SWATI Shree Hari Doodh'  # The message to send
        }

        try:
            sms_response = requests.get(sms_api_url, params=sms_api_params)
            sms_response.raise_for_status()  # Raise an exception for HTTP errors
            response_message = sms_response.text
            print("SMS API Response:", response_message)
            self.request.session['sms_response'] = response_message
            # messages.success(self.request, response_message)

        except requests.RequestException as e:
            print("Error sending SMS:", e)
            error_message = f"Error: Failed to send SMS. {e}"
            self.request.session['sms_response'] = error_message
            messages.error(self.request, error_message)  

            

        messages.success(self.request, "Registration successful!")

        subject = 'Welcome to Shri hari doodh !'
        message = 'Thank you for registering to Shri Hari doodh. We hope you enjoy using our platform.'
        from_email = 'info@shreeharidoodh.in'  # Change to your email
        to_email = form.cleaned_data['username']  # Assuming your form has an email field
        send_mail(subject, message, from_email, [to_email])

        
        subject = 'Welcome to Shri hari doodh !'
        message = 'you have new registration please check it by login.'
        from_email = 'info@shreeharidoodh.in'  # Change to your email
        to_email = 'info@shreeharidoodh.in'  # Assuming your form has an email field
        send_mail(subject, message, from_email, [to_email])
        

        response = super().form_valid(form)

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

# @never_cache
# @login_required    
# def Dashboard(request):
    
#     return render(request, 'shrihariapp/Dashboard.html')

@never_cache
@login_required
def Dashboard(request):
    user = request.user
    if user.role == 'admin':
        customer_count = Customer_list.objects.filter(role='customer').count()
        product_count = Products.objects.count()
        order_count1 = orders.objects.count()
        order_count2 = daily_orders.objects.count()
        delivery_count_by_order = Delievery_Management.objects.values('orderid').annotate(count=Count('orderid')).count()
        
        context = {
            'customer_count': customer_count,
            'product_count': product_count,
            'order_count1': order_count1,
            'order_count2': order_count2,
            'delivery_count_by_order':delivery_count_by_order
        }
        
        return render(request, 'shrihariapp/Dashboard.html', context)
    elif user.role == 'customer':
        return redirect('product_list')
    else:
        return redirect('Delievery_list')
        



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

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Record Added successfully!')
        return response

@never_cache
@login_required 
def ProductListView(request):
    products = Products.objects.all()
    return render(request, 'shrihariapp/product_list.html', {'products': products})      



def Product_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    messages.success(request, 'Record Deleted Successfully.')
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
            
#             # If the image is not changed, just save the form without image processing
#             else:
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
            
            # Check if a new image file is uploaded
            if 'product_image' in request.FILES:
                # Save the image file
                new_product.product_image = request.FILES['product_image']
            
            # Save the product with updated information
            new_product.save()
            messages.success(request, 'Record Edited Successfully.')
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
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Record Added successfully!')
        return response


@never_cache
@login_required 
def PackageListView(request):
    packages = Package.objects.all()
    return render(request, 'shrihariapp/package_list.html', {'packages': packages})  


def Packagedelete(request, pk):
    package = get_object_or_404(Package, pk=pk)
    package.delete()
    messages.success(request, 'Record Edited Successfully.')
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


# @never_cache
# @login_required 
# def Packageedit(request, pk):
#     package = get_object_or_404(Package, pk=pk)
    
#     if request.method == "POST":
#         form = PackageForm(request.POST, request.FILES, instance=package)
#         if form.is_valid():
#             new_package = form.save(commit=False)
            
#             # Save the package image if it's changed
#             if 'package_image' in request.FILES:
#                 new_package.package_image.save(request.FILES['package_image'].name, request.FILES['package_image'], save=False)
            
#             # If the image is not changed, just save the form without image processing
#             else:
#                 new_package.save()

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
            
            # Check if a new image file is uploaded
            if 'package_image' in request.FILES:
                # Save the image file
                new_package.package_image = request.FILES['package_image']
            
            # Save the package with updated information
            new_package.save()
            messages.success(request, 'Record Edited Successfully.')
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

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Customer successfully registered!')
        return response    


@never_cache
@login_required 
def CustomerListView(request):
    customers = Customer_list.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/customer_list.html', {'customers': customers,'today': today})   




def Customerdelete(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    customer.delete()
    messages.success(request, 'Customer deleted successfully.')
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
            messages.success(request, 'Customer Record Updated successfully.')
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
            messages.success(request, 'Password Updated successfully.')
            return redirect('customer_list')
    else:
        form = ChangeDetailsForm(instance=customer)
    
    packages = Package.objects.all()
    
    return render(request, 'shrihariapp/changedetails.html', {'form': form, 'packages': packages})




# def order_create(request, product_id):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.instance.created_by = request.user
#             form.instance.product_id_id = product_id
#             form.save()
#             messages.success(request, 'Order Created Successfully.')
#             return redirect('order_list')  # Redirect to a success page
#     else:
#         form = OrderForm(product_id=product_id)
#     return render(request, 'shrihariapp/order_create.html', {'form': form,'product_id': product_id})




# def order_create(request, product_id):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.instance.created_by = request.user
#             form.instance.product_id_id = product_id
#             form.save()

#             # Extract phone number from the logged-in user
#             phone_number = request.user.phone  # Assuming the User model has a phone field
            
#             # Prepare SMS API request details
#             sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
#             sms_api_params = {
#                 'mobile': '9987952450',
#                 'pass': 'Dreamz@2024',
#                 'senderid': 'SWATKH',
#                 'to': phone_number,  # Use the phone number from the logged-in user
#                 'msg': 'Thank you for your order. You will receive an order confirmation message shortly! - SWATKH'  # The message to send
#             }

#             try:
#                 sms_response = requests.get(sms_api_url, params=sms_api_params)
#                 sms_response.raise_for_status()  # Raise an exception for HTTP errors
#                 response_message = sms_response.text
#                 print("SMS API Response:", response_message)
#                 messages.success(request, f'Order Created Successfully.')
#             except requests.RequestException as e:
#                 print("Error sending SMS:", e)
#                 error_message = f"Error: Failed to send SMS. {e}"
#                 messages.error(request, error_message)
            
#             return redirect('order_list')  # Redirect to a success page
#     else:
#         form = OrderForm(product_id=product_id)
#     return render(request, 'shrihariapp/order_create.html', {'form': form, 'product_id': product_id})




def order_create(request, product_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.instance.product_id_id = product_id
            order = form.save()

          
            phone_number = request.user.phone 


            product = Products.objects.get(id=product_id)
            amount = int(product.saleprice * 100)

            
            razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            
            amount = amount  
            currency = 'INR'
            receipt = f'order_{order.id}'
            notes = {
                'order_id': order.id,
                'product_id': product_id
            }

            razorpay_order = razorpay_client.order.create({
                'amount': amount,
                'currency': currency,
                'receipt': receipt,
                'notes': notes
            })

            order.razorpay_order_id = razorpay_order['id']
            order.save()

            callback_url = request.build_absolute_uri(reverse('payment_callback'))

            context = {
                'order': order,
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount,
                'currency': currency,
                'phone_number': phone_number,
                'callback_url': callback_url
            }

            return render(request, 'shrihariapp/razorpay_payment.html', context)
    else:
        form = OrderForm(product_id=product_id)
    
    return render(request, 'shrihariapp/order_create.html', {'form': form, 'product_id': product_id})




@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        try:
            razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            payment_id = request.POST.get('razorpay_payment_id')
            order_id = request.POST.get('razorpay_order_id')
            signature = request.POST.get('razorpay_signature')
            order_pk = request.POST.get('order_id')


            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            result = razorpay_client.utility.verify_payment_signature(params_dict)
            
            print("orderid:", result) 
            # if result is None:
                # Fetch the order using the razorpay_order_id
            order = orders.objects.get(pk=order_pk)
            order.payment_id = payment_id
            order.payment_status = 'Paid'
            order.save()
            messages.success(request, 'Payment Successful.')
            # else:
            #     messages.error(request, 'Payment Verification Failed.')

        except orders.DoesNotExist:
            messages.error(request, 'Order does not exist.')
        except Exception as e:
            print("Error during payment verification:", e)
            messages.error(request, 'Error during payment verification.')

    return redirect('order_list')   










@never_cache
@login_required 
def OrderListView(request):
    orderss = orders.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/order_list.html', {'orderss': orderss,'today': today}) 



# def order_createtwo(request, package_id):
#     if request.method == 'POST':
#         form = OrderFormtwo(request.POST)
#         if form.is_valid():
#             form.instance.created_by = request.user
#             # form.instance.package_id = package_id
#             form.save()
#             messages.success(request, 'Order Created Successfully.')
#             return redirect('daily_list')  # Redirect to a success page
#     else:
#         form = OrderFormtwo(package_id=package_id)
#     return render(request, 'shrihariapp/order_createtwo.html', {'form': form,'package_id': package_id})




def order_createtwo(request, package_id):
    if request.method == 'POST':
        form = OrderFormtwo(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.instance.package_id_id = package_id
            order=form.save()

            

          
            phone_number = request.user.phone 


            package = Package.objects.get(id=package_id)
            amount = int(package.package_price * 100)

            
            razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            
            amount = amount  
            currency = 'INR'
            receipt = f'order_{order.id}'
            notes = {
                'order_id': order.id,
                'package_id': package_id
            }

            razorpay_order = razorpay_client.order.create({
                'amount': amount,
                'currency': currency,
                'receipt': receipt,
                'notes': notes
            })

            order.razorpay_order_id = razorpay_order['id']
            order.save()

            callback_url = request.build_absolute_uri(reverse('payment_callbacktwo'))

            context = {
                'order': order,
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount,
                'currency': currency,
                'phone_number': phone_number,
                'callback_url': callback_url
            }

            return render(request, 'shrihariapp/razorpay_payment.html', context)
    else:
        form = OrderFormtwo(package_id=package_id)
    return render(request, 'shrihariapp/order_createtwo.html', {'form': form, 'package_id': package_id})

@csrf_exempt
def payment_callbacktwo(request):
    if request.method == 'POST':
        try:
            razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            payment_id = request.POST.get('razorpay_payment_id')
            order_id = request.POST.get('razorpay_order_id')
            signature = request.POST.get('razorpay_signature')
            order_pk = request.POST.get('order_id')


            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            result = razorpay_client.utility.verify_payment_signature(params_dict)
            
            print("orderid:", result) 
          
            order = daily_orders.objects.get(pk=order_pk)
            order.payment_id = payment_id
            order.payment_status = 'Paid'
            order.save()
            messages.success(request, 'Payment Successful.')
            # else:
            #     messages.error(request, 'Payment Verification Failed.')

        except orders.DoesNotExist:
            messages.error(request, 'Order does not exist.')
        except Exception as e:
            print("Error during payment verification:", e)
            messages.error(request, 'Error during payment verification.')

    return redirect('daily_list')   

@never_cache
@login_required 
def DailyOrderListView(request):
    ordersss = daily_orders.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/dailyorder_list.html', {'ordersss': ordersss,'today': today})     




def Orderdelete(request, pk):
    orderd = get_object_or_404(daily_orders, pk=pk)
    orderd.delete()
    messages.success(request, 'Order deleted Successfully.')
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
            messages.success(request, 'Order edited Successfully.')
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

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Record Added successfully!')
        return response

@never_cache
@login_required 
def BoyListView(request):
    customers = Customer_list.objects.all()
    
    today = date.today()

    return render(request, 'shrihariapp/boy_list.html', {'customers': customers,'today': today}) 



def Boydelete(request, pk):
    customer = get_object_or_404(Customer_list, pk=pk)
    customer.delete()
    messages.success(request, 'Record Deleted Successfully.')
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
            messages.success(request, 'Record Edited Successfully.')
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

    def form_valid(self, form):
        delivery_management = form.save(commit=False)
        orderidofdo = delivery_management.orderid
 
        selected_package = orders.objects.get(pk=orderidofdo.pk)  
        delivery_management.Date = selected_package.order_date
        delivery_management.delievery_type = "single order"
        
        
        delivery_management.save()
        
        return super().form_valid(form)            


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
        Date=selected_package.start_date

        packagedays = Package.objects.get(pk=package_id.pk) 
        gap_days = packagedays.gap_days
        package_days = packagedays.package_days

        # start_date_str = Date
        start_date = Date  
        # start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None  
        
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
    messages.success(request, 'Record Deleted Successfully.')
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
            messages.success(request, 'Record updated Successfully.')
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

        customer_email = leave_instance.created_by.username
        customer_phone = leave_instance.created_by.phone

        subject = 'Subscription Pause Request'
        message = f'Subscription has been paused for order :{leave_id}'
        from_email = 'info@shreeharidoodh.in' 
        to_email = customer_email  
        send_mail(subject, message, from_email, [to_email])


        subject = 'Subscription Pause Request'
        message = f'Subscription has been paused for order :{leave_id}'
        from_email = 'info@shreeharidoodh.in' 
        to_email = 'info@shreeharidoodh.in'  
        send_mail(subject, message, from_email, [to_email])


        sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
        sms_api_params = {
            'mobile': '9987952450',
            'pass': 'Dreamz@2024',
            'senderid': 'SWATKH',
            'to': customer_phone,
            'msg': f'Alert! Order ID: {leave_id} has been PAUSED.- SWATI Shree Hari Doodh'
        }
        response = requests.get(sms_api_url, params=sms_api_params)


        sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
        sms_api_params = {
            'mobile': '9987952450',
            'pass': 'Dreamz@2024',
            'senderid': 'SWATKH',
            'to': '8421263364',
            'msg': f'Alert! Order ID: {leave_id} has been PAUSED.- SWATI Shree Hari Doodh'
        }
        response = requests.get(sms_api_url, params=sms_api_params)

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



@csrf_exempt
def stopforcustomer(request):
    if request.method == 'POST':
        leave_id = request.POST.get('order_id')
        leave_instance = get_object_or_404(daily_orders, id=leave_id)
        leave_instance.approved_status = 2
        leave_instance.save()

        customer_phone = leave_instance.created_by.phone

        subject = 'Subscription Pause Request'
        message = f'You have recieved request to pause the service for order ID {leave_id}. Please Login to admin Panel.'
        from_email = 'info@shreeharidoodh.in' 
        to_email = 'info@shreeharidoodh.in'  
        send_mail(subject, message, from_email, [to_email])

        sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
        sms_api_params = {
            'mobile': '9987952450',
            'pass': 'Dreamz@2024',
            'senderid': 'SWATKH',
            'to': customer_phone,
            'msg': f'We acknowledge that you want to pause/hold your order ID: {leave_id} - SWATI Shree Hari Doodh'
        }
        response = requests.get(sms_api_url, params=sms_api_params)


        sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
        sms_api_params = {
            'mobile': '9987952450',
            'pass': 'Dreamz@2024',
            'senderid': 'SWATKH',
            'to': '8421263364',
            'msg': f'We acknowledge that you want to pause/hold your order ID: {leave_id} - SWATI Shree Hari Doodh'
        }
        response = requests.get(sms_api_url, params=sms_api_params)

        return JsonResponse({'message': 'Request For Pause Subscription Has been raised Wait for admin Approval'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400) 



def send_otp(phone_number, otp):
    sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
    sms_api_params = {
        'mobile': '9987952450',
        'pass': 'Dreamz@2024',
        'senderid': 'SWATKH',
        'to': phone_number,
        # 'msg': f'Your OTP for password reset is {otp}.'
        'msg': f'Your mobile OTP to reset password is: {otp} - SWATI Shree Hari Doodh'
    }


    response = requests.get(sms_api_url, params=sms_api_params)
    return response.status_code == 200

# def forgot_password(request):
#     if request.method == 'POST':
#         form = UsernameForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             try:
#                 user = Customer_list.objects.get(username=username)
#                 request.session['reset_user_id'] = user.id
#                 return redirect('reset_password')
#             except Customer_list.DoesNotExist:
#                 messages.error(request, 'Username not found in our records.')
#     else:
#         form = UsernameForm()
#     return render(request, 'shrihariapp/forgot_password.html', {'form': form})



def forgot_password(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = Customer_list.objects.get(username=username)
                otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
                request.session['reset_user_id'] = user.id
                request.session['otp'] = otp
                if send_otp(user.phone, otp):
                    return redirect('verify_otp')
                else:
                    messages.error(request, 'Failed to send OTP. Please try again.')
            except Customer_list.DoesNotExist:
                messages.error(request, 'Username not found in our records.')
    else:
        form = UsernameForm()
    return render(request, 'shrihariapp/forgot_password.html', {'form': form})








def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == str(request.session.get('otp')):
            return redirect('reset_password')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, 'shrihariapp/verify_otp.html')


def send_notification(phone_number):
    sms_api_url = 'http://trans.dreamztechnolgy.org/smsstatuswithid.aspx'
    sms_api_params = {
        'mobile': '9987952450',
        'pass': 'Dreamz@2024',
        'senderid': 'SWATKH',
        'to': phone_number,
        'msg': 'Your password has been changed successfully. - SWATI Shree Hari Doodh'
    }
    response = requests.get(sms_api_url, params=sms_api_params)
    return response.status_code == 200
    

def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        user_id = request.session.get('reset_user_id')
        try:
            user = Customer_list.objects.get(id=user_id)
            user.password = make_password(new_password)
            user.save()

          
            subject = 'Welcome to Shri hari doodh!'
            message = 'Your password has been changed successfully. Thank you for using Shri Hari doodh.'
            from_email = 'info@shreeharidoodh.in'
            to_email = user.username
            send_mail(subject, message, from_email, [to_email])

            # Send SMS notification
            if user.phone:
                send_notification(user.phone)

            messages.success(request, 'Your password has been reset successfully.')
            return redirect('admin_login')
        except Customer_list.DoesNotExist:
            messages.error(request, 'User not found. Please try again.')
    return render(request, 'shrihariapp/reset_password.html')