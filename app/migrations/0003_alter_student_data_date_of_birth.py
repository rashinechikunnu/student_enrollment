# Generated by Django 4.2.16 on 2024-11-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_class_room_subject_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='date_of_birth',
            field=models.CharField(max_length=10),
        ),
    ]