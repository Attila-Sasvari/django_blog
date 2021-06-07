from django.contrib import admin
from .models import FileUpload

# Register your models here.
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(FileUpload, FileUploadAdmin)