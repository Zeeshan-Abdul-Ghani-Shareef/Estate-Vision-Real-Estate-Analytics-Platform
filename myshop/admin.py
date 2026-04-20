from django.contrib import admin

from .models import Customer,Category,Supplier,Product,Cart,Shipping_Address,Order


class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','full_name','username','email','country','city','address')

admin.site.register(Customer,CustomerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','description','image')

admin.site.register(Category,CategoryAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display=('id','company_name','username','email','country','city','address')

admin.site.register(Supplier,SupplierAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=('id','product_name','product_category','price')

admin.site.register(Product,ProductAdmin)

admin.site.register(Cart)

admin.site.register(Shipping_Address)

admin.site.register(Order)