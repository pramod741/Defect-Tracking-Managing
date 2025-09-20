from rest_framework import serializers
from .models import Developers, Testers, DefectDetails, Defect_Screen_Shots
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DeveloperSerializer(serializers.ModelSerializer):
    dev_name = UserSerializer(read_only=True)
    dev_name_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='dev_name', write_only=True
    )

    class Meta:
        model = Developers
        fields = ['id', 'dev_name', 'dev_name_id', 'designation', 'experience']

class TesterSerializer(serializers.ModelSerializer):
    tester_name = UserSerializer(read_only=True)
    tester_name_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='tester_name', write_only=True
    )

    class Meta:
        model = Testers
        fields = ['id', 'tester_name', 'tester_name_id', 'designation', 'experience', 'is_admin']

class DefectSerializer(serializers.ModelSerializer):
    assigned_by = TesterSerializer(read_only=True)
    assigned_by_id = serializers.PrimaryKeyRelatedField(
        queryset=Testers.objects.all(), source='assigned_by', write_only=True
    )
    assigned_to = DeveloperSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=Developers.objects.all(), source='assigned_to', write_only=True
    )

    class Meta:
        model = DefectDetails
        fields = [
            'id', 'defect_id', 'defect_name', 'description',
            'defect_status', 'priority', 'assigned_date',
            'assigned_by', 'assigned_by_id',
            'assigned_to', 'assigned_to_id'
        ]

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect_Screen_Shots
        fields = ['id', 'defect', 'defect_img']
