from django.urls import path
from .views import beaty_view, master_view, contacts_view

urlpatterns = [
    path("", beaty_view, name="beaty"),
    path("master/", master_view, name="master"),
    path("contacts/", contacts_view, name='contacts'),
]
