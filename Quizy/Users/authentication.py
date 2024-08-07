# users/authentication.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            if '@' in username:
                user = UserModel.objects.get(email=username)
            else:
                # Check both username and user_id fields
                user = UserModel.objects.get(models.Q(username=username) | models.Q(user_id=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
