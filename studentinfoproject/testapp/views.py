from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def home_page_view(request):
	#students=Student.objects.all()
	####take student marks less than 35
	#students=Student.objects.filter(marks__lt=35) 
	####I want only students whose name startwith "a"
	#students=Student.objects.filter(name__startswith='A')
	#### I want all student but orderby marks
	###bydefault it will give asending order
	#students=Student.objects.all().order_by('marks')
	### for desending order
	students=Student.objects.all().order_by('-marks')
	return render(request,'testapp/index.html',{'students':students})