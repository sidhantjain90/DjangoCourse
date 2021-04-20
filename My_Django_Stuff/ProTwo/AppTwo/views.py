from django.shortcuts import render
from AppTwo.models import User

#NEW! --> Import NewUserForm from AppTwo.forms
from AppTwo.forms import NewUserForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')

def userExtension(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/') #take you back to homePage!
        else:
            print('ERROR FORM INVALID')

    return render(request, 'AppTwo/users.html', {'form':form})
