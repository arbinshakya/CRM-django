# Generated by Django 5.1.2 on 2024-11-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_record_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]
