# Generated by Django 4.0.2 on 2022-02-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_requisition_app', '0024_auto_20220211_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrequisition',
            name='edited_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]