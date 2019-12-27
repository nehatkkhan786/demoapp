from django.shortcuts import render
from . models import Profile
import pdfkit
import io
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def homepage(request):
	if request.method == 'POST':
		name = request.POST.get("name", "")
		email = request.POST.get("email", "")
		phone = request.POST.get("phone", "")
		summary = request.POST.get("summary", "")
		university = request.POST.get("university", "")
		school = request.POST.get("school")
		work_experience = request.POST.get("work_experience", "")

		profile = Profile(name = name, email=email, phone = pmmaryhone, summary=su, university = university, school = school, work_experience=work_experience)
		profile.save()

	return render(request, 'homepage.html', {})

def resume(request, id):
	user_profile = Profile.objects.get(pk=id)
	template = loader.get_template('includes/resume.html')
	html = template.render({'user_profile':user_profile})
	options = {

		'page-size':'Letter',
		'encoding': 'UTF-8',
	}
	pdf = pdfkit.from_string(html, False, options)
	response = HttpResponse(pdf, content_type = 'application/pdf')
	response['Content-Disposition']= 'attachment'
	filename = 'resume.pdf'
	return response

def cv_list(request):
	user_profile = Profile.objects.all()
	return render(request, 'cv_list.html', {'user_profile':user_profile})

























