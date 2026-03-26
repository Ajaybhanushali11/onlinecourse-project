from django.contrib import admin
from .models import Course, Lesson, Enrollment, Question, Choice, Submission

# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Inline for Lesson inside Course
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Register models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
