from rest_framework import serializers
from .models import ContactsUser
class ContactsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsUser
        fields = ['id','fullName','numberPhone']