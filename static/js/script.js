$('#subbtn').click(function(){
    // e.preventDefault();
    var course_name = $("#cname").val()
    var course_id =$("#uniqueid").val()
    var course_tag = $("#tag :selected").text()
    var curriculam = $("#oldcurriculum").is(':checked');
    // alert(course_name+course_id+course_tag+curriculam);
    // console.log(course_name);
    

    let data = new FormData()
    data.append('name',course_name)
    data.append('course_unique_id',course_id)
    data.append('tag',course_tag)
    data.append('is_old_curriculam',curriculam)
    data.append('subject_file',$('input[id^="subfile"]')[0].files[0]);
    data.append('module_file',$('input[id^="modulefile"]')[0].files[0]);
    data.append('topic_file',$('input[id^="topicfile"]')[0].files[0]);
    // data.append('csrfmiddlewiretoken',"{{ csrf_token }}");
    // console.log(data.get("subject_file"))

    $.ajax({
          url: 'course_creation_script',
          method: "POST",
          processData: false,
          contentType: false,
          MimeType:"multipart/form-data",
          data:data,

          success: function(res){
            console.log(res)
          },
          error: function(status,error){
            console.log(error)
          }
        })

  }
  )