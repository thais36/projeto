# Generated by Django 4.2 on 2023-05-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_remove_pessoa_eh_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='aluno',
            field=models.BooleanField(default=False),
        ),
    ]
