from rest_framework.routers import DefaultRouter
from quiz_app.api.views import (Quiz_CategoryformVS, 
                                QuestionModelformVS, 
                                LeaderboardformVS, 
                                General_KnowledgeformVS,
                                Question_AnswerformVS, 
                                Quiz_QuestionformVS, QuestionModelformVS_Two)

from django.urls import path, include

router = DefaultRouter()

router.register('quizcategory', Quiz_CategoryformVS, basename = 'quizcategory')
router.register('quiz_one_question', QuestionModelformVS, basename = 'quizquestionone')
router.register('quiz_two_question', QuestionModelformVS_Two, basename = 'quizquestiontwo')
router.register('leaderboard', LeaderboardformVS, basename = 'leaderboard')
router.register('generalknowledge', General_KnowledgeformVS, basename = 'generalknowledge')
router.register('questionanswer', Question_AnswerformVS, basename = 'questionanswer')
router.register('takequiz', Quiz_QuestionformVS, basename = 'takequiz')

urlpatterns = [
    
    path('', include(router.urls)),
    
]
