from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
# from userprojectappone.models import Registration
from django.forms import ValidationError



class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_superuser"]


class SuperUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "is_superuser"]

    # def authenticate_superuser(self, data):
    #     if data["is_superuser"] == False:
    #         raise ValidationError("User not allowed")
    #     return data


