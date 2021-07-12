from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify
from unidecode import unidecode

result_choices = [
    (True, 'Hide Results'),
    (False, 'Publish Results')
]

multiple_answers_choices = [
    (True, 'Select Multiple Answers'),
    (False, 'Select One Answer')
]

stats_choices = [
    (True, 'Active'),
    (False, 'Inactive')
]


class Poll(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(max_length=500)
    title = models.CharField(max_length=150, null=True, blank=True)
    summary = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='poll_images')
    hide_results = models.BooleanField(default=False, choices=result_choices)
    multiple_answers = models.BooleanField(default=False, choices=multiple_answers_choices)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    start_at = models.DateTimeField(default=now)
    end_at = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True, choices=stats_choices)

    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.question}-{self.id}")
        return super().save(*args, **kwargs)
        
        
class PollCode(models.Model):
    code = models.CharField(max_length=60)
    poll = models.OneToOneField(Poll, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.poll.question   

class Answer(models.Model):
    poll_question = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='answer')
    answer = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='answers_images')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.answer
    
    def get_valid_votes(self):
        return self.votes.all().count()
    
class Vote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    
    def __str__(self):
        return self.answer.answer