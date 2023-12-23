from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Courses
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def CourseView(request):
    courses = Courses.objects.all()
    return render(request, 'course.html', {'courses': courses})

@csrf_exempt
def CourseAddView(request):
    output = {'messages': []}
    method = request.method

    if method == 'POST':
        data = request.POST
        course_data = {
            'course_name': data['course_name'],
            'instructor': data['instructor'],
            'course_length': data['course_length'],
        }

        if not output['messages']:
            courses = Courses.objects.filter(course_name=course_data['course_name'])

            if courses:
                output['messages'].append(f'Course with name: {course_data["course_name"]} already exists.')
            else:
                c = Courses(**course_data)
                c.save()
                print('saved successfully')
                output['messages'].append(f'Course with name: {course_data["course_name"]} Added Successfully !')

                courses = Courses.objects.all()
                output['courses'] = courses

    return render(request, "course.html", output)


# def CourseAssignmentView(request):
#     output = {}

#     if request.method == 'POST':
#         course_id = request.POST['course']
#         student_id = request.POST['student']
#         sc = StudentCourse.objects.filter(
# 			student_id=student_id,
# 			course_id=course_id
# 			)
#         if sc:
#             output['message'] = 'Already enrolled'
#         else:
#             sc = StudentCourse(
# 			student_id=student_id,
# 			course_id=course_id,
# 			registration_date=datetime.now()
# 			)
#             sc.save()
            
#     output['students'] = Profile.objects.filter(
# 		).values('id', 'first_name')
#     courses = Course.objects.filter()
#     output['courses'] = courses.values('id', 'name')
#     output['student_courses'] = StudentCourse.objects.filter(
# 		).values('student__first_name', 'course__name')
    
#     return render(request, "assignment.html", output)