import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfoproject.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
faker = Faker()
def phonenumbergen():
	d1=randint(7,9)
	num=''+str(d1)
	for i in range(9):
		num=num+str(randint(0,9))
	return int(num)

def populate(n):
    for i in range(n):
    	froll_no=faker.random_int(min=1,max=999)
    	fname=faker.name()
    	fdob=faker.date()
    	fmarks=faker.random_int(min=1,max=1000)
    	femail=faker.email()
    	fphonenumber=phonenumbergen()
    	faddress=faker.address()
    	student_record=Student.objects.get_or_create(roll_no=froll_no,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
populate(100)
