# Generated by Django 2.1.2 on 2019-07-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyname', models.CharField(max_length=200)),
                ('surveynumber', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
    ]
