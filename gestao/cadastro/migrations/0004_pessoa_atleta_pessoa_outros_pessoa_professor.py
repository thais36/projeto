# Generated by Django 4.2 on 2023-05-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_alter_pessoa_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='atleta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='outros',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='professor',
            field=models.BooleanField(default=False),
        ),
    ]
