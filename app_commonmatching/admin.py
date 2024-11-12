from django.contrib import admin
from .models import CommonMatchingTable,MasterTable
# Register your models here.
admin.site.register(CommonMatchingTable)
admin.site.register(MasterTable)