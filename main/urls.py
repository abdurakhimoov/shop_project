from django.urls import path
from .views import HomePage, UserLoginView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]