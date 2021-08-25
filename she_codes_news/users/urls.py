from .views import CreateAccountView
from django.urls import path

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
]
