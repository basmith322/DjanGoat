from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template
from django.shortcuts import render
from app.decorators import user_is_authenticated
from app.views import utils


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def schedule_index(request):
    current_user = utils.current_user(request)
    context = {'current_user': current_user}
    return render(request, 'schedule/index.html', context=context)


@require_http_methods(["GET"])
@user_is_authenticated
def get_pto_schedule_schedule_index(request):
    return HttpResponse("PTO schedule index")


@require_http_methods(["GET"])
@user_is_authenticated
def new_schedule(request):
    return HttpResponse("New schedule")


@require_http_methods(["GET"])
@user_is_authenticated
def edit_schedule(request, schedule_id):
    return HttpResponse("Edit schedule " + str(schedule_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def schedule(request, schedule_id):
    return HttpResponse("View schedule " + str(schedule_id))
