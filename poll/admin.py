from django.contrib import admin
from .models import Poll, Answer, Vote, PollCode


admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "Poll Admin"

class ChoiceInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question', 'image']}),
    ('settings', {'fields': [
        'title',
        'summary',
        'author',
        'hide_results',
        'multiple_answers',
        'views',
        'start_at',
        'end_at',
        'slug',
        'status',
        ]})
    ]
    inlines = [ChoiceInline,]


admin.site.register(Poll, QuestionAdmin)
admin.site.register(PollCode)
admin.site.register(Vote)



