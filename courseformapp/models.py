from django.db import models

# Create your models here.

class CourseForm(models.Model):
    name=models.CharField(max_length=255,null=False, blank=False)
    couse_unique_id=models.CharField(max_length=255,null=False, blank=False)
    tag = models.CharField(max_length=255,null=False, blank=False)
    is_old_curriculam = models.BooleanField(default=False)
    subject_file = models.FileField(upload_to= 'subfile')
    module_file = models.FileField(upload_to= 'modfile')
    topic_file =models.FileField(upload_to= 'topfile')



