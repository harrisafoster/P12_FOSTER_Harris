from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_name', 'client_company', 'sales_contact')

    def client_id(self, obj):
        return str(obj.id)

    def client_name(self, obj):
        return f"{str(obj.last_name).upper()}, {str(obj.first_name).capitalize()}"

    def client_company(self, obj):
        return str(obj.company_name)

    def sales_contact(self, obj):
        return str(obj.sales_contact)


admin.site.register(Client, ClientAdmin)
