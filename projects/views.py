from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from .models import Project,Tag,Review
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from .utils import searchProject, paginateProjects
from django.contrib.auth.decorators import login_required
def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context = {'projects': projects,'search_query':search_query,'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        messages.success(request, 'Your review was successfully submited')
        return redirect('project', pk=projectObj.id)
    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form':form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object':project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, "delete_template.html", context)