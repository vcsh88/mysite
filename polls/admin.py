from django.contrib import admin

# Register your models here.
from .models import Question, Choice
#admin.site.register(Question)
#admin.site.register(Choice)

#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

class ChoiceInline(admin.TabularInline): #Chg from StackedInline
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
         'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]
  

admin.site.register(Question, QuestionAdmin)