from rest_framework import serializers
from quiz_app.models import Quiz_Category, QuestionModel, Leaderboard, General_Knowledge

class QuestionModelSerializer(serializers.ModelSerializer):
    #category = serializers.StringRelatedField(read_only=True)
    #category = serializers.CharField(source='category.quiz_name')
    
    class Meta:
        model = QuestionModel
        exclude = ('answer',)
        #fields = "__all__"
        
class Quiz_CategorySerializer(serializers.ModelSerializer):
    
    category = QuestionModelSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz_Category
        fields = "__all__"
           
class LeaderboardSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Leaderboard
        fields = "__all__"
        #exclude = ('id',)
        
class General_KnowledgeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = General_Knowledge
        fields = "__all__"
        
        
class QuestionAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionModel
        fields = ['id', 'question', 'answer', 'category']
     
    '''    
class QuizQuestionAnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    answer = serializers.CharField(max_length=200)
    ''' 

class QuizQuestionAnswerSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    answer = serializers.CharField(max_length=200)