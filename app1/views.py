from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
# error -from django.core.urlresolvers import reverse
#Django 2.0 removes the django.core.urlresolvers module, which was moved to django.urls in version 1.10. You should change any import to use django.urls instead, like this:

from django.urls import reverse

# from .models import Topic,Entry
# from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from .forms import TicketsForm
from .models import Tickets

def index(request):
    """homepage"""
    return render(request,'app1/index.html')


@login_required  
def bookTicket(request):
    if request.method != 'POST':
        form = TicketsForm()
    else:
        form =TicketsForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            #connectin to new user
            new_booking.owner=request.user
            new_booking.save()
            return HttpResponseRedirect(reverse('app1:payment'))



    city_list=['patna','kolkata','Nalanda','Banaras','Delhi','Lucknow','Patiala','Chandigarh']


    context={'form':form,'city_list':city_list}
    return render(request,'app1/booking.html',context)

@login_required
def payment(request):
    bill=Tickets.objects.last()
    context = {'bill':bill}
    return render(request, 'app1/payment.html',context)







