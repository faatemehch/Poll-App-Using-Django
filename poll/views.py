from django.shortcuts import render, redirect
from .models import Poll


def home(request):
    polls = Poll.objects.all()
    context = {'title': 'home | PollApp', 'polls': polls}
    return render( request, 'poll/home.html', context )


def vote(request):
    context = {'title': 'vote | PollApp'}
    return render( request, 'poll/vote.html', context )


def result(request, poll_id):
    poll = Poll.objects.filter( id=poll_id ).first()
    context = {'title': 'result | PollApp', 'poll': poll}
    return render( request, 'poll/result.html', context )


def create(request):
    if request.method == 'POST':
        form_data = request.POST
        question = form_data.get( 'question' )
        opt_1 = form_data.get( 'opt1' )
        opt_2 = form_data.get( 'opt2' )
        opt_3 = form_data.get( 'opt3' )
        Poll.objects.create( question=question, option_1=opt_1, option_2=opt_2, option_3=opt_3 )
        return redirect( 'poll:create' )
    context = {'title': 'create | PollApp'}
    return render( request, 'poll/create.html', context )
