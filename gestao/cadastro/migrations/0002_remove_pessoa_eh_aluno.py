# Generated by Django 4.2 on 2023-05-01 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='eh_aluno',
        ),
    ]
