from django.shortcuts import render, redirect
from .models import Poll


# show all polls
def home(request):
    polls = Poll.objects.all()
    context = {'title': 'home | PollApp', 'polls': polls}
    return render( request, 'poll/home.html', context )


# vote a poll
def vote(request, poll_id):
    poll = Poll.objects.filter( id=poll_id ).first()
    print( request.method )
    if request.method == 'POST':
        print( request.POST )
        form_data = request.POST
        user_answer = form_data.get( f'{poll.question}' )

        if user_answer == poll.option_1:
            poll.option_1_counter += 1

        elif user_answer == poll.option_2:
            poll.option_2_counter += 1

        elif user_answer == poll.option_3:
            poll.option_3_counter += 1

        poll.save()
        return redirect( 'poll:result', poll.id )
    context = {'title': 'vote | PollApp', 'poll': poll}
    return render( request, 'poll/vote.html', context )


#  show the result of a poll
def result(request, poll_id):
    poll = Poll.objects.filter( id=poll_id ).first()
    context = {'title': 'result | PollApp', 'poll': poll}
    return render( request, 'poll/result.html', context )


# create new poll
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
