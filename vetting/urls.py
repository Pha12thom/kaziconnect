# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.VettingDataView.as_view(), name='vetting-data'),  # POST and GET
    path('skills/<int:id>/', views.SkillDetailView.as_view(), name='skill-detail'),  # PUT/PATCH/DELETE
    path('experience/<int:id>/', views.ExperienceDetailView.as_view(), name='experience-detail'),  # PUT/PATCH/DELETE
    path('recommendations/<int:id>/', views.RecommendationDetailView.as_view(), name='recommendation-detail'),  # PUT/PATCH/DELETE
]
