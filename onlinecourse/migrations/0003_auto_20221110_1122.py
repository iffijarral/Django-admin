# Generated by Django 3.1.3 on 2022-11-10 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221110_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_content',
            new_name='content',
        ),
    ]
