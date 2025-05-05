import os
from sqlite3 import IntegrityError

from config.cypher import decrypt_aes
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse


def error_handler_basic(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ObjectDoesNotExist as ex:
            return JsonResponse({'Message': 'Not found'}, status=404)
        except IntegrityError as ex:
            return JsonResponse({'Message': (str(ex))}, status=406)
        except Exception as ex:
            return JsonResponse({'Message': (str(ex))}, status=400)
    return wrapper


def mfc_auth_token(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        token = ''
        try:
            token = decrypt_aes(request.headers['Token'])
        except Exception as ex:
            print(ex)
        if token != os.environ.get("AES_TOKEN"):
            return JsonResponse({'Message': 'Failed authorization'}, status=403)
        return func(*args, **kwargs)
    return wrapper


def student_mfc_token(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        if not request.headers.get('Token') or request.headers['Token'] != os.environ.get("STUD_TOKEN"):
            return JsonResponse({'Message': 'Failed authorization'}, status=403)
        return func(*args, **kwargs)
    return wrapper
