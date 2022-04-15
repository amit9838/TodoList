from django.contrib import admin
from home.models import Task
# Register your models here.
class Admin1(admin.ModelAdmin):
    list_display =('taskName','taskDesc','time')
    


admin.site.register(Task,Admin1)
