from django.contrib import admin
from .models import Question, Choice
from django.utils.translation import gettext_lazy as _



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
                ('問題',{'fields': ['question_text']}),
                ('日期資訊', {'fields': ['pub_date']}),
            ]
    inlines = [ChoiceInline]

    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.site_header = '測試後台'