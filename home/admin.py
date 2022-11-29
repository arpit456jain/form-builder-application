from django.contrib import admin
from home.models import FormBuilder

@admin.register(FormBuilder)
class FormBuilderModel(admin.ModelAdmin):
  list_display = ['form_id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']