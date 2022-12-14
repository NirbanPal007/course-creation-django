from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')


@csrf_exempt
def course_creation_script(request):
    coursename = request.POST.get("name")
    course_unique_id = request.POST.get("course_unique_id")
    tag = request.POST.get("tag")
    is_old_curriculam = request.POST.get("is_old_curriculam")
    subject_file = request.FILES.get("subject_file")
    module_file = request.FILES.get("module_file")
    topic_file = request.FILES.get("topic_file")
    print(coursename)
    print(course_unique_id)
    print(tag)
    print(is_old_curriculam)
    print(subject_file)
    print(module_file)
    print(topic_file)


    fss = FileSystemStorage()
    sub_file = fss.save(subject_file.name,subject_file)
    sub_file_url= fss.url(sub_file)
    mod_file = fss.save(module_file.name,module_file)
    mod_file_url= fss.url(mod_file)
    top_file = fss.save(topic_file.name,topic_file)
    top_file_url= fss.url(top_file)
    print(sub_file_url)
    print(mod_file_url)
    print(top_file_url)
 

    # a = CourseForm(name=coursename,couse_unique_id=course_unique_id,tag=tag,is_old_curriculam=is_old_curriculam,subject_file=sub_file_url,module_file=mod_file_url,topic_file=top_file_url)
    # a.save()
    # CourseForm.objects.create(name=coursename,couse_unique_id=course_unique_id,tag=tag,is_old_curriculam=is_old_curriculam,subject_file=sub_file_url,module_file=mod_file_url,topic_file=top_file_url)
    # return redirect(index)
    return render(request,'index.html')
