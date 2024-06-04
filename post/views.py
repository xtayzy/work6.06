from django.shortcuts import render, HttpResponse, redirect
from django.utils.text import slugify

from post.models import Store, Category, Product
# Create your views here.


def index(request):
    search = request.GET.get('search') or ''
    print(search)
    stores = Store.objects.filter(name__icontains=search)
    ctx = {
        'store': stores
    }
    return render(request, 'post/index.html', context=ctx)


def add_store(request):
    print(request.POST.get('store_name'))
    store = Store()
    store.name = request.POST.get('store_name')
    store.slug = slugify(store.name, allow_unicode=True)
    store.save()
    return redirect('index_page')


def store(request, id):
    store = Store.objects.filter(pk=id)
    ctx = {
        'store': store,
    }

    return render(request, 'post/store.html', context=ctx)


def categories(request, store_id):
    store = Store.objects.filter(pk=store_id)
    cat = Category.objects.all()
    ctx = {
        'store': store,
        'cat': cat
    }
    return render(request, 'post/categories.html', context=ctx)


def products(request, store_id, cat_id):
    products = Product.objects.filter(store__id=store_id, category__id=cat_id)

    ctx = {
        'products': products
    }
    return render(request, 'post/products.html', context=ctx)


def dell_cat(request, id):
    cat = Category.objects.get(pk=id)
    cat.delete()
    return redirect('index_page')


def add_cat(request):
    print(request.POST.get('cat_name'))
    cat = Category()
    cat.name = request.POST.get('cat_name')
    cat.slug = slugify(cat.name, allow_unicode=True)
    cat.save()
    return redirect('index_page')


def edit_page(request, id):
    cat = Category.objects.get(pk=id)
    ctx = {
        'cat': cat,
    }

    return render(request, 'post/edit_cat.html', context=ctx)


def edit_cat(request):
    cat = Category.objects.get(id=request.POST.get('cat_id'))
    cat.name = request.POST.get('cat_name')
    cat.slug = slugify(cat.name, allow_unicode=True)
    cat.save()
    return redirect('index_page')


def dell_pr(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('index_page')


def edit_pr(request, id):
    product = Product.objects.get(pk=id)
    categories = Category.objects.all()
    ctx = {
        'pr': product,
        'cats': categories,
    }
    return render(request, 'post/edit_pr.html', context=ctx)


def pr_edit(request):
    pr = Product.objects.get(id=request.POST.get('pr_id'))
    category = Category.objects.get(id=request.POST.get('cat_id'))
    pr.name = request.POST.get('pr_name')
    pr.price = request.POST.get('pr_price')
    pr.slug = slugify(pr.name, allow_unicode=True)
    pr.category = category
    pr.save()
    return redirect('index_page')


def pr_infa(request, id):
    pr = Product.objects.get(pk=id)
    ctx = {
        'pr': pr
    }
    return render(request, 'post/pr_infa.html', context=ctx)
