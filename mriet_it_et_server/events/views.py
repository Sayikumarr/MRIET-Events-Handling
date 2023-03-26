from django.shortcuts import redirect, render

from events.models import Student
from events.forms import StudentForm
from events.models import Payment
from django.contrib.auth.decorators import login_required

from events.models import Stu_Coordinator

# Create your views here.
def registerEvent(request,roll=None):
    stu = None
    done = False
    if request.method == "GET":
        roll = request.GET.get('roll')
        try:
            stu = Student.objects.get(roll=roll)
        except Student.DoesNotExist:
            print("Not Exists")
    if request.method == "POST":
        # create object of form
        form = StudentForm(request.POST)
        
        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            roll = request.POST.get('roll')
            stu = Student.objects.get(roll=roll)
            done = True
        else:
            try:
                # name = request.POST.get('name')
                # father = request.POST.get('father')
                # college = request.POST.get('college')
                roll  = request.POST.get('roll')
                # branchNyear  = request.POST.get('branchNyear')
                # email = request.POST.get('email')
                # wanumber = request.POST.get('wanumber')
                paper = request.POST.get('paper')
                poster = request.POST.get('poster')
                codigo = request.POST.get('codigo')
                expo = request.POST.get('expo')
                quiz = request.POST.get('quiz')
                treasure = request.POST.get('treasure')
                short = request.POST.get('short')
                conn = request.POST.get('conn')
                circuit = request.POST.get('circuit')
                tinker = request.POST.get('tinker')
                logo = request.POST.get('logo')
                shark = request.POST.get('shark')
                stu = Student.objects.get(roll=roll)
                stu.paper = True if paper=='on' else False
                stu.poster = True if poster=='on' else False
                stu.codigo = True if codigo=='on' else False
                stu.expo = True if expo=='on' else False
                stu.quiz = True if quiz=='on' else False
                stu.treasure = True if treasure=='on' else False
                stu.short = True if short=='on' else False
                stu.conn = True if conn=='on' else False
                stu.circuit = True if circuit=='on' else False
                stu.tinker = True if tinker=='on' else False
                stu.logo = True if logo=='on' else False
                stu.shark = True if shark=='on' else False

                stu.save()
                done = True
            except Exception as e:
                print(e)
                pass
    if done:
        try:
            evnts = [stu.paper,stu.poster,stu.codigo,stu.expo,stu.quiz,stu.treasure,stu.conn,stu.circuit,stu.tinker,stu.short,stu.logo,stu.shark]
            total = evnts.count(True)*100
            pay = Payment()
            pay.student=stu
            pay.total = total
            pay.save()
        except Exception as e:
            print(e)
            pay = Payment.objects.get(student=stu)
            total = evnts.count(True)*100
            pay.total = total
            pay.save()
        return render(request,'paydetails.html',{'stu':stu,'pay':pay})
    return render(request,'register.html', {'stu':stu})

def getroll(request):
    stu = Stu_Coordinator.objects.all()
    # if request.method == "POST":
    #     roll = request.POST.get("roll")
    #     redirect.method = "GET"
    #     return registerEvent(request,roll)
    return render(request,'roll.html',{'stu':stu})


from django.db.models import Q

@login_required
def dashboard(request):
    if request.method == "POST":
        kw = request.POST.get('keyword')
        stu = Payment.objects.filter(Q(student__roll=kw) | Q(student__father=kw) | Q(student__college=kw) | Q(student__branchNyear=kw) | Q(student__email=kw))
    else:
        stu = Payment.objects.all()
    return render(request,'dashboard.html',{'stu':stu})

from django.db.models import F

@login_required
def paid(request):
    stu = Payment.objects.filter(paid=F('total'))
    return render(request,'dashboard.html',{'stu':stu})

@login_required
def unpaid(request):
    stu = Payment.objects.filter(paid=0)
    return render(request,'dashboard.html',{'stu':stu})

@login_required
def pending(request):
    stu = Payment.objects.exclude(paid=F('total'))
    return render(request,'dashboard.html',{'stu':stu})


@login_required
def done_payment(request,roll):
    stu = Student.objects.get(roll=roll)
    pay = Payment.objects.get(student=stu)
    evnts = [stu.paper,stu.poster,stu.codigo,stu.expo,stu.quiz,stu.treasure,stu.conn,stu.circuit,stu.tinker,stu.short,stu.logo,stu.shark]
    total = evnts.count(True)*100
    if request.method=="POST":
        amount = request.POST.get("paid")
        cashMode = request.POST.get("mode")
        pay.paid = amount
        pay.total = total
        pay.cash = True if cashMode=="1" else False
        # coord = Stu_Coordinator(user=request.user)
        pay.verifiedBy = request.user.username
        pay.save()
        return redirect(dashboard)
    return render(request,'payment.html',{'pay':pay})

@login_required
def getDetails(request,roll):
    try:
        stu = Student.objects.get(roll=roll)
    except:
        return redirect(dashboard)
    if request.method=="POST":
                # name = request.POST.get('name')
                # father = request.POST.get('father')
                # college = request.POST.get('college')
                # roll  = request.POST.get('roll')
                # branchNyear  = request.POST.get('branchNyear')
                email = request.POST.get('email')
                wanumber = request.POST.get('wanumber')
                paper = request.POST.get('paper')
                poster = request.POST.get('poster')
                codigo = request.POST.get('codigo')
                expo = request.POST.get('expo')
                quiz = request.POST.get('quiz')
                treasure = request.POST.get('treasure')
                short = request.POST.get('short')
                conn = request.POST.get('conn')
                circuit = request.POST.get('circuit')
                tinker = request.POST.get('tinker')
                logo = request.POST.get('logo')
                shark = request.POST.get('shark')
                stu = Student.objects.get(roll=roll)
                # stu.name = name
                # stu.father = father
                # stu.college = college
                # stu.branchNyear = branchNyear
                stu.email = email
                stu.paper = True if paper=='on' else False
                stu.poster = True if poster=='on' else False
                stu.codigo = True if codigo=='on' else False
                stu.expo = True if expo=='on' else False
                stu.quiz = True if quiz=='on' else False
                stu.treasure = True if treasure=='on' else False
                stu.short = True if short=='on' else False
                stu.conn = True if conn=='on' else False
                stu.circuit = True if circuit=='on' else False
                stu.tinker = True if tinker=='on' else False
                stu.logo = True if logo=='on' else False
                stu.shark = True if shark=='on' else False
                stu.save()
                evnts = [stu.paper,stu.poster,stu.codigo,stu.expo,stu.quiz,stu.treasure,stu.conn,stu.circuit,stu.tinker,stu.short,stu.logo,stu.shark]
                total = evnts.count(True)*100
                pay = Payment.objects.get(student=stu)
                total = evnts.count(True)*100
                pay.total = total
                pay.save()
                return redirect(dashboard)
    return render(request,'detailView.html',{'stu':stu})

import csv
from django.http import HttpResponse

@login_required
def export_to_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # replace "Model" with the name of your model
    writer = csv.writer(response)
    writer.writerow(['Roll Number', 'Name', 'Father','College','Branch','Email','WhatsApp','Total','Paid','MODE(Cash)','Verified By']) # replace with your own fields

    queryset = Payment.objects.all() # replace "Model" with the name of your model
    for obj in queryset:
        writer.writerow([obj.student.roll, obj.student.name,obj.student.father, obj.student.college,obj.student.branchNyear, obj.student.email, obj.student.wanumber,obj.total,obj.paid,obj.cash,obj.verifiedBy]) # replace with your own fields

    return response


@login_required
def filter_data(request):
    if request.method == "POST":
        filt = request.POST.get('filter')
        if filt == "paper":
            stu = Payment.objects.filter(Q(student__paper=True))
        elif filt == 'poster':
            stu = Payment.objects.filter(Q(student__poster=True))
        elif filt == 'codigo':
            stu = Payment.objects.filter(Q(student__codigo=True))
        elif filt == 'expo':
            stu = Payment.objects.filter(Q(student__expo=True))
        elif filt == 'quiz':
            stu = Payment.objects.filter(Q(student__quiz=True))
        elif filt == 'treasure':
            stu = Payment.objects.filter(Q(student__treasure=True))
        elif filt == 'short':
            stu = Payment.objects.filter(Q(student__short=True))
        elif filt == 'conn':
            stu = Payment.objects.filter(Q(student__conn=True))
        elif filt == 'circuit':
            stu = Payment.objects.filter(Q(student__circuit=True))
        elif filt == 'tinker':
            stu = Payment.objects.filter(Q(student__tinker=True))
        elif filt == 'logo':
            stu = Payment.objects.filter(Q(student__logo=True))
        elif filt == 'shark':
            stu = Payment.objects.filter(Q(student__shark=True))
        return render(request,'dashboard.html',{'stu':stu})
    return render(request,'filter.html')

@login_required
def overallpaymentDetails(request):
    payments = Payment.objects.all()
    paid=total=0
    for pay in payments:
        total+=pay.total
        paid+=pay.paid
    due=total-paid
    return render(request,'overallpay.html',{'total':total,'paid':paid,'due':due})