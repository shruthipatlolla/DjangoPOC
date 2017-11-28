from django.http import HttpResponse

from django.shortcuts import render

from django_tables2 import RequestConfig

from tables import PersonTable

from models import Person

data = [
    {'name': 'shr', "project" : "DT", "year":2016},
    {'name': 'sos', "project" : "DT", "year":2016}
   
]


def person_list(request):
    table = PersonTable(data)
    RequestConfig(request).configure(table)
    return render(request, 'testData/person_list.html', {
        'table': table})
    





