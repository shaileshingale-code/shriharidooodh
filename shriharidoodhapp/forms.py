# forms.py
from django import forms



from django import forms
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError  
from django.utils.translation import gettext as _
# from .models import Users
from .models import Products
from .models import Package
from .models import Customer_list
from .models import orders
from .models import daily_orders
from .models import Delievery_Management






class UserRegistrationForm(UserCreationForm):
    
    password2 = None
   
    
    # Make 'lastname' not required
    lastname = forms.CharField(required=False)
    
  
    

    class Meta:
        model = Customer_list
        fields = ['customer_name', 'customer_address', 'username', 'password1','phone','role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize the labels and help text
        self.fields['customer_name'].label = 'First Name'
        self.fields['customer_address'].label = 'Address'
        self.fields['username'].label = 'username'
        self.fields['password1'].label = 'Password'
        
        self.fields['phone'].label = 'phone'
        self.fields['role'].label = 'role'
        
        

        self.fields['customer_name'].help_text = 'Enter your name'
        self.fields['username'].help_text = 'Enter email Id'
        self.fields['password1'].help_text = 'Enter a password with at least one uppercase letter'
       

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
      
        if not any(char.isupper() for char in password1):
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
                code='password_no_upper',
            )

        return password1

    


class UserLoginForm(AuthenticationForm):
    
     class Meta:
        model = Customer_list
        fields = ['email', 'password']



class AddProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['product_name', 'varient', 'mrpprice', 'saleprice','product_image','description']
        labels = {
            'apply_by': 'Apply By',
            'product_name': 'product_name',
            'varient': 'varient',
            'mrpprice': 'mrpprice',
            'saleprice': 'saleprice',
            'product_image': 'product_image',
            'description': 'description',
        }
        help_texts = {
            'apply_by' : 'please enter your mail id',
            'product_name': 'Please enter product',
            'varient': 'Please enter varient',
            'mrpprice': 'Please enter mrp',
            'saleprice': 'Please enter sale price',
        }

class PackageForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=Products.objects.all(), widget=forms.SelectMultiple)

    class Meta:
        model = Package
        fields = ['apply_by', 'products', 'package_name', 'package_price' ,'package_days','package_image','gap_days']
        labels = {
            'apply_by': 'Apply By',
            'products': 'Products',
            'package_name': 'Package Name',
            'package_price': 'Price',
            'package_days': 'package_days',
            'package_image': 'package_image',
            'gap_days': 'gap_days',
        }
        help_texts = {
            'apply_by': 'Please enter your mail id',
            'products': 'Please select products',
            'package_name': 'Enter package name',
            'package_price': 'Enter package price',
            'package_days': 'Enter package days',
            'gap_days': 'Enter gap days',
        }


class CustomeraddForm(UserCreationForm):
    password2 = None

    class Meta:
        model = Customer_list
        fields = [ 'customer_name', 'start_date', 'password1', 'username', 'phone', 'role', 'customer_address', 'customer_city', 'customer_dist', 'customer_plan', 'package']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.fields['customer_name'].label = 'Customer Name'
        self.fields['start_date'].label = 'Start Date'
        self.fields['customer_address'].label = 'Customer Address'
        self.fields['customer_city'].label = 'Customer City'
        self.fields['customer_dist'].label = 'Customer District'
        self.fields['customer_plan'].label = 'Customer Plan'
        self.fields['package'].label = 'Package'
        self.fields['username'].label = 'email'
        self.fields['phone'].label = 'Phone'
        self.fields['role'].label = 'Role'

        
        self.fields['customer_name'].help_text = 'Customer name required'
        self.fields['start_date'].help_text = 'Date is required'
        self.fields['customer_address'].help_text = 'Address is required'
        self.fields['customer_city'].help_text = 'City required'
        self.fields['customer_dist'].help_text = 'District is required'
        self.fields['customer_plan'].help_text = 'Plan is required'
        self.fields['package'].help_text = 'Package is required'
        self.fields['username'].help_text = 'email is required'

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
      
        if not any(char.isupper() for char in password1):
            raise ValidationError(
                "The password must contain at least one uppercase letter.",
                code='password_no_upper',
            )

        return password1






class OrderForm(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['order_date', 'product_id', 'delievery_address','created_by','order_qty']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id', None)
        super().__init__(*args, **kwargs)
        if product_id:
            self.fields['product_id'].initial = product_id



class OrderFormtwo(forms.ModelForm):
    class Meta:
        model = daily_orders
        fields = ['start_date', 'package_id', 'delievery_address', 'created_by', 'customer_plan']

    def __init__(self, *args, **kwargs):
        package_id = kwargs.pop('package_id', None)  
        super().__init__(*args, **kwargs)
        if package_id:
            self.fields['package_id'].initial = package_id




class UserEditForm(forms.ModelForm):
    password2 = None

    class Meta:
        model = Customer_list
        fields = ['customer_name', 'customer_address', 'phone', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].label = 'Customer Name'
        self.fields['customer_address'].label = 'Customer Address'
        self.fields['phone'].label = 'Phone'
        self.fields['role'].label = 'Role'
        self.fields['customer_name'].help_text = 'Customer name required'

    


class ChangeDetailsForm(UserCreationForm):
    password2 = None

    class Meta:
        model = Customer_list
        fields = [ 'password1', 'role']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
     

        
      

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
      
        if not any(char.isupper() for char in password1):
            raise ValidationError(
                "The password must contain at least one uppercase letter.",
                code='password_no_upper',
            )

        return password1

   

    

class Delievery_ManagementForm(forms.ModelForm):
    class Meta:
        model = Delievery_Management
        fields = ['Delivery_Boy', 'Date', 'orderid','daily_order_id']

    # def __init__(self, *args, **kwargs):
    #     product_id = kwargs.pop('product_id', None)
    #     super().__init__(*args, **kwargs)
    #     if product_id:
    #         self.fields['product_id'].initial = product_id



# class Delievery_ManagementForm(forms.ModelForm):
#     class Meta:
#         model = Delievery_Management
#         fields = ['Delivery_Boy', 'Date', 'orderid', 'daily_order_id']

#     def save(self, commit=True):
#         instance = super().save(commit=False)

#         # Fetch package_id from daily_orders model
#         package_id = self.cleaned_data.get('daily_order_id').package_id

        
#         package = Package.objects.get(package_id=package_id)
#         package_days = package.package_days
#         gap_days = package.gap_days

        
#         total_instances = package_days * gap_days

        
#         if commit:
#             for i in range(total_instances):
#                 instance.pk = None  
#                 instance.save()

#         return instance
