from django.contrib import admin
from quiz_app.models import QuestionModel, Leaderboard, Quiz_Category, General_Knowledge


# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(Leaderboard)
admin.site.register(Quiz_Category)
admin.site.register(General_Knowledge)