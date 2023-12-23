from django.shortcuts import render
from django.http import HttpResponse
from user.models import Profile
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def StudentView(request):
    students = Profile.objects.all()

    return render(request,"student.html",{'students':students})

@csrf_exempt
def StudentAddView(request):
    
    output = {"messages": []}
    method = request.method
    if method == 'POST':
        data = request.POST
        profile_data = {
			'first_name': data['first_name'],
			'last_name': data['last_name'],
			'email' :data['email'],
			'mobile_no': data['mobile_no'],
			'grade' :data['grade'],
            'faculty' :data['faculty'],
		}
    
    if len(profile_data['first_name']) < 3:
        output['messages'].append("first_name should be at least 3 characters")

    if len(profile_data['last_name']) < 3:
        output['messages'].append("last_name should be at least 3 characters")

    if not profile_data['mobile_no'].isdigit():
        output['messages'].append("Invalid phone number")
        print (output)

    if not output['messages']:
        profile = Profile.objects.filter(email=profile_data['email'])
        
        if profile:
            output['messages'].append(f"Student with email : {profile_data['email']} already exists.")
            
        else:
            p = Profile(**profile_data)
            p.save()
            print ('saved successfully')
            output['messages'].append(f"{profile_data['first_name']} Added Successfully !")

            students = Profile.objects.all()
            output['students'] = students
            
            return render(request,"student.html",output)
