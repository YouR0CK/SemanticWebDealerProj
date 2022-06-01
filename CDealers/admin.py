from django.contrib import admin

from CDealers.models import Engine, Car, Employee, Dealer, CustomUser

admin.site.register(Engine)
admin.site.register(Car)
admin.site.register(Employee)
admin.site.register(Dealer)
admin.site.register(CustomUser)