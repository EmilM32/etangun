from django.shortcuts import render
import os
import json
import traceback
from django.db.models import Count, F, Value
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import LevelDict, Members, Addresses
from .tools.login_generator import LoginGenerator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
        login = LoginGenerator(data_front).create()
        if login['code'] == 1:
            return JsonResponse({'info': 'No free login', 'code': 1})
        _new_member = Members()
        _new_member.first_name = data_front['firstName']
        _new_member.last_name = data_front['lastName']
        _new_member.date_of_birth = data_front['birthDate']
        _new_member.belt_level_id = data_front['level']
        _new_member.group = data_front['group']
        _new_member.comment = data_front['comment']
        _new_member.gender = data_front['gender']
        _new_member.login = login['login']
        _new_member.save()

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
                 'comment', 'id', 'gender', 'login')
        all_members = list(all_members)

    except BaseException:
        return JsonResponse({'code': 1})
    return JsonResponse({'data': all_members})


@csrf_exempt
@require_http_methods(["GET"])
def get_all_addresses(request):
    """
    Funkcja pobiera wszystkie aktywne adresy
    """
    try:
        all_addresses = Addresses.objects.filter(is_active=True).annotate(
            postCode=F('post_code'), streetAddress=F('street_address'),
            isActive=F('is_active')
        ).values('id', 'city', 'postCode',
                 'streetAddress', 'descr', 'isActive')
        all_addresses = list(all_addresses)

    except BaseException:
        return JsonResponse({'code': 1})
    return JsonResponse({'data': all_addresses})


@csrf_exempt
@require_http_methods(["POST"])
def add_new_address(request):
    """
    Funkcja zapisuje nowy adres
    {
        "city": "Poznań",
        "postCode": "60-688",
        "streetAddress": "Stróżyńskiego 15e",
        "descr": "dom"
    }

    """
    try:
        data_front = json.loads(request.body)
        _new_address = Addresses()
        _new_address.city = data_front['city']
        _new_address.post_code = data_front['postCode']
        _new_address.street_address = data_front['streetAddress']
        _new_address.descr = data_front['descr']
        _new_address.save()

    except BaseException:
        return JsonResponse({'code': 1})
    return JsonResponse({'code': 0})


@csrf_exempt
@require_http_methods(["POST"])
def edit_address(request):
    try:
        data_front = json.loads(request.body)
        _edited_item = Addresses.objects.get(id=data_front['id'])
        _edited_item.city = data_front['city']
        _edited_item.post_code = data_front['postCode']
        _edited_item.street_address = data_front['streetAddress']
        _edited_item.descr = data_front['descr']
        _edited_item.save()
    except BaseException:
        traceback.print_exc()
        return JsonResponse({'code': 1})
    return JsonResponse({'code': 0})


@csrf_exempt
@require_http_methods(["POST"])
def delete_address(request):
    """
    Funkcja zmienia status adresu na nieaktywny
    """
    try:
        data_front = json.loads(request.body)
        _inactive = Addresses.objects.get(id=data_front)
        _inactive.is_active = False
        _inactive.save()
    except BaseException:
        traceback.print_exc()
        return JsonResponse({'code': 1})
    return JsonResponse({'code': 0})


@csrf_exempt
@require_http_methods(["POST"])
def login_user(request):
    """
    Funkcja logująca użytkownika
    """
    try:
        data_front = json.loads(request.body)
        user = authenticate(username=data_front['username'],
                            password=data_front['password'])
        return_status = None
        if user is not None:
            return_status = True
        else:
            return_status = False

    except BaseException:
        traceback.print_exc()
        return JsonResponse({'code': 1})
    return JsonResponse({'data': return_status, 'code': 0})
