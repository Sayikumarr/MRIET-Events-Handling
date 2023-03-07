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
                debugging = request.POST.get('debugging')
                expo = request.POST.get('expo')
                quiz = request.POST.get('quiz')
                treasure = request.POST.get('treasure')
                short = request.POST.get('short')
                conn = request.POST.get('conn')
                circuitrix = request.POST.get('circuitrix')
                tinker = request.POST.get('tinker')
                stu = Student.objects.get(roll=roll)
                stu.paper = True if paper=='on' else False
                stu.poster = True if poster=='on' else False
                stu.debugging = True if debugging=='on' else False
                stu.expo = True if expo=='on' else False
                stu.quiz = True if quiz=='on' else False
                stu.treasure = True if treasure=='on' else False
                stu.short = True if short=='on' else False
                stu.conn = True if conn=='on' else False
                stu.circuit = True if circuitrix=='on' else False
                stu.tinker = True if tinker=='on' else False

                stu.save()
                done = True
            except Exception as e:
                print(e)
                pass
    if done:
        try:
            evnts = [stu.paper,stu.poster,stu.debugging,stu.expo,stu.quiz,stu.treasure,stu.conn,stu.circuit,stu.tinker]
            total = evnts.count(True)*50
            pay = Payment()
            pay.student=stu
            pay.total = total
            pay.save()
        except Exception as e:
            print(e)
            pay = Payment.objects.get(student=stu)
            total = evnts.count(True)*50
            pay.total = total
            pay.save()
        return render(request,'paydetails.html',{'stu':stu,'pay':pay})
    return render(request,'register.html', {'stu':stu})

def getroll(request):
    # if request.method == "POST":
    #     roll = request.POST.get("roll")
    #     redirect.method = "GET"
    #     return registerEvent(request,roll)
    return render(request,'roll.html')


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
    if request.method=="POST":
        amount = request.POST.get("paid")
        cashMode = request.POST.get("mode")
        pay.paid = amount
        pay.cash = True if cashMode=="1" else False
        coord = Stu_Coordinator(user=request.user)
        pay.verifiedBy = coord.rollno
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
                debugging = request.POST.get('debugging')
                expo = request.POST.get('expo')
                quiz = request.POST.get('quiz')
                treasure = request.POST.get('treasure')
                short = request.POST.get('short')
                conn = request.POST.get('conn')
                circuitrix = request.POST.get('circuitrix')
                tinker = request.POST.get('tinker')
                stu = Student.objects.get(roll=roll)
                # stu.name = name
                # stu.father = father
                # stu.college = college
                # stu.branchNyear = branchNyear
                stu.email = email
                stu.paper = True if paper=='on' else False
                stu.poster = True if poster=='on' else False
                stu.debugging = True if debugging=='on' else False
                stu.expo = True if expo=='on' else False
                stu.quiz = True if quiz=='on' else False
                stu.treasure = True if treasure=='on' else False
                stu.short = True if short=='on' else False
                stu.conn = True if conn=='on' else False
                stu.circuit = True if circuitrix=='on' else False
                stu.tinker = True if tinker=='on' else False
                stu.save()
                evnts = [stu.paper,stu.poster,stu.debugging,stu.expo,stu.quiz,stu.treasure,stu.conn,stu.circuit,stu.tinker]
                total = evnts.count(True)*50
                pay = Payment.objects.get(student=stu)
                total = evnts.count(True)*50
                pay.total = total
                pay.save()
                return redirect(dashboard)
    return render(request,'detailView.html',{'stu':stu})