from django.urls import path, include, re_path
from .. import views
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    # ---- Default dj-rest-auth Routes ----
    path("dj-rest-auth/", include("dj_rest_auth.urls")),

    # ---- Refresh Token Routes ----
    path("dj-rest-auth/token/refresh/", views.CookieTokenRefreshView.as_view()),

    # ---- Registration Routes ----
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    #re_path(r"^dj-rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$", views.CustomConfirmEmailView.as_view(), name="account_confirm_email"),

    # ---- Logout Routes ----
    path("dj-rest-auth/logout/", views.CustomLogoutView.as_view()),

    # ---- Password Reset Routes ----
    path("dj-rest-auth/password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("dj-rest-auth/password/reset/confirm/<str:uidb64>/<str:token>/", views.password_reset_confirm_redirect, name="password_reset_confirm"),
    path("dj-rest-auth/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

]