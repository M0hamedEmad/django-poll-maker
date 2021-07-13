from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView, View
from poll.models import Poll
from .forms import UserProfileForm

class PollListView(LoginRequiredMixin, ListView):
    model = Poll
    template_name = 'dashboard/polls_list.html'
    context_object_name = 'polls'
    
    def get_queryset(self):
        return self.request.user.poll_set.all()

class ProfileView(LoginRequiredMixin, View):
    template_name = 'dashboard/profile.html'
    
    def get(self, request, *args, **kwargs):
        form = UserProfileForm(instance=self.request.user)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST ,instance=self.request.user)
        if form.is_valid():
            form.save()
        form = UserProfileForm(instance=self.request.user)
        return self.get(request, *args, **kwargs)
     
     