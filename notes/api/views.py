#from django.shortcuts import render

# Create your views here.

import re
from django.http import JsonResponse

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': ['GET'],
            'body': None,
            'description': 'Return an array of notes.',
        },
        {
            'Endpoint': '/notes/id',
            'method': ['GET'],
            'body': None,
            'description': 'Return a note with the given id.',
        },
        {
            'Endpoint': '/notes/create/',
            'method': ['POST'],
            'body': {'body': ''},
            'description': 'Create a new note with data sent in post request.',
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': ['PUT'],
            'body': {'body': ''},
            'description': 'Update a note with the given id with data sent in put request.',
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': ['DELETE'],
            'body': None,
            'description': 'Delete a note with the given id.',
        }, 
    ]

    return JsonResponse(routes, safe=False)
