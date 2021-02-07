from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_form.as_view(), name='signup'),
]
