# Generated by Django 4.2.7 on 2023-11-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('client_id', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
