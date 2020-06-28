from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Plans


class Test(View):

    planss = Plans.objects.all()
    output = ''
    # output = f"names of the objects{len(planss)}s"
    for plans in planss:
        output += f"names of the objects{plans.name_plan}s{plans.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('first visit')
