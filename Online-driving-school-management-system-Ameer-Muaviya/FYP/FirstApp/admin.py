from django.contrib import admin
from FirstApp.models import Attendence, Links, Notifications, Students,Programs,Assignments,SubmitAssignment,ManageVehicles,Instructor

# Register your models here.
admin.site.register(Students)
admin.site.register(Attendence)
admin.site.register(Programs) 
admin.site.register(Notifications) 
admin.site.register(Assignments) 
admin.site.register(SubmitAssignment)  
admin.site.register(ManageVehicles)  
admin.site.register(Instructor)  
admin.site.register(Links)  
 
