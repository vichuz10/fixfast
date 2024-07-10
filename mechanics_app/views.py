from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MechanicRegistrationForm

@login_required
def mechanic_dashboard(request):
    return render(request, 'mechanic_dashboard.html')

def mechanic_register(request):
    if request.method == 'POST':
        form = MechanicRegistrationForm(request.POST)
        if form.is_valid():
            mechanic = form.save(commit=False)
            mechanic.user = request.user
            mechanic.save()
            return redirect('mechanic_dashboard')
    else:
        form = MechanicRegistrationForm()
    return render(request, 'mechanic_register.html', {'form': form})
