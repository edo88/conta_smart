# Generated by Django 4.1.1 on 2023-03-02 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_rename_description_solicitud_comentario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='nombre',
        ),
    ]