from django.views.generic import ListView

from.models import Produto

class IndexListView(ListView):
    template_name = 'index.html'
    paginate_by = 2
    model = Produto
    ordering = 'id'




