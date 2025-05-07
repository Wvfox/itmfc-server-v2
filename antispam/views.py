from django.http import JsonResponse
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser

from config.decorators import mfc_auth_token, error_handler_basic
from .serializers import *


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
@mfc_auth_token
@error_handler_basic
def dictionary_list(request):
    data = request.data

    if request.method == 'GET':
        dictionaries = AntispamDictionary.objects.all()
        serializer = AntispamDictionarySerializer(dictionaries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print(data)
        serializer = AntispamDictionarySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


@api_view(['PATCH'])
@parser_classes([JSONParser])
@mfc_auth_token
@error_handler_basic
def dictionary_detail(request):

    if request.method == 'PATCH':
        data = request.data
        if AntispamDictionary.objects.filter(word=data['word']).exists():
            return JsonResponse(AntispamDictionarySerializer(AntispamDictionary.objects.get(word=data['word'])).data)
        return JsonResponse({'value': 0}, status=404)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
@mfc_auth_token
@error_handler_basic
def public_log_list(request):
    data = request.data

    if request.method == 'GET':
        public_logs = PublicChatLog.objects.all()
        serializer = PublicChatLogSerializer(public_logs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = PublicChatLogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)
