from django.contrib import admin
from quizzes.models import Question, Quiz, MultipleChoice, ResultOption

class MultipleChoiceInline(admin.TabularInline):
    model = MultipleChoice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ MultipleChoiceInline, ]

class ResultOptionInline(admin.StackedInline):
    model = ResultOption

class QuizAdmin(admin.ModelAdmin):
    inlines = [ ResultOptionInline, ]


    #fieldsets = (
    #    (None, {
    #        'fields': ('answer')
    #    }),
    #    ('Advanced options', {
    #        'classes': ('collapse',),
    #        'fields': ('feedback', 'is_correct')
    #    }),
    #)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
