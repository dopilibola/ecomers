from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
# Register your models here.
 
admin.site.register(ShippingAddress)
 
admin.site.register(Order)
 
admin.site.register(OrderItem)

# Create order item inlanie 
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# Exteng our Order model 
class OrderAdmin(admin.ModelAdmin):
    model = Order 
    readonly_fields = ["date_ordered"]
    fields = ["user", "full_name","email", "shipping_address", "amount_paid", "date_ordered", "shipped" ]
    inlines = [OrderItemInline]

# Unregister Order MOdel 

admin.site.unregister(Order)

# Re-register our order and oroder Adims 
admin.site.register(Order, OrderAdmin)