from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def not_found_404(request, exception):
    #tratar exceptions  
    return render(request, 'not-found.html', context=exception, status=404)