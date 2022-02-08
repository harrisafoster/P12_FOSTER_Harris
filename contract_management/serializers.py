from rest_framework import serializers

from .models import Contract
from event_management.models import Event


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'client', 'sales_contact', 'date_created', 'date_updated', 'status', 'amount',
                  'payment_due_date']

    def validate_sales_contact(self, sales_contact):
        if not sales_contact.groups.filter(name="sales").exists():
            raise serializers.ValidationError("Sales_contact must be on sales team.")
        else:
            return sales_contact

    def create(self, validated_data):
        contract = Contract.objects.create(**validated_data)
        event = Event.objects.create(contract=contract, client=contract.client)
        contract.save()
        event.save()
        return contract

    def update(self, instance, validated_data):
        validated_data.pop('client', None)
        return super().update(instance, validated_data)
