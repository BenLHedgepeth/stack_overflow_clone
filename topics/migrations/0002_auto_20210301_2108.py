# Generated by Django 2.2 on 2021-03-02 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='tag',
            new_name='tags',
        ),
    ]
