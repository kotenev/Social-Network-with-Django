from django.shortcuts import render, get_object_or_404
from .models import Category, Teacher


def teacher_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Teacher.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/teacher/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def teacher_detail(request, id, slug):
    product = get_object_or_404(Teacher,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
