from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class Cloth1ListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Somethings").order_by("-id")
    template_name = "cloth1_list.html"
    context_object_name = 'cloth1_list'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Somethings").order_by("-id")


class Cloth2ListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Man cloth").order_by("-id")
    template_name = "cloth2_list.html"
    context_object_name = 'cloth2_list'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Man cloth").order_by("-id")


class Cloth3ListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Women cloth").order_by("-id")
    template_name = "cloth3_list.html"
    context_object_name = 'cloth3_list'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Women cloth").order_by("-id")


class Cloth4ListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Child cloth").order_by("-id")
    template_name = "cloth4_list.html"
    context_object_name = 'cloth4_list'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Child cloth").order_by("-id")


class ClothDetailView(DetailView):
    template_name = "cloth1_detail.html"

    def get_object(self, **kwargs):
        id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=id)


class OrderCreateView(CreateView):
    template_name = "add_order.html"
    form_class = forms.OrderForm
    success_url = "/products/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
