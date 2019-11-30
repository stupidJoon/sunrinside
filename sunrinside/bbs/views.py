from django.shortcuts import render

def board(request):
  if request.method == "GET":
    return render(request, 'index.html')