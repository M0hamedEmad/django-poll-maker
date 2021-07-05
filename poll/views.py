# from django.shortcuts import render, get_object_or_404  ,redirect, Http404
# from django.forms import inlineformset_factory
# from django.contrib import messages
# from django.http import JsonResponse
# from .models import Poll, Option
# from .forms import PollForm, OptionForm

# def createPoll(request):
#     """Create A poll """
#     # number of options or 5 options
#     number_of_options = request.GET.get('number_of_options') or 5
#     # max number of options is 30
#     number_of_options = int(number_of_options) if int(number_of_options) <= 30 else 5

#     OptionFormSet = inlineformset_factory(Poll, Option, fields=('option',), can_delete=False, form=OptionForm, extra= number_of_options)
   

#     if request.method == 'POST':
#         poll_form = PollForm(request.POST)
#         if poll_form.is_valid():
#             poll = poll_form.save(commit=False)
#             if request.user.is_authenticated:
#                 poll.author = request.user 
#             poll.save()

#         formset = OptionFormSet(request.POST, instance=poll)
#         if formset.is_valid():
#             formset.save()
#             return redirect('vote', poll.pk)
        
#     poll_form = PollForm()
#     formset = OptionFormSet()

#     context = {
#         'poll_form':poll_form,
#         'option_form':formset,
#         'nop':number_of_options,
#     }
#     return render(request, 'poll/create_poll.html', context)

# def deletePoll(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     if request.user != poll.author:
#         raise Http404
        
#     if request.method == 'POST':
#         poll.delete()
#         return redirect('/')

#     context = {
#         'poll':poll,
#     }
#     return render(request, 'poll/delete_poll.html', context)

# def vote(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     if request.method == 'POST':
#         if 'option' in request.POST:
#             option = request.POST.get('option')
#             options = poll.options.filter(option=option)
#             if len(options) > 0:
#                 op = options.first()
#                 op.number_of_vote += 1
#                 op.save()
#                 return redirect('result', pk)
#             else:
#                 messages.warning(request, 'Incorrect chose! please try again')
#         else:
#             messages.warning(request, 'You must choose an option!')

#     context = {
#         'poll':poll
#     }
#     return render(request, 'poll/voting.html', context)

# def result(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     total_votes = 0

#     for option in poll.options.all():
#         total_votes += option.number_of_vote

#     context = {
#         'poll':poll,
#         'total_votes':total_votes,
#     }
#     return render(request, 'poll/result.html', context)

# def resultDate(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     options = poll.options.all()

#     result_date = []

#     for option in options:
#         result_date.append({option.option:option.number_of_vote})

#     return JsonResponse(result_date, safe=False)