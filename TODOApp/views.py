from django.http import JsonResponse
from TODOApp.models import TodoItem
from TODOApp.serializers import TodoItemSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication


@api_view(['POST'])
@permission_classes([])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # check if user exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'User "{}" already exists'.format(username)}, status=400)

    # create user
    user = User.objects.create_user(
        username=username, password=password, email=email)

    # create token
    # token, created = Token.objects.get_or_create(user=user)

    return JsonResponse({"response": f"User {user} created successfully!"}, status=201)


# Create your views here.
def home(request):
    return JsonResponse({'message': 'Welcome to the TODO App!', 'data': [
        {'list of items': 'api/items/'},
        {'detail of item': 'api/items/<int:pk>/'}
    ]}, status=200)


class TodoItemView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
