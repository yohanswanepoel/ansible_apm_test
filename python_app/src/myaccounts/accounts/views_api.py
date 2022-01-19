from django.http import JsonResponse
from .services import refresh_accounts

def get_accounts(request,user_id):
    return JsonResponse(refresh_accounts(user_id))
