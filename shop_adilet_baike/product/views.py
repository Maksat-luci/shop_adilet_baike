from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
from product.models import Category, Product


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'categories': categories})
#products? category = slug



# def product_list(request,category_slug):
#     # products = Product.objects.all()
#     # if Category.objects.filter(slug=category_slug).exists():
#     #     raise Http 404
#     # products = Product.objects.filter(category_id=category_slug) #фильтрует SELECT* from product WHERE category_id = categoru_slug
#     products = get_list_or_404(Product, category_id=category_slug)
#
#     return render(request, 'product/products_list.html',{'products':products})

# def products_list_2(request):
#     category_slug = request.GET.get('category')
#     products = Product.objects.all()
#     if category_slug is not None:
#         products = prod
# ucts.filter(category_id =category_slug)

def products_list(request,category_slug):
    if  not Category.objects.filter(slug=category_slug).exists():
        raise Http404('нет такой категории')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})



def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html',{'product':product})







#TODO:CRUD
#TODO: поиск и фильрация
#TODO:пагинация
#TODO: функции переписать на классы (СLASS BASED VIEWS)

#all() - выводит все обьекты моделей
# select * from table

#filter() - фильтрует результат queryseta
# select * from table where....

# exclude(условие) - выводит все кроме тех которые написаны в скобках
# select * from table where category !=1

# order_by() - сортировка результатов запроса
# product.objects.order_by('price');
# select * from product order by price ASC;

# Product.objects.order_bby('-price')
# select * from product order by price DESC;


# product.objects.reverse()[:5] - выводит первые пять значений в обратном порядке


# distinct() - исключает повторения

# Product.object.value_list('category',flat=True)- выводит в списке

# product.objects.values('id','title')-> выводит по ключам

# values_list()- выводит значения в виде кортежей

# get() - возвращает условие


# eсли get находит несколько обьектов;

# create()- позволяет создавать новые обьекты модели

# Product.objects.create(title='пшено',description='...',price=100)

# get_or_create(условие) - выбирает обьект, отвечаюший условию,если такого обьекта нет то его создаёт

# bulk_create()- позволяет создавать несколько обьектов

# count() = возвращает количество результатов queryset


# exists() - проверяет если в query set хоть один результат

# bulk_update()- обновляет несколько обьектов

#
# gt -> ">
# "
# lt -> "<"
#
# gte -> ">="
# lte -> "<="

# startswith = откуда он начинает
# istartswith = независит от регистра

# contains= 'day'
# icontains = "day"
# ccsc

# exact="milk"-
# hhhiexact="milk"

# category__isnull = True
# category__isnull = False



# id__in=[1,2,3,4,5,6] -> WHERE id IN (1,2,3,4):

# order.objects.filter(date__range=(start_date,stop_date) -> where date between start_date and end_date

#
#
