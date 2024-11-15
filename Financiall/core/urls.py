from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="core_home"),
    path('account/new', views.create_account, name="account_create"),
    path('account/<str:id>', views.read_account, name="account_read"),
    path('account/<str:id>/new', views.create_mutation, name="mutation_create"),
]
