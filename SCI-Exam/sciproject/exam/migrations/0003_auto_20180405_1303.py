# Generated by Django 2.0.1 on 2018-04-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20180405_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examiner',
            name='name',
        ),
        migrations.RemoveField(
            model_name='examinerlacthroughmodel',
            name='examiner',
        ),
        migrations.RemoveField(
            model_name='examinerlacthroughmodel',
            name='lac',
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['Sid']},
        ),
        migrations.RemoveField(
            model_name='subject',
            name='Examiner',
        ),
        migrations.AddField(
            model_name='subject',
            name='examiner',
            field=models.CharField(default='foo', max_length=100),
        ),
        migrations.AddField(
            model_name='subject',
            name='ratio',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=7),
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Degree',
            field=models.IntegerField(choices=[('0', 'Bachelor'), ('1', 'Master'), ('2', 'Doctor')], default='0'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='S_type',
            field=models.IntegerField(choices=[('0', 'One Instructor'), ('1', 'Multiple Instructor')], default='0'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Sid',
            field=models.CharField(default='foo', max_length=5),
        ),
        migrations.AlterField(
            model_name='subject',
            name='T_type',
            field=models.IntegerField(choices=[('0', 'Choice'), ('1', 'Short answer'), ('2', 'Interview and Practice')], default='0'),
        ),
        migrations.DeleteModel(
            name='Examiner',
        ),
        migrations.DeleteModel(
            name='ExaminerLacThroughModel',
        ),
    ]