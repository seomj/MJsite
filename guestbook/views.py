
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from guestbook.models import Guestbook


@login_required
def guest_list(request):
    guestbooklist = Guestbook.objects.all().order_by('-reg_date')
    data = {'guestbooklist': guestbooklist}
    return render(request, 'guestbook/list.html', data)


@login_required
def guest_write(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.contents = request.POST['contents']
    guestbook.save()

    return HttpResponseRedirect('list')


@login_required
def deleteform(request, id):
    guestbook = Guestbook.objects.get(id=id)
    if request.method == "POST":
        password = request.POST['password']
        if password == guestbook.password:
            guestbook.delete()
            return redirect('/guestbook/list')
    return render(request, 'guestbook/deleteform.html', {'id': guestbook})