from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        frontend_url = settings.FRONTEND_URL
        return f"{frontend_url}/account/confirm-email/{emailconfirmation.key}"