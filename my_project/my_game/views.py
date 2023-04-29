from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import SavedGameData



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('game_view')
    else:
        form = UserCreationForm()
    return render(request, 'my_game/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserCreationForm()
    return render(request,'my_game/login.html',{'form': form})

@login_required
def game_view(request):
    return render(request, 'my_game/index.html')

from django.http import JsonResponse
from .models import SavedGameData

@login_required
def save_game_data(request):
    if request.method == 'POST':
        data = request.POST['game_data']
        saved_game_data, created = SavedGameData.objects.get_or_create(user=request.user)
        saved_game_data.game_data = data
        saved_game_data.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def load_game_data(request):
    try:
        saved_game_data = SavedGameData.objects.get(user=request.user)
        return JsonResponse({'game_data': saved_game_data.game_data})
    except SavedGameData.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'No saved game data found'})
