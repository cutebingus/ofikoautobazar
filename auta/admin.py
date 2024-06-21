from django.contrib import admin
from .models import Auta, Dealer, Customer

admin.site.register(Auta)
admin.site.register(Dealer)
admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'prijmeni', 'email', 'tel','adresa')