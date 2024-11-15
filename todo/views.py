from todo.models import Todo
from django.shortcuts import render, redirect
from todo.forms import UserSignupForm, UserLogin
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse_lazy
from django.views.generic import (ListView,CreateView,
                                  DetailView,UpdateView,
                                  DeleteView)

# Create your views here.

def index(request):
    return render(request, "todo/index.html")

def userSignup(request):
    if request.method == "POST":
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserSignupForm()  # Moved this outside of the POST check

    return render(request, 'todo/signup.html', {'form': form})

def userLogin(request):
    if request.method == "POST":
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                form.add_error(None, "Invalid username or password.")  # Add error if authentication fails
    else:
        form = UserLogin()  # Moved this outside of the POST check

    return render(request, 'todo/login.html', {'form': form})

def userLogout(request):
    logout(request)
    return redirect('index')

############CLASS VIEW#####################################
##########################################################
class TodoListView(ListView):
    model = Todo
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user,completed_date__isnull=True)

class TodoCreateView(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy('list')
    
class TodoDetailView(DetailView):
    model = Todo
    