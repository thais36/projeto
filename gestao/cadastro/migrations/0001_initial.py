# Generated by Django 4.2 on 2023-05-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('cpf', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('telefone', models.CharField(max_length=256)),
                ('aluno', models.CharField(max_length=256)),
                ('eh_aluno', models.BooleanField()),
                ('curso', models.CharField(max_length=256)),
                ('semestre', models.IntegerField()),
                ('cep', models.CharField(max_length=256)),
                ('enderenco', models.CharField(max_length=256)),
                ('numero_endereco', models.CharField(max_length=256)),
                ('complemento', models.CharField(max_length=256)),
                ('bairro', models.CharField(max_length=256)),
                ('cidade', models.CharField(max_length=256)),
                ('estado', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'pessoa',
                'verbose_name_plural': 'pessoas',
                'db_table': 'pessoa',
                'ordering': ['nome'],
            },
        ),
    ]
