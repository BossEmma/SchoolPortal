# Generated by Django 4.2.8 on 2024-05-01 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_portal_app', '0007_delete_finance_delete_school_alter_faq_answer_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicCalender',
        ),
        migrations.DeleteModel(
            name='FAQ',
        ),
    ]