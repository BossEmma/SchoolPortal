# Generated by Django 4.2.8 on 2024-04-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_portal_app', '0005_school_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='admission',
            field=models.JSONField(blank=True, max_length=1000, null=True, verbose_name='admission'),
        ),
    ]