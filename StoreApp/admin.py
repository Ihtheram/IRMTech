from django.contrib import admin
from .models import PERSON, TECH, OrderInfo, OrderedTech, DeliveryLocation

# Register models.

admin.site.register(PERSON)
admin.site.register(TECH)
admin.site.register(OrderInfo)
admin.site.register(OrderedTech)
admin.site.register(DeliveryLocation)