from rest_framework import viewsets
from rest_framework.response import Response
from quiz_app.models import Quiz_Category, QuestionModel, Leaderboard, General_Knowledge
from quiz_app.api.serializers import (Quiz_CategorySerializer, 
                                      QuestionModelSerializer, 
                                      LeaderboardSerializer, 
                                      General_KnowledgeSerializer,
                                      QuestionAnswerSerializer,
                                      QuizQuestionAnswerSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import status
from quiz_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from quiz_app.api.pagination import QuestionModelformVSPagination
from rest_framework import filters, generics, mixins, status, viewsets
import random
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

class Quiz_CategoryformVS(viewsets.ViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    def list(self, request):
        queryset = Quiz_Category.objects.all()
        serializer = Quiz_CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Quiz_Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = Quiz_CategorySerializer(category)
        return Response(serializer.data)

    def create(self, request):
        permission_classes = [IsAdminOrReadOnly]
        serializer = Quiz_CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
          
    def delete(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = Quiz_CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# quiz_list = Quiz_Category.objects.get(pk=category_id)
# quiz_questions_list = QuestionModel.objects.filter(category=category_id).all()
''' 
    
    def list(self, request):
        queryset = QuestionModel.objects.all()
        serializer = QuestionModelSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request):
        queryset = QuestionModel.objects.all()
        serializer = QuestionModelSerializer(queryset, many=True)
        return Response(serializer.data)
        
        '''
        
'''For Quiz One Question'''
class QuestionModelformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        from rest_framework.pagination import PageNumberPagination
        queryset = list(QuestionModel.objects.filter(category=5).all())
        paginator = QuestionModelformVSPagination()
        random.shuffle(queryset)
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = QuestionModelSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = QuestionModelSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    # def list(self, request):
        
    #     queryset = QuestionModel.objects.all()
    #     #random.shuffle(queryset)
    #     serializer = QuestionModelSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = QuestionModel.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
          
    def delete(self, request, pk):
        queryset = QuestionModel.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
       
       
'''For Quiz Two Question'''
 
class QuestionModelformVS_Two(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        from rest_framework.pagination import PageNumberPagination
        queryset = list(QuestionModel.objects.filter(category=5).all())
        paginator = QuestionModelformVSPagination()
        random.shuffle(queryset)
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = QuestionModelSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = QuestionModelSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    # def list(self, request):
        
    #     queryset = QuestionModel.objects.all()
    #     #random.shuffle(queryset)
    #     serializer = QuestionModelSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = QuestionModel.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
          
    def delete(self, request, pk):
        queryset = QuestionModel.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class LeaderboardformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Leaderboard.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
          
    def delete(self, request, pk):
        queryset = Leaderboard.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Leaderboard.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class General_KnowledgeformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        
        queryset = list(General_Knowledge.objects.all())
        today_topic = random.choice(queryset)
        serializer = General_KnowledgeSerializer(today_topic)
        return Response(serializer.data, )

    def retrieve(self, request, pk=None):
        queryset = General_Knowledge.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data)

    def create(self, request):
        serializer = General_KnowledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
          
    def delete(self, request, pk):
        queryset = General_Knowledge.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = General_Knowledge.objects.get(pk=pk)
        serializer = General_KnowledgeSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class Question_AnswerformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        
        queryset = QuestionModel.objects.all()
        serializer = QuestionAnswerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():        
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Quiz_QuestionformVS(viewsets.ViewSet):
    
    permission_classes = [IsReviewUserOrReadOnly]
    
    def create(self, request):
        serializer = QuizQuestionAnswerSerializer(data=request.data)
        
        if serializer.is_valid():
            
            id = serializer.validated_data['id']
            answer = serializer.validated_data['answer']
            question = QuestionModel.objects.get(pk=id)
            if question.answer == answer:
                return Response("Your Answer is correct")
            else:
                return Response("Your Answer is incorrect")
        else:
            return Response(serializer.errors)
        
    