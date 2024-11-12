from django.urls import path
from .views import SkillListCreateView, SkillDetailView

urlpatterns = [
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    # Define similar endpoints for Experience, JobDone, PastCompany, and Recommendation models
]
