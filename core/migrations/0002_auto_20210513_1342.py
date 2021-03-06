# Generated by Django 3.1.10 on 2021-05-13 13:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, choices=[('INI', 'INITIATED'), ('PEN', 'PENDING'), ('CMP', 'COMPLETED'), ('FAL', 'FAILED'), ('ERR', 'ERROR')], default='INI', max_length=3, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('IN', 'IN'), ('OUT', 'OUT')], max_length=3, verbose_name='type'),
        ),
    ]
