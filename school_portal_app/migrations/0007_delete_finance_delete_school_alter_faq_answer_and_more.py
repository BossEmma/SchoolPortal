# Generated by Django 4.2.8 on 2024-04-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_portal_app', '0006_school_admission'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Finance',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Question'),
        ),
    ]