from rest_framework import generics
from .models import ContactsUser
from .serializers import ContactsUserSerializer



# Create your views here.
class ContactstUserView(generics.ListCreateAPIView):
    queryset = ContactsUser.objects.all()
    serializer_class = ContactsUserSerializer

class ContactsUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactsUser.objects.all()
    serializer_class = ContactsUserSerializer 