from django.shortcuts import render, redirect

from gamesplay_app.core.forms import ProfileForm, GameForm, DeleteGameForm, EditProfileForm, DeleteProfileForm
from gamesplay_app.core.models import Profile, GameModel


def get_profile():
    return Profile.objects.all()


def show_index(request):
    profile = get_profile()
    context = {
        "profile": profile
    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show index')
    else:
        profile_form = ProfileForm()

    context = {
        'profile_form': profile_form
    }
    return render(request, 'create-profile.html', context)


def show_dashboard(request):
    games = GameModel.objects.all()
    context = {
        'games': games
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == "POST":
        game_form = GameForm(request.POST)
        if game_form.is_valid():
            game_form.save()
            return redirect('show dashboard')
    else:
        game_form = GameForm()
    context = {
        'game_form': game_form
    }
    return render(request, 'create-game.html', context)


def show_game(request, pk):
    game = GameModel.objects.get(pk=pk)

    context = {
        'game': game
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = GameModel.objects.get(pk=pk)
    if request.method == "POST":
        game_form = GameForm(request.POST, request.FILES, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('show dashboard')
    else:
        game_form = GameForm(instance=game)

    context = {
        'game_form': game_form,
        'id': game.id
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = GameModel.objects.get(pk=pk)
    if request.method == "POST":
        game_form = DeleteGameForm(request.POST, request.FILES, instance=game)
        if game_form.is_valid():
            game_form.save()
            return redirect('show dashboard')
    else:
        game_form = DeleteGameForm(instance=game)

    context = {
        'game_form': game_form,
        'id': game.id
    }
    return render(request, 'delete-game.html', context)


def show_profile(request):
    profile = get_profile()[0]
    games = GameModel.objects.all()
    if games:
        avg_rating = f'{sum([game.rating for game in games]) / len(games):.1f}'
    else:
        avg_rating = '0.0'
    context = {
        'profile': profile,
        'games': len(games),
        'avg_rating': avg_rating
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()[0]
    if request.method == "POST":
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show profile')
    else:
        profile_form = EditProfileForm(instance=profile)
    context = {
        'profile_form': profile_form
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()[0]
    if request.method == "POST":
        profile_form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show index')
    else:
        profile_form = DeleteProfileForm(instance=profile)

    context = {
        'profile_form': profile_form
    }
    return render(request, 'delete-profile.html', context)
