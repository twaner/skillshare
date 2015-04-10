from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import SignupForm
# Create your views here.


def home(request):
    form = SignupForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'We will be in touch')
        return HttpResponseRedirect('/thank-you/')
    
    context = {}
    template = 'signup.html'
    return render_to_response(template, locals(),
                              context_instance=RequestContext(request))
