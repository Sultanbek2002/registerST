# Generated by Django 4.1.7 on 2023-03-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useaccounts', '0003_remove_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
