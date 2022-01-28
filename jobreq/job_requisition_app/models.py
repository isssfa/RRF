from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=30, unique=True)
    emp_name = models.CharField(max_length=100)
    emp_desi = models.CharField(max_length=100)
    emp_process = models.CharField(max_length=150)
    emp_rm1 = models.CharField(max_length=100)
    emp_rm1_id = models.CharField(max_length=30)
    emp_rm2 = models.CharField(max_length=100)
    emp_rm2_id = models.CharField(max_length=30)
    emp_rm3 = models.CharField(max_length=100)
    emp_rm3_id = models.CharField(max_length=30)
    agent_status = models.CharField(max_length=30)

    def __str__(self):
        return self.emp_name


class JobRequisition(models.Model):
    requisition_date = models.DateField()
    hc_req = models.IntegerField()
    req_raised_by = models.CharField(max_length=150)
    created_by_manager = models.CharField(max_length=150)
    created_by_manager_id = models.CharField(max_length=30)
    created_by_id = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    process_type_one = models.CharField(max_length=50)
    process_type_two = models.CharField(max_length=50)
    process_type_three = models.CharField(max_length=50)
    salary_rang_frm = models.IntegerField()
    salary_rang_to = models.IntegerField()
    qualification = models.CharField(max_length=100)

    other_quali = models.CharField(max_length=150,null=True,blank=True)

    skills_set = models.TextField()
    languages = models.TextField()

    shift_timing = models.CharField(max_length=20)
    shift_timing_frm = models.CharField(max_length=20,null=True,blank=True)
    shift_timing_to = models.CharField(max_length=20,null=True,blank=True)

    type_of_working = models.CharField(max_length=100)

    working_from = models.CharField(max_length=20,null=True,blank=True)
    working_to = models.CharField(max_length=20,null=True,blank=True)
    week_no_days = models.IntegerField(null=True,blank=True)

    week_from = models.CharField(max_length=20,null=True,blank=True)
    week_to = models.CharField(max_length=20,null=True,blank=True)

    requisition_type = models.CharField(max_length=50)
    reason_for_replace = models.TextField(null=True,blank=True)
    closure_date = models.DateField(null=True, blank=True)

    candidate_name_1 = models.TextField(null=True,blank=True)
    source_1 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_1 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_1 = models.CharField(max_length=20,null=True,blank=True)
    source_social_1 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_1 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_2 = models.TextField(null=True,blank=True)
    source_2 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_2 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_2 = models.CharField(max_length=20,null=True,blank=True)
    source_social_2 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_2 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_3 = models.TextField(null=True,blank=True)
    source_3 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_3 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_3 = models.CharField(max_length=20,null=True,blank=True)
    source_social_3 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_3 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_4 = models.TextField(null=True,blank=True)
    source_4 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_4 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_4 = models.CharField(max_length=20,null=True,blank=True)
    source_social_4 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_4 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_5 = models.TextField(null=True,blank=True)
    source_5 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_5 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_5 = models.CharField(max_length=20,null=True,blank=True)
    source_social_5 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_5 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_6 = models.TextField(null=True,blank=True)
    source_6 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_6 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_6 = models.CharField(max_length=20,null=True,blank=True)
    source_social_6 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_6 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_7 = models.TextField(null=True,blank=True)
    source_7 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_7 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_7 = models.CharField(max_length=20,null=True,blank=True)
    source_social_7 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_7 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_8 = models.TextField(null=True,blank=True)
    source_8 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_8 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_8 = models.CharField(max_length=20,null=True,blank=True)
    source_social_8 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_8 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_9 = models.TextField(null=True,blank=True)
    source_9 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_9 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_9 = models.CharField(max_length=20,null=True,blank=True)
    source_social_9 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_9 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_10 = models.TextField(null=True,blank=True)
    source_10 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_10 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_10 = models.CharField(max_length=20,null=True,blank=True)
    source_social_10 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_10 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_11 = models.TextField(null=True,blank=True)
    source_11 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_11 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_11 = models.CharField(max_length=20,null=True,blank=True)
    source_social_11 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_11 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_12 = models.TextField(null=True,blank=True)
    source_12 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_12 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_12 = models.CharField(max_length=20,null=True,blank=True)
    source_social_12 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_12 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_13 = models.TextField(null=True,blank=True)
    source_13 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_13 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_13 = models.CharField(max_length=20,null=True,blank=True)
    source_social_13 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_13 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_14 = models.TextField(null=True,blank=True)
    source_14 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_14 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_14 = models.CharField(max_length=20,null=True,blank=True)
    source_social_14 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_14 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_15 = models.TextField(null=True,blank=True)
    source_15 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_15 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_15 = models.CharField(max_length=20,null=True,blank=True)
    source_social_15 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_15 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_16 = models.TextField(null=True,blank=True)
    source_16 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_16 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_16 = models.CharField(max_length=20,null=True,blank=True)
    source_social_16 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_16 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_17 = models.TextField(null=True,blank=True)
    source_17 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_17 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_17 = models.CharField(max_length=20,null=True,blank=True)
    source_social_17 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_17 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_18 = models.TextField(null=True,blank=True)
    source_18 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_18 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_18 = models.CharField(max_length=20,null=True,blank=True)
    source_social_18 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_18 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_19 = models.TextField(null=True,blank=True)
    source_19 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_19 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_19 = models.CharField(max_length=20,null=True,blank=True)
    source_social_19 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_19 = models.CharField(max_length=100,null=True,blank=True)

    candidate_name_20 = models.TextField(null=True,blank=True)
    source_20 = models.CharField(max_length=50,null=True,blank=True)
    source_emp_name_20 = models.CharField(max_length=150,null=True,blank=True)
    source_emp_id_20 = models.CharField(max_length=20,null=True,blank=True)
    source_social_20 = models.CharField(max_length=100,null=True,blank=True)
    source_partners_20 = models.CharField(max_length=100,null=True,blank=True)


    closed_by = models.CharField(max_length=150,null=True,blank=True)
    closed_by_id = models.CharField(max_length=30,null=True,blank=True)

    recruited_people = models.IntegerField(null=True,blank=True)
    request_status = models.CharField(max_length=20, default="Pending")
    candidate_remark = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)


class Tickets(models.Model):
    job_requisition_id = models.CharField(max_length=10)
    created_by = models.CharField(max_length=150)
    created_by_id = models.CharField(max_length=30)
    created_date = models.DateField()
    edited_by = models.TextField(null=True,blank=True)
