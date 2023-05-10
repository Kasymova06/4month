from django.urls import path
from .views import get_contacts, get_about, get_hello 
urlpatterns = [
    path("contacts/", get_contacts, name="Contacts-view"),
    path("about/", get_about, name="About-view"),
    path("hello/", get_hello, name="Hello-view")
]