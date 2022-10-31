from django.shortcuts import render, redirect

from exam_web_basics.web.forms import CrateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from exam_web_basics.web.models import Profile, Car


def profile_get():
    try:
        return Profile.objects.get()

    except:
        return None


def index(request):
    profile = profile_get()
    cars = Car.objects.all()

    context = {
        'profile': profile,
        'cars': cars,
        # 'profile_exists': profile_exists,
    }

    return render(request, 'index.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CrateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return redirect('index')
    else:
        form = CrateProfileForm()

    context = {'form': form}

    return render(request, 'profile-create.html', context)


def catalogue(request):
    cars = Car.objects.all()
    total_cars = len(cars)
    context = {
        'cars': cars,
        'total_cars': total_cars,
    }
    return render(request, 'catalogue.html', context)


def car_create(request):
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()

    context = {
        'form': form,
    }

    return render(request, 'car-create.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car,
    }

    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)

    context = {
        'form': form,

    }
    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'form': form,
    }
    return render(request, 'car-delete.html', context)


def profile_details(request):
    profile = profile_get()
    cars = Car.objects.all()
    total_price_count = sum(car.price for car in cars)

    context = {
        'profile': profile,
        'cars': cars,
        'total_price_count': total_price_count,

    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = profile_get()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = profile_get()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
