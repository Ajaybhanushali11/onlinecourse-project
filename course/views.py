from django.shortcuts import render

# Create your views here.

def submit(request):
    return render(request, 'result.html')

def show_exam_result(request):
    return render(request, 'result.html')