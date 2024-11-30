from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, UpdateRecordForm, CreateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

def home(request):
    query = request.GET.get('search', '')  # Get the search query from the request
    if query:
        records = Record.objects.filter(first_name__icontains=query) | Record.objects.filter(last_name__icontains=query)
    else:
        records = Record.objects.all()  # Return all records if no search term is provided
    
    return render(request, 'webapp/index.html', {'records': records})
    # return render(request, 'webapp/index.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")

            return redirect(request,"my_login") 
    context = {'form':form}
    return render(request, 'webapp/register.html',context = context)



def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password=password)

            if user is not None:
                auth.login(request, user)

    
                return redirect('dashboard')
            
    context = {'form':form}
    return render(request, 'webapp/my_login.html', context = context)



def user_logout(request):
    auth.logout(request)
    messages.success(request,"Logout success!")
    
    return redirect("my_login")



@login_required(login_url="my_login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render (request,'webapp/dashboard.html', context = context)


@login_required(login_url="my_login")
def create_record(request):

    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request,"Your record was created!")

            return redirect("dashboard")
    context = {'form': form}
    return render(request,'webapp/create-record.html', context=context)


@login_required(login_url="my_login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance = record)

        if form.is_valid():
            form.save()
            messages.success(request,"Your record was updated!")

            return redirect("dashboard")
    
    context = {'form':form}
    return render (request,'webapp/update_record.html',context = context)


#-Read or View single record
def singular_record(request, pk):
    all_records = Record.objects.get(id = pk )
    context = {'record':all_records}
    return render(request, 'webapp/view-record.html', context=context)


@login_required(login_url = 'my_login')
def delete_record(request,pk):
    record = Record.objects.get(id = pk)
    record.delete()
    messages.success(request,"Your record was deleted!")

    return redirect("dashboard")

@login_required(login_url="my_login")  
def dashboard(request):
    # Filter records based on the logged-in user
    records = Record.objects.filter(user=request.user)
    return render(request, 'webapp/dashboard.html', {'records': records})