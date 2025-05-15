from rest_framework import generics
from .models import ContactsUser
from .serializers import ContactsUserSerializer



# Create your views here.
class cantactUserView(generics.ListCreateAPIView):
    queryset = ContactsUser.objects.all()
    serializer_class = ContactsUserSerializer
