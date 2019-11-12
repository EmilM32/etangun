from django.shortcuts import render
import os
import json
import traceback
from django.db.models import Count, F, Value
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import LevelDict, Members


@csrf_exempt
@require_http_methods(["GET"])
def get_belt_level(request):
    try:
        belt_level = LevelDict.objects.all().values()
        belt_level = list(belt_level)

    except BaseException:
        return JsonResponse({'data': 'error'})
    return JsonResponse({'data': belt_level})


@csrf_exempt
@require_http_methods(["POST"])
def save_new_member(request):
    try:
        data_front = json.loads(request.body)
        new_member = Members()
        new_member.first_name = data_front['firstName']
        new_member.last_name = data_front['lastName']
        new_member.date_of_birth = data_front['birthDate']
        new_member.belt_level_id = data_front['level']
        new_member.group = data_front['group']
        new_member.comment = data_front['comment']
        new_member.save()

    except BaseException:
        return JsonResponse({'code': 1})
    return JsonResponse({'code': 0})


@csrf_exempt
@require_http_methods(["GET"])
def get_all_members(request):
    try:
        all_members = Members.objects.annotate(
            firstName=F('first_name'), lastName=F('last_name'),
            birthDate=F('date_of_birth'), level=F('belt_level__belt_level')
        ).values('firstName', 'lastName', 'birthDate', 'level', 'group',
                 'comment')
        all_members = list(all_members)

    except BaseException:
        return JsonResponse({'code': 1})
    return JsonResponse({'data': all_members})
