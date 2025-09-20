from django import forms
from defects.models import DefectDetails

class DefectEditForm(forms.ModelForm):
    defect_id = forms.CharField(max_length=50, disabled=True)
    defect_name = forms.CharField(max_length=50, disabled=True)

    class Meta:
        model = DefectDetails
        fields = ['defect_id', 'defect_name', 'assigned_by', 'assigned_to', 'description', 'defect_status', 'priority']


class AddDefect(forms.ModelForm):
    class Meta:
        model = DefectDetails
        fields = '__all__'

class FilterDevelopers(forms.ModelForm):
    class Meta:
        model = DefectDetails
        fields = ['assigned_to']