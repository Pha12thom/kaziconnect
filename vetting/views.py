from django.contrib.auth import get_user_model  # Import get_user_model dynamically
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Skill, Experience, Recommendation
from .serializers import SkillSerializer, ExperienceSerializer, RecommendationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# View to handle multiple data creation (Skills, Experience, Recommendations)
class VettingDataView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        skills_data = request.data.get('skills', [])
        experience_data = request.data.get('experience', [])
        recommendations_data = request.data.get('recommendations', [])
        
        # Create Skills
        for skill in skills_data:
            Skill.objects.create(user=request.user, **skill)

        # Create Experience
        for exp in experience_data:
            Experience.objects.create(user=request.user, **exp)
        
        # Create Recommendations
        for rec in recommendations_data:
            client_id = rec.get('client')  # Extract client ID
            service_provider_id = rec.get('service_provider')  # Extract service provider ID

            try:
                # Dynamically get the actual user model
                User = get_user_model()
                
                # Fetch the actual User objects (CustomUser instances)
                client = User.objects.get(id=client_id)
                service_provider = User.objects.get(id=service_provider_id)

                # Create the recommendation object
                Recommendation.objects.create(client=client, service_provider=service_provider, text=rec.get('recommendation_text'))
            except User.DoesNotExist:
                return Response({"error": "Invalid user ID for client or service provider"}, status=400)
        
        return Response({"message": "Vetting data added successfully!"})

# Retrieve and update a single skill
class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Skill.objects.get(id=self.kwargs['id'], user=self.request.user)

# Retrieve and update a single experience entry
class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Experience.objects.get(id=self.kwargs['id'], user=self.request.user)

# Retrieve and update a single recommendation
class RecommendationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Recommendation.objects.get(id=self.kwargs['id'], user=self.request.user)
