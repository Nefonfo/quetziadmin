from django.views.generic.edit import CreateView
from .models import Project
from .forms import ProjectForm
# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm

    def __init__(self):
        data = ProjectForm()
        data.fields['boss']
        super().__init__()