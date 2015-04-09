from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignupForm
# Create your views here.


def home(request):
    form = SignupForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    context = {}
    template = 'signup.html'
    return render_to_response(template, locals(),
                              context_instance=RequestContext(request))
