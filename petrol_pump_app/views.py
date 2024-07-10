from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PetrolPumpRegistrationForm

@login_required
def petrol_pump_dashboard(request):
    return render(request, 'petrol_pump_dashboard.html')

def petrol_pump_register(request):
    if request.method == 'POST':
        form = PetrolPumpRegistrationForm(request.POST)
        if form.is_valid():
            petrol_pump = form.save(commit=False)
            petrol_pump.user = request.user
            petrol_pump.save()
            return redirect('petrol_pump_dashboard')
    else:
        form = PetrolPumpRegistrationForm()
    return render(request, 'petrol_pump_register.html', {'form': form})
