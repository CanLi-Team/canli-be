from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,IsAdminUser,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from practicetest.models import *
from django.db.models import Q
from practicetest.serializers import *

# Create your views here.
class FetchQuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_classes = []

    def get(self, request):
        try:
            user = request.user
            context = {"user_id": user.id}
            user_practices = UserPractice.objects.filter(user = user, is_bookmarked = True)
            question_type = request.query_params.get("question_type", None)
            questions = PracticeTest.objects.filter(question_type = question_type)
            return Response({"response":PracticeTestSerializer(questions, context = context, many = True).data}, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":"something went wrong"}, status.HTTP_400_BAD_REQUEST)