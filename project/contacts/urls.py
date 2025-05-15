from django.urls import path
from . import views


urlpatterns = [
    path('contacts/',views.ContactstUserView.as_view(),name='cantact-list'),
]