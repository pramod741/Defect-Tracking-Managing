from django.shortcuts import render, redirect
from .models import DefectDetails, Testers, Defect_Screen_Shots
from django.contrib.auth.decorators import login_required
from defects.forms import DefectEditForm, AddDefect, FilterDevelopers
from django.core.paginator import Paginator
from .models import Developers, DefectDetails
from django.contrib.auth.models import User
from defects.utils import send_mail_view

# Create your views here.

@login_required(login_url='login')
def all_defects(request):
    defects = DefectDetails.objects.all()
    defects_count = len(defects)
    tester = Testers.objects.all()
    paginator = Paginator(defects, 3)
    page_num = request.GET.get('pg')
    # pages = paginator.get_page(page_num)
    defects = paginator.get_page(page_num)

    #logged in user Details
    show_button = False
    user = request.user
    # print(user)
    try:
        tester = Testers.objects.get(tester_name=user)
        if tester.is_admin:
            show_button = True
    except Testers.DoesNotExist:
        pass

    context = {
        'defects': defects,
        'tester': tester,
        'defects_count': defects_count,
        'show_button': show_button
        # 'pages': pages
    }
    return render(request, 'defects/alldefects.html', context)

@login_required(login_url='login')
def description_list(request, id=0):
    defects = DefectDetails.objects.get(id=id)
    screenshots = Defect_Screen_Shots.objects.filter(defect = defects)
    context = {
        'defects': defects,
        'screenshots': screenshots
        }
    return render(request, 'defects/description.html', context)


@login_required(login_url='login')
def edit_defects(request, id=0):
    defect = DefectDetails.objects.get(id=id)
    if request.method == 'POST':
        form = DefectEditForm(request.POST, instance=defect)
        if form.is_valid():
            form.save()
            return redirect('defects')
    else:
        form = DefectEditForm(instance=defect)
    return render(request, "defects/edit_defect.html", {'form': form})


@login_required(login_url='login')
def add_defect(request):
    if request.method == 'POST':
        form = AddDefect(request.POST)
        if form.is_valid():
            dev = form.cleaned_data['assigned_to']
            user = User.objects.get(username=dev)
            # print(dev)
            # print(user.email)
            form.save()
            send_mail_view(user.email)
            return redirect('defects')
    else:
        form = AddDefect()
    return render(request, 'defects/add_defect.html', {'form': form})

@login_required(login_url='login')
def filter_data(request):
    developers = Developers.objects.all()
    defects = []
    if request.method == 'POST':
        name = request.POST['devname']
        name = User.objects.get(username=name)

        # user_name = request.POST['id']
        print(name)
        try:
            dev = Developers.objects.get(dev_name=name)
            defects = DefectDetails.objects.filter(assigned_to=dev)
            print(defects)
        except Developers.DoesNotExist:
            pass
        except DefectDetails.DoesNotExist:
            pass
    context = {
        'developers': developers,
        'defects': defects,
        }
    return render(request, 'defects/filter.html', context)


'''def filter_dev_data(request):
    if request.methos == 'POST':
        form = FilterDevelopers(request.POST)
        if form.is_valid():
            name = form.cleaned_data['assigned_to']
            name = User.objects.get(username = name)
            devname = Developers.objects.get(dev_name=name)
            defects = DefectDetails.objects.filter(assigned_to=devname)
    else:
        form = FilterDevelopers()'''