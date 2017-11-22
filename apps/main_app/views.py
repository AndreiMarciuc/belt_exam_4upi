from django.shortcuts import render,redirect
from .models import Poke
from ..login_app.models import User
from django.contrib import messages
from django.utils import timezone



# Create your views here.
def dashboard(request):
    if "id" in request.session:
        users = User.objects.all().exclude(id=request.session['id'])
        pokes = Poke.objects.all()
        user_poke_count = Poke.objects.all().filter(poked=request.session['id'])
        list_of_users = Poke.objects.filter(poked=request.session['id']).exclude(id=request.session['id'])
        user = User.objects.get(id=request.session['id'])
        current_user = User.objects.get(id=request.session['id'])
        context = {
            'current_user': current_user,
            'user': user,
            'users': users,
            'pokes': pokes,
            'user_poke_count': user_poke_count,
            'list_of_users': list_of_users }
        return render(request, 'main_app/index.html', context)
    else:
        del request.session
        return redirect('/main/')

def poke(request, id):
    poker = User.objects.get(id=request.session['id'])
    poked = User.objects.get(id=id)
    poke = Poke()
    poke.poker = poker
    poke.poked = poked
    poke.counter+=1
    poke.save()
    return redirect('/main/')