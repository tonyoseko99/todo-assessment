from django.http import JsonResponse
from TODOApp.models import TodoItem
from TODOApp.serializers import TodoItemSerializer
from rest_framework import generics, permissions, authentication

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

# import requests

# url = 'http://localhost:8000/api-token-auth/'
# headers = {'Authorization': 'Token ' +
#            '8f60651d513ab3fcecc4649eccf5c0a2b7050756'}
# response = requests.get(url, headers=headers)


class GenerateTokenView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User "{}" does not exist'.format(username)})
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class TodoItemAuthToken(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


# Create your views here.
def home(request):
    return JsonResponse({'message': 'Welcome to the TODO App!', 'data': [
        {'list of items': 'api/items/'},
        {'detail of item': 'api/items/<int:pk>/'}
    ]}, status=200)


class TodoItemView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [
        authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [
        authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
