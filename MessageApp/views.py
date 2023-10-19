from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import MyMessage
from .forms import MessageForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def display(request):
    return render(request, "display.html")

@login_required
def control_panel(request):
    form = MessageForm()
    return render(request, 'control_panel.html', {'form': form})

@login_required
def update_message(request):
    user = request.user
    last_message = MyMessage.objects.filter(user=user).last()

    if request.method == 'POST':
        form = MessageForm(request.POST, instance=last_message)
        if form.is_valid():
            message_instance = form.save(commit=False)
            message_instance.user = user
            message_instance.save()
            return JsonResponse({'status': 'success'})
    else:
        form = MessageForm(instance=last_message)

    return render(request, 'control_panel.html', {'form': form})

@login_required
def get_message(request):
    user = request.user
    last_message = MyMessage.objects.filter(user=user).last()

    if last_message:
        message = last_message.message
        background_color = last_message.background_color
        status = last_message.status
        background_image = last_message.background_image
    else:
        message = ''
        background_color = 'white'
        status = 'unknown'
        background_image = ''

    return JsonResponse({'message': message, 'background_color': background_color, 'status': status, 'background_image': background_image})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('control_panel')  # Redirect to a home page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})