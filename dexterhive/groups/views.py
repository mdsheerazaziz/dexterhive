from django.http.response import HttpResponse
from dexterhive.groups import resources


def create_group(requests):
    group_details = {'name': requests.POST.get('group_name'),
                     'about': requests.POST.get('about'),
                     'group_type': requests.POST.get('group_type'),
                     'group_visibility': requests.POST.get('group_visibility')
                     }
    resources.create_group(group_details)
    return HttpResponse("Created")
