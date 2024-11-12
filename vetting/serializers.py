from rest_framework import serializers
from .models import Skill, Experience, JobDone, PastCompany, Recommendation

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'company', 'duration', 'description']

class JobDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDone
        fields = ['id', 'title', 'description', 'date_completed']

class PastCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PastCompany
        fields = ['id', 'name', 'position', 'start_date', 'end_date']

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['id', 'client', 'service_provider', 'text', 'created_at']
