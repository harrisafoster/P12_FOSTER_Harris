from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'landline', 'mobile', 'company_name', 'date_created',
                  'date_updated', 'sales_contact']

    def validate_sales_contact(self, sales_contact):
        if not sales_contact.groups.filter(name="sales").exists():
            raise serializers.ValidationError("Sales_contact must be on the sales team.")
        else:
            return sales_contact

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client
