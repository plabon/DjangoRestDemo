from django.contrib.auth.models import User
from django.shortcuts import render
from main.models import Event
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class MainViewSet(viewsets.GenericViewSet):

    @action(methods=['get'],
            authentication_classes=(TokenAuthentication,),
            permission_classes=(IsAuthenticated, IsAdminUser,),
            detail=False)
    def ping(self, request):
        # if not request.user.is_authenticated:
        #     return Response({'success': False})
        data = {'success': True}
        return Response(data)

    @action(methods=['post'],
            detail=False)
    def register(self, request):
        # print(request.META)
        user_name = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')
        try:
            if User.objects.filter(username=user_name):
              return Response({'message': 'user already exist!'})
            else:
                user = User.objects.create_user(username=user_name, password=password)
                token = Token.objects.create(user=user)
                return  Response({'Token' : token.key})
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'})

        return Response({'success': True})

    @action(methods=['post'],
            detail=False)
    def test_post(self, request):
        # print(request.META)
        first = request.data.get('first')
        last = request.data.get('last')
        print(first)
        print(last)
        return Response({'success': True})

    @action(methods=['post'],
            authentication_classes=(TokenAuthentication,),
            permission_classes=(IsAuthenticated,),
            detail=False)
    def create_event(self, request):
        required_keys = [
            'event_name'
        ]

        if not all(key in request.data for key in required_keys):
            return Response({'success': False, 'message': 'Not all required keys are in JSON payload.'})

        event_name = request.data.get('event_name')
        description = request.data.get('event_description')
        try:
            Event.objects.create(user = request.user, name = event_name, description = description)
            return Response({'message': 'Event added successfully!'})
        except Exception as e:
            print(e)
            return Response({'message': 'something went wrong'})

        return Response({'success': True})