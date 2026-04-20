from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):   
    full_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.full_name


class Supplier(models.Model):
    
    company_name = models.CharField(max_length=100, null=True)
    contact_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.company_name
    

class Category(models.Model):
   
    category_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(
        upload_to='category_image/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.category_name  
    

class Product(models.Model):

    lorem="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
       
    product_name = models.CharField(max_length=100, null=True)

    product_category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1
    )

    description = models.TextField(default=lorem)

    price=models.DecimalField(max_digits=10,decimal_places=2)

    image = models.ImageField(
        upload_to='product_image/',
        blank=True,
        null=True
    )

    unitinstock=models.PositiveIntegerField()

    def __str__(self):
        return self.product_name      
    

class Shipping_Address(models.Model):

    order_date = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=14,null=True)
    shipping_address=models.CharField(max_length=1000,null=True)
    shipping_city=models.CharField(max_length=100,null=True)
    shipping_state=models.CharField(max_length=100,null=True)
    shipping_country=models.CharField(max_length=100,null=True)
    shipping_zip=models.CharField(max_length=100,null=True)   
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.contact      


class Order(models.Model):

    STATUS_CHOICES={
        ('pending','Pending'),
        ('processing','Processing'),
        ('shiped','Shiped'),
        ('delivered','Delivered')
    }
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    shiped=models.ForeignKey(
        Shipping_Address,
        on_delete=models.CASCADE,
        default=1
    )

    total_quantity=models.PositiveIntegerField(null=True)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    order_date = models.DateTimeField(auto_now_add=True,null=True)    

    def __str__(self):
           return f"{self.id} user: {self.user.first_name} order: {self.order_date} ->  {self.status}  {self.total_quantity} {self.total_price}"      




class Cart(models.Model):
   
    cart_product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        default=1
    )

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    order=models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        default=1      
    )

    quantity=models.IntegerField(default=1)

    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"order:{self.order.id}->{self.order.order_date}  {self.order.status}  {self.order.total_quantity} {self.order.total_price}  cart: {self.id}-> {self.cart_product.product_name}  {self.cart_product.price} x {self.quantity} "      

