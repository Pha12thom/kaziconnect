# serializers.py

from rest_framework import serializers
from .models import Skill, Experience, Recommendation

# BaseListSerializer for handling lists of data
class BaseListSerializer(serializers.ListSerializer):
    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError("Expected a list of items.")
        return super().to_internal_value(data)

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        list_serializer_class = BaseListSerializer

# Experience Serializer
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'duration', 'description']
        list_serializer_class = BaseListSerializer


# Recommendation Serializer (for clients recommending service providers)
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['client', 'service_provider', 'recommendation_text']
        list_serializer_class = BaseListSerializer

# Combined serializer to handle all input types
class VettingDataSerializer(serializers.Serializer):
    skills = SkillSerializer(many=True)
    experience = ExperienceSerializer(many=True)
    recommendations = RecommendationSerializer(many=True)

    # Validation to ensure that all data is structured correctly
    def validate(self, data):
        skills = data.get('skills', [])
        experience = data.get('experience', [])
        recommendations = data.get('recommendations', [])
        
        if not skills or not experience or not recommendations:
            raise serializers.ValidationError("All sections (skills, experience, recommendations) must be provided.")
        return data
