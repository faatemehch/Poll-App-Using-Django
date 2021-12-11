from django.shortcuts import render


def home(request):
    context = {'title': 'home | PollApp'}
    return render( request, 'poll/home.html', context )


def vote(request):
    context = {'title': 'vote | PollApp'}
    return render( request, 'poll/vote.html', context )


def result(request):
    context = {'title': 'result | PollApp'}
    return render( request, 'poll/result.html', context )


def create(request):
    context = {'title': 'create | PollApp'}
    return render( request, 'poll/create.html', context )


