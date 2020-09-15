from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def sudoku(request):
    return render(request, 'sudoku.html')


