from django.shortcuts import render

def submit(request):
    return render(request, 'result.html')

def show_exam_result(request):
    return render(request, 'result.html')