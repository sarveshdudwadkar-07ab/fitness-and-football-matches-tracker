from django import forms
from .models import FootballMatch, WorkoutSession

class FootballMatchForm(forms.ModelForm):
    class Meta:
        model = FootballMatch
        fields = ['date', 'duration', 'goals', 'performance_rating']

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        # Fields now match the corrected models.py
        fields = ['date', 'workout_type', 'exercise', 'weight', 'reps', 'personal_record']
