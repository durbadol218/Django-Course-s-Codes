from django.shortcuts import render
from cars.models import CarBrand, CarModel

def homepage(request,slug = None):
    data = CarModel.objects.all()
    if slug is not None:
        brand = CarBrand.objects.get(slug=slug)
        data = CarModel.objects.filter(brand_name= brand)
    brands = CarBrand.objects.all()
    # print(data)
    return render(request,'home.html',{'data':data,'brand':brands})