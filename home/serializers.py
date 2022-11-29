from rest_framework import serializers
from home.models import FormBuilder

class FormBuilderSerializer(serializers.ModelSerializer):
  class Meta:
    model=FormBuilder
    fields = ['form_id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']
