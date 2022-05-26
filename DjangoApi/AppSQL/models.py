from django.db import models

class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField()

class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=30)
    note_content = models.CharField(max_length=1000)
    note_author = models.ForeignKey(Clients, on_delete=models.CASCADE)
    note_date = models.DateField(auto_now_add=True)
