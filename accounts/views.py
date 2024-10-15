from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, ProjectForm, ProjectOwnerForm, InvestorForm, AnalystForm
from django.db.models import Q
from .models import ProjectOwner, Investor, Analyst, ProjectProgress,CustomUser, Project, FundingProposal
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
        
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        user = form.get_user()
        login(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else: 
            form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    
@login_required
def logout_view(request):
    logout_view(request)
    return redirect ('login')

@login_required
def profile_view(request):
    return render(request,'accounts/profile.html')

#CRUD views for user management
@login_required
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/use_list.html', {'users':users})

@login_required
def user_update_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else: 
            form = UserRegisterForm(instance=user)
        return render(request, 'accounts/user_form.html', {'form': form})

@login_required
def user_delete_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'accounts/user_confirm_delete.html', {'user':user})

#CRUD views for Project
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'accounts/project_detail.html', {'projects': projects})

def project_detail(request,pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'accounts/project_detail.html', {'project':project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
        return render(request, 'accounts/project_form.html',{'form':form})

def project_update(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, intance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
        return render (request,'accounts/project_form.html', {'form':form})

def project_delete(request, pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        project.delete()
        return render(request, 'accounts/project_confirm_delete.html', {'project':project})


#CRUD views for ProjectOwner
def projectowner_list(request):
    projectowner_list = Project.objects.all()
    return render(request, 'accounts/projectowner_detail.html', {'projectowner_list': projectowner_list})

def projectowner_detail(request,pk):
    project_owner_detail = get_object_or_404(ProjectOwner, pk=pk)
    return render (request, 'accounts/projectowner_detail.html', {'projectowner_detail':projectowner_detail})

def projectowner_create(request):
    if request.method == 'POST':
        form = ProjectOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projectowner')
    else:
        form = ProjectOwnerForm()
        return render(request, 'accounts/projectowner_form.html',{'form':form})

def projectowner_update(request,pk):
    projectowner = get_object_or_404(ProjectOwner,pk=pk)
    if request.method == 'POST':
        form = ProjectOwnerForm(request.POST, intance=projectowner)
        if form.is_valid():
            form.save()
            return redirect('projectowner', pk=projectowner.pk)
    else:
        form = ProjectOwnerForm(instance=projectowner)
        return render (request,'accounts/projectowner_form.html', {'form':form})

def projectowner_delete(request, pk):
    projectowner = get_object_or_404(ProjectOwner,pk=pk)
    if request.method == 'POST':
        projectowner.delete()
        return render(request, 'accounts/projectowner_confirm_delete.html', {'projectowner':projectowner})


#CRUD for views Investor
def investor_list(request):
    investor_list = Investor.objects.all()
    return render(request, 'accounts/investor_list_detail.html', {'investor_list': investor_list})

def investor_detail(request,pk):
    investor_detail = get_object_or_404(Investor, pk=pk)
    return render (request, 'accounts/investor_detail.html', {'investor_detail':investor_detail})

def investor_create(request):
    if request.method == 'POST':
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investor')
    else:
        form = InvestorForm()
        return render(request, 'accounts/investor_form.html',{'form':form})

def investor_update(request,pk):
    investor = get_object_or_404(Investor,pk=pk)
    if request.method == 'POST':
        form = Investor(request.POST, intance=investor)
        if form.is_valid():
            form.save()
            return redirect('investor', pk=investor.pk)
    else:
        form = Investor(instance=investor)
        return render (request,'accounts/investor_form.html', {'form':form})

def investor_delete(request, pk):
    investor = get_object_or_404(Investor,pk=pk)
    if request.method == 'POST':
        Investor.delete()
        return render(request, 'accounts/investor_confirm_delete.html', {'investor':investor})
    

#CRUD for views Analyst
def analyst_list(request):
    analyst_list = Analyst.objects.all()
    return render(request, 'accounts/analyst_list.html', {'analyst_list': analyst_list})

def analyst_detail(request,pk):
    analyst_detail = get_object_or_404(Analyst, pk=pk)
    return render (request, 'accounts/analyst_detail.html', {'analyst_detail':analyst_detail})

def analyst_create(request):
    if request.method == 'POST':
        form = AnalystForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analyst')
    else:
        form = AnalystForm()
        return render(request, 'accounts/analyst_form.html',{'form':form})

def analyst_update(request,pk):
    analyst = get_object_or_404(Analyst,pk=pk)
    if request.method == 'POST':
        form = Analyst(request.POST, intance=analyst)
        if form.is_valid():
            form.save()
            return redirect('analyst', pk=analyst.pk)
    else:
        form = Analyst(instance=analyst)
        return render (request,'accounts/analyst_form.html', {'form':form})

def analyst_delete(request, pk):
    analyst = get_object_or_404(Analyst,pk=pk)
    if request.method == 'POST':
        Analyst.delete()
        return render(request, 'accounts/analyst_confirm_delete.html', {'analyst':analyst})

def project_list(request):
    query = request.GET.get('query', '')
    projects = Project.objects.all()
    if query:
        projects = projects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'accounts/project_list.html', {'projects': projects})

def project_list(request):
    query = request.GET.get('q')
    if query:
        projects = Project.objects.filter(name__icontains=query)
    else:
        projects = Project.objects.all()
    return render(request, 'accounts/project_list.html', {'projects': projects})

def projectowner_list(request):
    query = request.GET.get('q')
    if query:
        projectowners = ProjectOwner.objects.filter(name__icontains=query)
    else:
        projectowners = ProjectOwner.objects.all()
    return render(request, 'accounts/projectowner_list.html', {'projectowners': projectowners})

def investor_list(request):
    query = request.GET.get('q')
    if query:
        investors = Investor.objects.filter(name__icontains=query)
    else:
        investors = Investor.objects.all()
    return render(request, 'accounts/investor_list.html', {'investors': investors})

def analyst_list(request):
    query = request.GET.get('q')
    if query:
        analysts = Analyst.objects.filter(name__icontains=query)
    else:
        analysts = Analyst.objects.all()
    return render(request, 'accounts/analyst_list.html', {'analysts': analysts})

def activate_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            project.is_active = True
            project.save()

            # Envoyer des notifications
            send_mail(
                'Projet Approuvé',
                'Le projet a été approuvé.',
                'admin@example.com',
                ['investor@example.com', 'admin@example.com', 'projectowner@example.com'],
            )
        else:
            # Envoyer un email au porteur de projet
            send_mail(
                'Projet Non Approuvé',
                'La pertinence de votre projet n\'est pas au top. Merci de bien vouloir améliorer.',
                'admin@example.com',
                [project.owner.email],
            )

        return redirect('analyst_list')  # Rediriger vers la page des analystes

    return render(request, 'accounts/validite_project.html', {'project': project})

def propose_funding(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        funder_name = request.POST.get('funder_name')
        amount = request.POST.get('amount')
        
        funding_proposal = FundingProposal.objects.create(
            funder_name=funder_name,
            project=project,
            amount=amount
        )

        # Envoyer une notification à l'administrateur
        send_mail(
            'Nouvelle Proposition de Financement',
            f'Le projet "{project.name}" a reçu une proposition de financement.',
            'admin@example.com',
            ['admin@example.com'],
        )

        # Envoyer un email au porteur de projet
        send_mail(
            'Proposition de Rendez-vous pour Financement',
            f'Votre projet "{project.name}" a reçu une proposition de financement. Veuillez contacter le financeur.',
            'admin@example.com',
            [project.owner.email],
        )

        return redirect('project_list')  # Rediriger après soumission

    return render(request, 'accounts/financement.html', {'project': project})

def toggle_user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.is_active = not user.is_active
        user.save()
        return redirect('admin_user_list')  # Rediriger vers la liste des utilisateurs admin

    return render(request, 'admin/manipuler_user.html', {'user': user})

def create_project_progress(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        progress_description = request.POST.get('progress_description')
        remaining_tasks = request.POST.get('remaining_tasks')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        images = request.FILES.get('images')
        expenses = request.POST.get('expenses')
        
        ProjectProgress.objects.create(
            project=project,
            progress_description=progress_description,
            remaining_tasks=remaining_tasks,
            start_date=start_date,
            end_date=end_date,
            images=images,
            expenses=expenses
        )

        # Envoyer une notification aux investisseurs
        investor_emails = [investor.email for investor in project.investors.all()]
        send_mail(
            'Mise à jour du Projet',
            f'Le projet "{project.name}" a une mise à jour.',
            'admin@example.com',
            investor_emails,
        )
        
        return redirect('project_progress_list')

    return render(request, 'project_progress/create.html', {'project': project})

def project_progress_list(request):
    progresses = ProjectProgress.objects.all()
    return render(request, 'project_progress/list.html', {'progresses': progresses})

def update_project_progress(request, progress_id):
    progress = get_object_or_404(ProjectProgress, id=progress_id)
    
    if request.method == 'POST':
        progress.progress_description = request.POST.get('progress_description')
        progress.remaining_tasks = request.POST.get('remaining_tasks')
        progress.start_date = request.POST.get('start_date')
        progress.end_date = request.POST.get('end_date')
        progress.images = request.FILES.get('images')
        progress.expenses = request.POST.get('expenses')
        progress.save()
        
        return redirect('project_progress_list')

    return render(request, 'project_progress/update.html', {'progress': progress})

def delete_project_progress(request, progress_id):
    progress = get_object_or_404(ProjectProgress, id=progress_id)
    
    if request.method == 'POST':
        progress.delete()
        return redirect('project_progress_list')

    return render(request, 'project_progress/delete.html', {'progress': progress})


def admin_dashboard(request):
    total_projects = Project.objects.count()
    completed_projects = Project.objects.filter(is_completed=True).count()
    active_projects = Project.objects.filter(is_active=True).count()
    funding_proposals = FundingProposal.objects.count()

    context = {
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'active_projects': active_projects,
        'funding_proposals': funding_proposals,
    }

    return render(request, 'admin/tableau_bord.html', context)