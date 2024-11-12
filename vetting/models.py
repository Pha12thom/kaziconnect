from django.db import models
from django.conf import settings

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in months")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.job_title} at {self.company}"


class JobDone(models.Model):
    service_provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs_done')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_completed = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.service_provider.username}"

class PastCompany(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='past_companies')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Recommendation(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='given_recommendations')
    service_provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_recommendations')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation from {self.client.username} to {self.service_provider.username}"
