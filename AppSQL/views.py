from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AppSQL.models import Notes, Clients
from AppSQL.serializers import NotesSerializer, ClientsSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def clientApi(request,id=0):
    if request.method=='GET':
        clients = Clients.objects.all()
        clients_serializer=ClientsSerializer(clients,many=True)
        return JsonResponse(clients_serializer.data,safe=False)
    elif request.method=='POST':
        client_data=JSONParser().parse(request)
        clients_serializer=ClientsSerializer(data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        client_data=JSONParser().parse(request)
        client=Clients.objects.get(client_id=id)
        clients_serializer=ClientsSerializer(client,data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        client=Clients.objects.get(client_id=id)
        client.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def noteApi(request,id=0):
    if request.method=='GET':
        notes = Notes.objects.all()
        notes_serializer=NotesSerializer(notes,many=True)
        return JsonResponse(notes_serializer.data,safe=False)
    elif request.method=='POST':
        note_data=JSONParser().parse(request)
        notes_serializer=NotesSerializer(data=note_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        note_data=JSONParser().parse(request)
        note=Notes.objects.get(note_id=id)
        notes_serializer=NotesSerializer(note,data=note_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        note=Notes.objects.get(note_id=id)
        note.delete()
        return JsonResponse("Deleted Successfully",safe=False)