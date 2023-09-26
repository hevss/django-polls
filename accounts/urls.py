from django.urls import path

from accounts import views

urlpatterns = [
    path(
        'cadastro/signup',
        views.AccountsCreateView.as_view(),
        name="signup"
        )
]