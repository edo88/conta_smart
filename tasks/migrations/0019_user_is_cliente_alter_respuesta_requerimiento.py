# Generated by Django 4.1.1 on 2023-02-21 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_alter_respuesta_requerimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_cliente',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='requerimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
