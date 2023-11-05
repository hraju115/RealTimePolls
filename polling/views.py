from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages

from .models import Poll, Choice
from .forms import VoteForm

def index(request):
    """
    Render a list of available polls.

    This view retrieves all available polls from the database and renders
    the 'index.html' template, displaying the list of polls.

    :param request: HTTP request object
    :return: Rendered HTML template with poll list
    """
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_polls': latest_polls}
    return render(request, 'index.html', context)

def detail(request, poll_id):
    """
    Render the details of a specific poll.

    This view retrieves a specific poll from the database using its ID and
    renders the 'detail.html' template.

    :param request: HTTP request object
    :param poll_id: ID of the poll to display
    :return: Rendered HTML template with poll details and real-time results
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    total_votes = poll.choice_set.aggregate(Sum('votes'))['votes__sum']
    
    form = VoteForm(poll_id)

    return render(request, 'detail.html', {'poll': poll, 'total_votes': total_votes, 'form': form, 'poll_id': poll_id})
