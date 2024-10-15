from django.http import HttpResponse
from django.shortcuts import redirect

def hello(request) :
    return redirect('accounts/register/')  # Redirect to a specific URL