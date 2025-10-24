from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Removed 'logout' from imports
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

from .forms import FootballMatchForm, WorkoutSessionForm
from .models import FootballMatch, WorkoutSession

@login_required
def dashboard(request):
    # Order by date descending for better visualization
    matches = FootballMatch.objects.filter(user=request.user).order_by('-date')
    workouts = WorkoutSession.objects.filter(user=request.user).order_by('-date')

    context = {
        'matches': matches,
        'workouts': workouts,
    }
    return render(request, 'tracker/dashboard.html', context)


@login_required
def add_match(request):
    if request.method == 'POST':
        form = FootballMatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.user = request.user
            match.save()
            messages.success(request, "Football match recorded successfully!")
            return redirect('dashboard')
    else:
        form = FootballMatchForm()
    return render(request, 'tracker/add_match.html', {'form': form})


@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, "Workout session recorded successfully!")
            return redirect('dashboard')
    else:
        form = WorkoutSessionForm()
    return render(request, 'tracker/add_workout.html', {'form': form})


# --- Authentication Views ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}. Welcome!")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'tracker/register.html', {'form': form}) 

# The user_logout function is intentionally removed to avoid conflict.