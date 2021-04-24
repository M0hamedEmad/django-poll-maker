from django.forms import ModelForm
from .models import Poll, Option

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['question'].widget.attrs = {
            'class':"form-control mb-3",
            'rows':"3",
            'placeholder':"Type Your Answer Here"
            }

        self.fields['question'].label = ''

class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = ['option',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['option'].widget.attrs = {
            'class':"form-control mb-3",
            'placeholder':"Write your option here"
        }

        self.fields['option'].label = ''