from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def teacher_view(request):
    return render(request, 'avatar/teacher.html')
