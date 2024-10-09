from django.db import models
from django.contrib.auth.models import AbstractUser,User



class CustomUser(AbstractUser):
     is_project_owner = models.BooleanField(default=False)
     is_investor = models.BooleanField(default=False)
     is_analyst = models.BooleanField(default=False)

     pass
def __str__(self):
    return self.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_projects')
   
class ProjectOwner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nberproject = models.ManyToManyField(CustomUser, related_name='prjects_realised')
    
    
class Investor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    

class Analyst(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)

class Project(models.Model):
    # ... vos champs existants ...
    is_active = models.BooleanField(default=False)

class FundingProposal(models.Model):
    funder_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Autres champs...

class ProjectProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    progress_description = models.TextField()
    remaining_tasks = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    images = models.ImageField(upload_to='project_progress/', blank=True, null=True)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)

class Project(models.Model):
    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Ajoutez d'autres champs nécessaires

class FundingProposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs nécessaires