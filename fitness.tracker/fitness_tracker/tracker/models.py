from django.db import models
from django.contrib.auth.models import User

# --- FootballMatch Model ---
class FootballMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField(help_text="Duration in HH:MM:SS")
    goals = models.PositiveIntegerField(default=0)
    performance_rating = models.PositiveIntegerField(default=0, help_text="Rate 1–10")

    def __str__(self):
        return f"⚽ {self.user.username}'s Match - {self.date} ({self.performance_rating}/10)"
    
    class Meta:
        verbose_name_plural = "Football Matches"


# --- WorkoutSession Model ---
class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    workout_type = models.CharField(max_length=100, help_text="e.g., Strength, Cardio, HIIT")
    exercise = models.CharField(max_length=100)
    
    # ADDED: Fields to match your WorkoutSessionForm
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Weight used (kg or lbs)")
    reps = models.PositiveIntegerField(null=True, blank=True)
    personal_record = models.BooleanField(default=False)
    
    def __str__(self):
        return f"💪 {self.user.username}'s Workout - {self.exercise} on {self.date}"

    class Meta:
        verbose_name_plural = "Workout Sessions"
