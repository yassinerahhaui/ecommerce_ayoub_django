# Generated by Django 4.2.6 on 2024-02-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
    ]
