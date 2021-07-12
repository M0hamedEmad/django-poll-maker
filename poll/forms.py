from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import Poll, Answer

class PollConfigForm(ModelForm):
    class Meta:
        model = Poll
        fields = [
            'title',
            'summary',
            'hide_results',
            'multiple_answers',
            'start_at',
            'end_at',
            'status',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['title'].widget.attrs = {
            'placeholder':"Title"
            }
        
        self.fields['summary'].widget.attrs = {
            'placeholder':"summary"
            }
        
        self.fields['title'].label = ''        
        self.fields['summary'].label = ''
        self.fields['hide_results'].label = 'Published result or not'
        self.fields['multiple_answers'].label = 'Select multiple answers'
        
        
class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = [
            'question',
            'image',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['question'].widget.attrs = {
            'class':"form-control mb-3",
            'rows':"3",
            'placeholder':"Type Your Question Here"
            }
        
        self.fields['question'].label = ''
        self.fields['image'].label = 'image'
        

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['answer'].widget.attrs = {
            'class':"form-control mb-3",
            'placeholder':"Write your option here"
        }

        self.fields['image'].label = 'image'
        self.fields['answer'].label = ''
        
        
AnswerFormSet = inlineformset_factory(Poll, Answer, can_delete=False, form=AnswerForm, max_num=40, extra=5)

