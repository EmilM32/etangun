from django.shortcuts import render
import os
import json
import traceback
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods


@csrf_exempt
def test_function(request):
    return JsonResponse({'data': 0})
