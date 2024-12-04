from django.db import models
 
class CommonMatchingTable(models.Model):

    TYPE_CHOICES = [
        ('gender', 'Gender'),
        
        ('caste', 'Caste'),

        ('religion', 'Religion'),

        ('profession', 'Profession'),

        ('education', 'Education'),

        ('location', 'Location'),

        ('language','Language'),

        ('marital_status','Marital_status')

    ] 
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.type


class MasterTable(models.Model):
    type = models.ForeignKey(CommonMatchingTable, on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=50, unique=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def generate_code(self):
        # Prefix mapping based on type
        prefix = {
            'gender': 'GE',
            'caste': 'CA',
            'religion': 'RE',
            'profession': 'PR',
            'education': 'ED',
            'location': 'LO',
            'language': 'LA',
            'marital_status': 'MS'
        }.get(self.type.type, 'XX')  # If the type isn't found, it defaults to 'XX'.

        # Get the last entry to determine the new number for the code
        last_entry = MasterTable.objects.filter(type=self.type).order_by('-id').first()
        last_number = 0
        if last_entry and last_entry.code:
            try:
                last_number = int(last_entry.code[2:])  # Extract the numeric part of the code
            except ValueError:
                last_number = 0  # In case the previous code does not follow the expected pattern

        new_number = last_number + 1  # Increment the number
        code = f"{prefix}{new_number:03d}"  # Format the code with leading zeros

        return code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()  # Generate the code if it doesn't exist
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type.type} - {self.value} - {self.code}"