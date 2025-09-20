from django.contrib import admin
from .models import DefectDetails, Developers, Testers, Defect_Screen_Shots

# Register your models here.
admin.site.register(DefectDetails)
admin.site.register(Developers)
admin.site.register(Testers)
admin.site.register(Defect_Screen_Shots)