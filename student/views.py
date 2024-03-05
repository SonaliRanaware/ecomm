from django.shortcuts import render,HttpResponse,redirect
from .models import stud
# Create your views here.
def create(request):
    if request.method=='POST':
          n=request.POST['uname']
          mail=request.POST['uemail']
          mob=request.POST['mobile']
          msg=request.POST['msg']

          m=stud.objects.create(name=n,email=mail,mobile=mob,msg=msg)
          m.save()
          #return HttpResponse("data fetched successfully.....")
          return redirect("/dashboard")
    else:
         print("request is :",request.method)
         return render(request,'index.html')
def dashboard(request):
     m=stud.objects.all()
     context={}
     context['data']=m
     return render(request,'dashboard.html',context)
def delete(request,rid):
    #delete from tablename where id=?
    m=stud.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/dashboard')
def edit(request,rid):
     if request.method=='GET':
      m=stud.objects.get(id=rid)  #get
      print(m)
      context={}
      context['data']=m
      return render (request,'edit.html',context)
     else:
         upname=request.POST['uname']
         upemail=request.POST['uemail']
         upmob=request.POST['mobile']
         upmsg=request.POST['msg']
         #update stud set name=? ,mob=? ,msg=?  where id=?;
         m=stud.objects.filter(id=rid)
         m.update(name=upname,email=upemail,mobile=upmob,msg=upmsg)
 
         return redirect('/dashboard')

     