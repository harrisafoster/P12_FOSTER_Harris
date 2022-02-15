from django.contrib import admin

from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_id', 'client', 'sales_contact')

    def contract_id(self,obj):
        return str(obj.id)

    def client(self,obj):
        return str(obj.client)

    def sales_contact(self, obj):
        return str(obj.sales_contact)


admin.site.register(Contract, ContractAdmin)
