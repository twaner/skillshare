from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import SignupForm
# Create your views here.


def home(request):
    template = 'signup.html'
    return render_to_response(template, locals(),
                              context_instance=RequestContext(request))


def thankyou(request):
    form = SignupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for your order. We will be in touch')
        return HttpResponseRedirect('/thank-you/')

    context = {}

    template = 'thankyou.html'
    return render_to_response(template, locals(),
                              context_instance=RequestContext(request))


def aboutus(request):
    template = 'aboutus.html'
    return render_to_response(template, locals(),
                              context_instance=RequestContext(request))
