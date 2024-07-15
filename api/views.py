from django.shortcuts import render, redirect

# Home page view
def home(request):
    # Assuming you have a template named 'home.html' in your templates directory
    return render(request, 'home.html')

def about(request):
    # Renders the about page
    return render(request, 'about.html')

# Contact page view
def contact(request):
    # Renders the contact page
    return render(request, 'contact.html')
    

