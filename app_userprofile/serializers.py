from rest_framework import serializers
from .models import UserProfile
from app_commonmatching.models import CommonMatchingTable, MasterTable

class UserProfileserializers(serializers.ModelSerializer):
    # Profile_img_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'  


    def validate_field(self, value, field_type):
    # Retrieve the type from CommonMatchingTable
        try:
            field_type_obj = CommonMatchingTable.objects.get(type=field_type)
        except CommonMatchingTable.DoesNotExist:
            raise serializers.ValidationError(f"Invalid field type: {field_type}")

        # Get valid values from the MasterTable for this type
        valid_values = MasterTable.objects.filter(type=field_type_obj).values_list('value', flat=True)

        if value not in valid_values:
            raise serializers.ValidationError(
                f"Invalid {field_type}. Valid values are: {', '.join(valid_values)}"
            )
        return value

    def validate_Gender(self, value):
        return self.validate_field(value, "gender")

    def validate_Religion(self, value):
        return self.validate_field(value, "religion")

    def validate_Caste(self, value):
        return self.validate_field(value, "caste")

    def validate_Profession(self, value):
        return self.validate_field(value, "profession")

    def validate_Education(self, value):
        return self.validate_field(value, "education")

    def validate_Location(self, value):
        return self.validate_field(value, "location")

    def validate_Language(self, value):
        return self.validate_field(value, "language")

    def validate_Marital_status(self, value):
        return self.validate_field(value, "marital_status")





    def get_Profile_img_url(self, obj):
        if obj.Profile_img:
            return obj.Profile_img.url  # Returns the URL of the uploaded image
        return None


     # def validate_Gender(self, value):
    #     # Check if the gender value exists in the MasterTable
    #     gender_type = CommonMatchingTable.objects.get(type="gender")  # Get the type for gender
    #     valid_values = MasterTable.objects.filter(type=gender_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid gender. Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Religion(self, value):
    #     # Check if the religion value exists in the MasterTable
    #     religion_type = CommonMatchingTable.objects.get(type="religion")  # Get the type for religion
    #     valid_values = MasterTable.objects.filter(type=religion_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid religion. Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Caste(self, value):
    #     # Check if the caste value exists in the MasterTable
    #     caste_type = CommonMatchingTable.objects.get(type="caste")  # Get the type for caste
    #     valid_values = MasterTable.objects.filter(type=caste_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid caste. Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Profession(self, value):
    #     # Check if the profession value exists in the MasterTable
    #     profession_type = CommonMatchingTable.objects.get(type="profession")  # Get the type for profession
    #     valid_values = MasterTable.objects.filter(type=profession_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid profession. Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Education(self, value):
    #     # Check if the education value exists in the MasterTable
    #     education_type = CommonMatchingTable.objects.get(type="education")  # Get the type for education
    #     valid_values = MasterTable.objects.filter(type=education_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid education. Valid values are: {', '.join(valid_values)}")
    #     return value


    # def validate_Location(self,value):
    #     location_type=CommonMatchingTable.objects.get(type="location")  # Get the type for location
    #     valid_values=MasterTable.objects.filter(type=location_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid location. Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Language(self,value):
    #     language_type=CommonMatchingTable.objects.get(type="language")  # Get the type for location
    #     valid_values=MasterTable.objects.filter(type=language_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid language. Valid values are: {', '.join(valid_values)}")
    #     return value
    
    
    # def validate_Marital_status(self,value):
    #     marital_status_type=CommonMatchingTable.objects.get(type="marital_status")  # Get the type for location
    #     valid_values=MasterTable.objects.filter(type= marital_status_type).values_list('value', flat=True)

    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid Status. Valid values are: {', '.join(valid_values)}")
    #     return value