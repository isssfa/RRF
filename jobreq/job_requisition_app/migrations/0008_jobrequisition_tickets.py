# Generated by Django 4.0.1 on 2022-01-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_requisition_app', '0007_delete_jobrequisition_delete_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisition_date', models.DateField()),
                ('hc_req', models.IntegerField()),
                ('req_raised_by', models.CharField(max_length=150)),
                ('created_by_id', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('process_type_one', models.CharField(max_length=50)),
                ('process_type_two', models.CharField(max_length=50)),
                ('process_type_three', models.CharField(max_length=50)),
                ('salary_rang_frm', models.IntegerField()),
                ('salary_rang_to', models.IntegerField()),
                ('qualification', models.CharField(max_length=100)),
                ('other_quali', models.CharField(blank=True, max_length=150, null=True)),
                ('skills_set', models.TextField()),
                ('languages', models.TextField()),
                ('shift_timing', models.CharField(max_length=20)),
                ('shift_timing_frm', models.CharField(blank=True, max_length=20, null=True)),
                ('shift_timing_to', models.CharField(blank=True, max_length=20, null=True)),
                ('working_from', models.CharField(max_length=20)),
                ('working_to', models.CharField(max_length=20)),
                ('week_no_days', models.IntegerField()),
                ('week_from', models.CharField(blank=True, max_length=20, null=True)),
                ('week_to', models.CharField(blank=True, max_length=20, null=True)),
                ('requisition_type', models.CharField(max_length=50)),
                ('candidate_name', models.TextField(blank=True, null=True)),
                ('closure_date', models.DateField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('source_empref_emp_name', models.CharField(blank=True, max_length=150, null=True)),
                ('source_empref_emp_id', models.CharField(blank=True, max_length=20, null=True)),
                ('source_social', models.CharField(blank=True, max_length=100, null=True)),
                ('source_partners', models.CharField(blank=True, max_length=100, null=True)),
                ('recruited_people', models.IntegerField(blank=True, null=True)),
                ('request_status', models.CharField(blank=True, default='Pending', max_length=20, null=True)),
                ('candidate_remark', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_requisition_id', models.CharField(max_length=10)),
                ('created_by', models.CharField(max_length=150)),
                ('created_by_id', models.CharField(max_length=30)),
                ('created_date', models.DateField()),
                ('edited_by', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
