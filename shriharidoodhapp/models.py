from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# class Users(AbstractUser):

#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
#     firstname = models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     username = models.EmailField(unique=True)
#     phone = models.IntegerField(blank=True, null=True)
#     role = models.CharField(max_length=100)
    
    

   
#     groups = models.ManyToManyField(Group, related_name='employee_groups')
#     user_permissions = models.ManyToManyField(Permission, related_name='employee_user_permissions')

#     def __str__(self):
#         return self.email


class Products(models.Model):
    USERNAME_FIELD = 'apply_by'  
    apply_by = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    varient = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    mrpprice = models.IntegerField()
    saleprice = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    product_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.CharField(blank=True, null=True ,max_length=500)

class Package(models.Model):
    apply_by = models.CharField(max_length=100)
    products = models.ManyToManyField(Products)
    package_name = models.CharField(max_length=30)
    package_price = models.CharField(max_length=30)
    package_days = models.IntegerField()
    gap_days = models.IntegerField(blank=True, null=True)
    package_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.CharField(blank=True, null=True ,max_length=500)

class ProductPackageMapping(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)



class Customer_list(AbstractUser):
    # USERNAME_FIELD = 'created_by'  
    # created_by = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    customer_address = models.CharField(max_length=100)
    customer_city = models.CharField(max_length=100,blank=True, null=True)
    customer_dist = models.CharField(max_length=100,blank=True, null=True)
    customer_plan = models.CharField(max_length=100,blank=True, null=True)
    approved_status = models.IntegerField(default=0)
    username = models.EmailField(unique=True,null=True)
    phone = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100)   
    package = models.ForeignKey(Package, on_delete=models.CASCADE ,blank=True, null=True)
    

    groups = models.ManyToManyField(Group, related_name='customer_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customer_user_permissions')

    def __str__(self):
        return self.email

    # def __str__(self):
    #     return f"{self.package.package_name} by {self.username}"  


class orders(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.ForeignKey(Customer_list, on_delete=models.CASCADE)
    order_date = models.DateField()
    approved_status = models.IntegerField(default=0)   
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    delievery_address = models.CharField(max_length=100)
    order_qty = models.IntegerField()

    
    def __str__(self):
        return f"Fine for {self.product.product_name} by {self.created_by}"

    def __str__(self):
        return f"Fine for {self.customer.username} by {self.created_by}" 

    def __str__(self):
        return f"Order #{self.id}"     


class daily_orders(models.Model):
    USERNAME_FIELD = 'created_by'  
    created_by = models.ForeignKey(Customer_list, on_delete=models.CASCADE)
    start_date = models.DateField()
    approved_status = models.IntegerField(default=0)   
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    delievery_address = models.CharField(max_length=100,blank=True, null=True)
    customer_plan = models.CharField(max_length=100,blank=True, null=True)
    description = models.CharField(blank=True, null=True ,max_length=500)
   

    
    # def __str__(self):
    #     return f"Fine for {self.package.package_name} by {self.created_by}"

    # def __str__(self):
    #     return f"Fine for {self.order.username} by {self.created_by}"                      

class Delievery_Management(models.Model):
    USERNAME_FIELD = 'created_by'  
    Delivery_Boy = models.ForeignKey(Customer_list, on_delete=models.CASCADE)
    Date = models.DateField(blank=True, null=True)
    orderid = models.ForeignKey(orders, on_delete=models.CASCADE,blank=True, null=True)  
    daily_order_id = models.ForeignKey(daily_orders, on_delete=models.CASCADE,blank=True, null=True)
    delievery_status = models.IntegerField(default=0)
    delievery_type = models.CharField(blank=True, null=True ,max_length=100)




    
