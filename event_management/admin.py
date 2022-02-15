from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'client_info', 'contract_info', 'support_contact_info')

    def event_id(self, obj):
        return f"Event: {obj.contract.id}"

    def client_info(self, obj):
        return str(obj.client)

    def contract_info(self, obj):
        return f"Contract: {obj.contract.id}"

    def support_contact_info(self, obj):
        return str(obj.support_contact)


admin.site.register(Event, EventAdmin)
