from rest_framework import serializers
from app_preference.models import Preference
from app_commonmatching.models import CommonMatchingTable, MasterTable

class Preferenceserializers(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = "__all__"


    def validate_field(self, value, field_type, is_range=False, is_list=False):
        """
        Generic field validator.

        Args:
            value: The value to validate.
            field_type: The type of field (e.g., "gender", "religion").
            is_range: Whether the field is a range (list with two values).
            is_list: Whether the field is a list of values.

        Returns:
            The validated value.

        Raises:
            serializers.ValidationError: If validation fails.
        """
        # For range fields like Age, Height, Weight, Income
        if is_range:
            if not isinstance(value, list) or len(value) != 2:
                raise serializers.ValidationError(f"{field_type.capitalize()} must be a list with two values representing a range [min, max].")
            
            if not all(isinstance(item, int) for item in value):
                raise serializers.ValidationError(f"All values in {field_type.capitalize()} range must be integers.")

            if value[0] > value[1]:
                raise serializers.ValidationError(f"The minimum {field_type} must be less than or equal to the maximum {field_type}.")
            return value

        # Get valid values for this field type
        try:
            field_type_obj = CommonMatchingTable.objects.get(type=field_type)
            valid_values = MasterTable.objects.filter(type=field_type_obj).values_list('value', flat=True)
        except CommonMatchingTable.DoesNotExist:
            raise serializers.ValidationError(f"Invalid field type: {field_type}")

        # For list fields like Religion, Caste, Profession
        if is_list:
            if not isinstance(value, list):
                raise serializers.ValidationError(f"{field_type.capitalize()} should be a list of values.")
            
            #create a new list by iterating over each element (item) in the iterable value.
            invalid_values = [item for item in value if item not in valid_values]
            if invalid_values:
                raise serializers.ValidationError(
                    f"Invalid {field_type} values: {', '.join(invalid_values)}. "
                    f"Valid values are: {', '.join(valid_values)}."
                )
            return value

        # For single-value fields like Gender, Marital_status
        if value not in valid_values:
            raise serializers.ValidationError(
                f"Invalid {field_type}. Valid values are: {', '.join(valid_values)}."
            )
        return value


    def validate_Age(self, value):
        return self.validate_field(value, field_type="age", is_range=True)

    def validate_Height(self, value):
        return self.validate_field(value, field_type="height", is_range=True)

    def validate_Weight(self, value):
        return self.validate_field(value, field_type="weight", is_range=True)

    def validate_Income(self, value):
        return self.validate_field(value, field_type="income", is_range=True)

    def validate_Gender(self, value):
        return self.validate_field(value, field_type="gender")

    def validate_Religion(self, value):
        return self.validate_field(value, field_type="religion", is_list=True)

    def validate_Caste(self, value):
        return self.validate_field(value, field_type="caste", is_list=True)

    def validate_Profession(self, value):
        return self.validate_field(value, field_type="profession", is_list=True)

    def validate_Education(self, value):
        return self.validate_field(value, field_type="education", is_list=True)

    def validate_Location(self, value):
        return self.validate_field(value, field_type="location", is_list=True)

    def validate_Language(self, value):
        return self.validate_field(value, field_type="language", is_list=True)

    def validate_Marital_status(self, value):
        return self.validate_field(value, field_type="marital_status")












    # # Range field validation (Age, Height, Weight, Income)
    # def validate_Age(self, value):
    #     if not isinstance(value, list) or len(value) != 2:
    #         raise serializers.ValidationError("Age must be a list with two values representing a range [min, max].")
    #     if value[0] > value[1]:
    #         raise serializers.ValidationError("The minimum age must be less than or equal to the maximum age.")
    #     return value

    # def validate_Height(self, value):
    #     if not isinstance(value, list) or len(value) != 2:
    #         raise serializers.ValidationError("Height must be a list with two values representing a range [min, max].")
    #     if value[0] > value[1]:
    #         raise serializers.ValidationError("The minimum height must be less than or equal to the maximum height.")
    #     return value

    # def validate_Weight(self, value):
    #     if not isinstance(value, list) or len(value) != 2:
    #         raise serializers.ValidationError("Weight must be a list with two values representing a range [min, max].")
    #     if value[0] > value[1]:
    #         raise serializers.ValidationError("The minimum weight must be less than or equal to the maximum weight.")
    #     return value

    # def validate_Income(self, value):
    #     if not isinstance(value, list) or len(value) != 2:
    #         raise serializers.ValidationError("Income must be a list with two values representing a range [min, max].")
    #     if value[0] > value[1]:
    #         raise serializers.ValidationError("The minimum income must be less than or equal to the maximum income.")
    #     return value

    # # Single value validation for Gender, Religion, Caste, etc.
    # def validate_Gender(self, value):
    #     gender_type = CommonMatchingTable.objects.get(type="gender")
    #     valid_values = MasterTable.objects.filter(type=gender_type).values_list('value', flat=True)
    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid gender. Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Caste(self, value):
    #     # Ensure `Caste` is a list and all values exist in the MasterTable
    #     caste_type = CommonMatchingTable.objects.get(type="caste")
    #     valid_values = MasterTable.objects.filter(type=caste_type).values_list('value', flat=True)

    #     if not isinstance(value, list):
    #         raise serializers.ValidationError("Caste should be a list of values.")
        
    #     invalid_values = [item for item in value if item not in valid_values]
    #     if invalid_values:
    #         raise serializers.ValidationError(f"Invalid caste values: {', '.join(invalid_values)}. Valid values are: {', '.join(valid_values)}.")
    #     return value

    # def validate_Religion(self, value):
    #     # Ensure `Religion` is a list and all values exist in the MasterTable
    #     religion_type = CommonMatchingTable.objects.get(type="religion")
    #     valid_values = MasterTable.objects.filter(type=religion_type).values_list('value', flat=True)

    #     if not isinstance(value, list):
    #         raise serializers.ValidationError("Religion should be a list of values.")
        
    #     invalid_values = [item for item in value if item not in valid_values]
    #     if invalid_values:
    #         raise serializers.ValidationError(f"Invalid caste values: {', '.join(invalid_values)}. Valid values are: {', '.join(valid_values)}.")
    #     return value


    # # Multi-value validation for Profession, Education, Location, Language
    # def validate_Profession(self, value):
    #     profession_type = CommonMatchingTable.objects.get(type="profession")
    #     valid_values = MasterTable.objects.filter(type=profession_type).values_list('value', flat=True)
    #     if not all(item in valid_values for item in value):
    #         raise serializers.ValidationError(f"Invalid profession(s). Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Education(self, value):
    #     education_type = CommonMatchingTable.objects.get(type="education")
    #     valid_values = MasterTable.objects.filter(type=education_type).values_list('value', flat=True)
    #     if not all(item in valid_values for item in value):
    #         raise serializers.ValidationError(f"Invalid education(s). Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Location(self, value):
    #     location_type = CommonMatchingTable.objects.get(type="location")
    #     valid_values = MasterTable.objects.filter(type=location_type).values_list('value', flat=True)
    #     if not all(item in valid_values for item in value):
    #         raise serializers.ValidationError(f"Invalid location(s). Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Language(self, value):
    #     language_type = CommonMatchingTable.objects.get(type="language")
    #     valid_values = MasterTable.objects.filter(type=language_type).values_list('value', flat=True)
    #     if not all(item in valid_values for item in value):
    #         raise serializers.ValidationError(f"Invalid language(s). Valid values are: {', '.join(valid_values)}")
    #     return value

    # def validate_Marital_status(self, value):
    #     marital_status_type = CommonMatchingTable.objects.get(type="marital_status")
    #     valid_values = MasterTable.objects.filter(type=marital_status_type).values_list('value', flat=True)
    #     if value not in valid_values:
    #         raise serializers.ValidationError(f"Invalid marital status. Valid values are: {', '.join(valid_values)}")
    #     return value
