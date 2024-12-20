from django.shortcuts import render

# Create your views here.
def faculty(request):
    return render(request,'faculty.html')

def student(request):
    return render(request,'student.html')