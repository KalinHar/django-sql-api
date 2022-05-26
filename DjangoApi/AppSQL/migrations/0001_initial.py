# Generated by Django 2.1.15 on 2022-05-26 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=30)),
                ('client_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_title', models.CharField(max_length=30)),
                ('note_content', models.CharField(max_length=1000)),
                ('note_date', models.DateField(auto_now_add=True)),
                ('note_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppSQL.Clients')),
            ],
        ),
    ]
