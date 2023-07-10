from django.contrib import admin
from .models import Employ, Products, PaymentMethods, Operations, Check

admin.site.register(Employ)
admin.site.register(Products)
admin.site.register(PaymentMethods)
admin.site.register(Operations)
admin.site.register(Check)
