from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def submit_contact_form(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Process the data (you can save it to a database or send it via email)
        # For demonstration purposes, let's just print the data
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Optionally, you can redirect the user to a thank you page
        return render(request, 'myapp/thanks.html',)
    else:
        # Handle GET requests or other methods (if necessary)
        return HttpResponse("Invalid request method.")

