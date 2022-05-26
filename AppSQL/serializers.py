from rest_framework import serializers
from AppSQL.models import Notes, Clients

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields=('note_id', 'note_title', 'note_content', 'note_author', 'note_date')

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clients
        fields=('client_id', 'client_name', 'client_email')