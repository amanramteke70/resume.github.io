# Generated by Django 4.2.6 on 2023-10-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_contact_delete_my_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='text',
        ),
    ]