from django.urls import path
from . import views


urlpatterns = [
    path('contacts/',views.ContactstUserView.as_view(),name='contact-list'),
    path('contacts/<int:pk>/',views.ContactsUserDetailView.as_view(),name='contact-detail'),
]