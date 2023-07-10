from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class ProductsListAddView(FormView, ListView):
    model = Products  # which table use for create this list
    template_name = 'crm/products_add_list.html'
    context_object_name = 'products_add'  # how it will be name in template
    form_class = ProductForm  # get form from
    success_url = reverse_lazy('crm:products_add')  # redirect to URL path name "products" from "crm" namespace
    paginate_by = 5  # how many items per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class ProductCreateAndListView(CreateView, ListView):
    model = Products
    template_name = 'crm/products_combined.html'
    form_class = ProductForm
    context_object_name = 'product_list'
    success_url = reverse_lazy('crm:products_combined_view')

    def post(self, request, *args, **kwargs):
        # self.object_list = self.get_queryset()
        if 'delete_selected' in request.POST:
            selected_items = request.POST.getlist('selected_item')
            Products.objects.filter(id__in=selected_items).delete()
            return redirect(self.request.path_info)
        elif "save_item" in request.POST:
            form = self.get_form()
            return self.form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products'
        # print(context)
        return context


class EmploysCreateAndListView(View):
    model = Employ
    template_name = 'crm/employs.html'
    form_class = ProductForm
    context_object_name = 'employs'
    success_url = reverse_lazy('crm:employ_list')

    def get(self, request, *args, **kwargs):
        form = EmployForm()
        employs = Employ.objects.all()
        return render(request, self.template_name, {'form': form, 'employs': employs})

    def post(self, request, *args, **kwargs):
        form = EmployForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:employ_list')


class EmployDeleteView(DeleteView):
    model = Employ
    template_name = 'crm/employ_confirm_delete.html'
    success_url = reverse_lazy('crm:employ_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
