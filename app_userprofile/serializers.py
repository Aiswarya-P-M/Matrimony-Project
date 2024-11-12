from rest_framework import serializers
from .models import UserProfile

class UserProfileserializers(serializers.ModelSerializer):
    Profile_img_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'  # Includes all fields, including Profile_img

    def get_Profile_img_url(self, obj):
        if obj.Profile_img:
            return obj.Profile_img.url  # Returns the URL of the uploaded image
        return None