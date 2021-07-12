from django.shortcuts import reverse, get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView, TemplateView, DetailView, DetailView, FormView, View
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.timezone import now
from .models import Poll, Answer, Vote
from .forms import PollForm, AnswerForm, PollConfigForm, AnswerFormSet
from requests import get

def get_client_ip():
    return get('https://api.ipify.org').text

class HomeView(TemplateView):
    template_name = 'poll/home.html'
    
    def get_context_data(self, **kwargs):
        """ Override get_context method to add answer form set and poll config form

        Returns:
            context with answer_form
        """
        context = super().get_context_data(**kwargs)
        context['form'] = PollForm(self.request.POST or None)
        context['answer_form'] = AnswerFormSet(self.request.POST or None)
        context['poll_form'] = PollConfigForm(self.request.POST or None)
        
        return context

class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/create_poll.html'

    def get_context_data(self, **kwargs):
        """ Override get_context method to add answer form set and poll config form

        Returns:
            context with answer_form
        """
        context = super().get_context_data(**kwargs)
        context['answer_form'] = AnswerFormSet(self.request.POST, files=self.request.FILES or None)
        context['poll_form'] = PollConfigForm(self.request.POST or None)
        
        return context

    def form_valid(self, form):
        """ override this mehod to check if form set if vaild save question and answers

        Returns:
            [type]: [description]
        """
        answer_from_set = self.get_context_data().get('answer_form')
        poll_form = self.get_context_data().get('poll_form')
        
        if answer_from_set.is_valid() and poll_form.is_valid():
            self.object = form.save(commit=False)
            self.object.author = self.request.user if self.request.user.is_authenticated else None
            self.object.save()
            
            poll_form = PollConfigForm(self.request.POST, instance=self.object)
            poll_form.save()
            
            answer_from_set.instance = self.object
            answer_from_set.save()
            messages.success(self.request, f'The question "{self.object.question}" has been created successfully')
            return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('create_poll')
        
class PollDeleteView(UserPassesTestMixin, DeleteView):
    model = Poll
    template_name = 'poll/delete_poll.html'
    success_url = '/'
    
    def test_func(self):
        poll = self.get_object()

        try:
            return True if poll.author == self.request.user or poll.pollcode.code == self.request.GET.get('code') else False
        except:
            return False
       
class PollDetailView(DetailView):
    model = Poll
    template_name = 'poll/voting.html'
    context_template_name = 'poll'
    
    def get(self, request, *args, **kwargs):
        poll = self.get_object()
        if poll.end_at and poll.end_at < now():
            messages.info(request, "this poll is end")
            if not poll.hide_results:
                return redirect('result', slug=poll.slug)
        
        return super().get(request, *args, **kwargs)
 
 
    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        poll = self.get_object()
        
        context['poll_is_end'] = True if poll.end_at and poll.end_at < now() else False
        
        return context

class VoteCreate(View):
    def post(self, request, *args, **kwargs):
        poll_id = int(request.POST.get('poll_id'))
        answers_id = request.POST.getlist('answer')
        if poll_id and answers_id:
            poll = Poll.objects.filter(id=poll_id)
            
            answers = Answer.objects.filter(id__in=answers_id)
            for answer in answers:
                if answer.poll_question.id == poll_id:
                    vote = Vote()
                    vote.answer = answer
                    vote.user = request.user if request.user.is_authenticated else None
                    vote.ip = get_client_ip()
                    vote.save()
        
        return redirect('result', slug=poll.first().slug)
    
class ResultView(UserPassesTestMixin, DeleteView):
    model = Poll
    template_name = 'poll/result.html'
    context_template_name = 'poll'
    
    def test_func(self):
        poll = self.get_object()

        if not poll.hide_results or poll.author == self.request.user:
            return True
        
        try:
            return poll.pollcode.code == self.request.GET.get('code')
        except:
            return False
        
    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        total_votes = 0
            
        for answer in self.get_object().answer.all():
            total_votes += answer.get_valid_votes()
        
        context['total_votes'] = total_votes
        
        return context
    
def resultDate(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    answers = poll.answer.all()

    result_date = []

    for answer in answers:
        result_date.append({answer.answer:answer.get_valid_votes()})

    return JsonResponse(result_date, safe=False)

    PollCreateView
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

