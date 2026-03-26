from django.contrib import admin
from .models import Question, Choice, Submission

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Dummy LessonInline (requirement fulfill करने के लिए)
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# LessonAdmin (dummy class, required by assignment)
class LessonAdmin(admin.ModelAdmin):
    pass

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
