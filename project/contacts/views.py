from rest_framework import generics
from .models import ContactsUser
from .serializers import ContactsUserSerializer



# Create your views here.
class ContactstUserView(generics.ListCreateAPIView):
    queryset = ContactsUser.objects.all()
    serializer_class = ContactsUserSerializer
    filterset_fields = ['fullName', 'numberPhone']
    search_fields = ['fullName']
    ordering_fields = ['fullName']

class ContactsUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactsUser.objects.all()
    serializer_class = ContactsUserSerializer 