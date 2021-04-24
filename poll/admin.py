from django.contrib import admin
from .models import Option, Poll


admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "Poll Admin"

class ChoiceInline(admin.TabularInline):
    model = Option
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
    ('author', {'fields': ['author']})
    ]
    inlines = [ChoiceInline,]



admin.site.register(Poll, QuestionAdmin)

