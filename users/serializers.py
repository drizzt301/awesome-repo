from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "user_permissions",
            'password',
            "last_login",
            "is_superuser",
            "is_staff",
        )




# before
    # class TinyUserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         field = ("username", "superhost")