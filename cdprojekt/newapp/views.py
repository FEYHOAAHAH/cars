from django.shortcuts import render

from .models import Car


# Create your views here.

def car_info(request):
    cars = Car.objects.all()

    return render(request, 'index.html', {'cars': cars})


def add_car(request):
    if request.method == "POST":
        brand = request.POST.get("car_brand")
        date = request.POST.get("car_date")
        color = request.POST.get("car_color")
        mileage = request.POST.get("car_mileage")
        price = request.POST.get("car_price")

        if brand:
            print(brand, date, color, mileage, price)
            Car.objects.create(brand=brand,
                               date=date,
                               color=color,
                               mileage=mileage,
                               price=price)

    return render(request, 'addCar.html')
