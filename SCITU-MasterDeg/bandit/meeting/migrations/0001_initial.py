# Generated by Django 2.0.2 on 2018-03-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meetingTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('dueDate', models.CharField(max_length=200)),
            ],
        ),
    ]
