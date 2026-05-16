from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def stranger_dashboard(request):
    return render(request, 'stranger_practice/dashboard.html')
