from django.shortcuts import render
from AppTwo.models import User

# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')

def userExtension(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {'users' : users_list}
    return render(request,'AppTwo/users.html', context=users_dict)
