from django.shortcuts import render,get_object_or_404
from.forms import Students
from.models import User
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import UpdateView






# Create your views here.
def add(request):
    if request.method=='POST':
        fm=Students(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('add')


    else:
        fm=Students()
    std=User.objects.all()
    return render(request,'add.html',{'formss':fm,'std':std})


class DeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        User.objects.filter(id=id).delete()
        messages.success(request,"deleted successfully")
        return redirect("add")

class UpdateView(UpdateView):
    model=User
    form_class=Students
    template_name="update.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("add")

    def form_valid(self, form):
        messages.success(self.request,"updated successfully")
        return super().form_valid(form)

