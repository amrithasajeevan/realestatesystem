
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django .views import generic
from .models import *
from .forms import *

# Create your views here

#admin register

class Adminregister(generic.CreateView):
    form_class = AdminRegForm
    template_name = 'adminregister.html'
    success_url = reverse_lazy('admin_login')

#admin login

class AdminLogin(generic.View):
    form_class=AdminLoginForm
    template_name='admin_login.html'
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        if request.method=='POST':
            a=AdminLoginForm(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=adminuser.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse('login success')
                else:
                    return HttpResponse('login failed')
            return HttpResponse('invalid credentials')


#propertylist cretion by admin
class  PropertyAddView(generic.CreateView):
    form_class=PropertyForm
    template_name='property.html'
    success_url=reverse_lazy('propertydisp')

#view all properities by admin
class PropertyListView(generic.ListView):
    model = propertydetail
    template_name = 'propertydisplay.html'
    context_object_name = 'propertylist'

#tenent registraion

class TenentReg(generic.CreateView):
    form_class = TenentRegForm
    template_name = 'tenentregister.html'
    success_url = reverse_lazy('tenent_login')

#tenent login
class TenentLogin(generic.View):
    form_class = TenentLoginForm
    template_name = 'tenent_login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            ps = form.cleaned_data['password']
            b = tenentreg.objects.all()
            for i in b:
                    if name==i.name and ps==i.password:
                        request.session['u_id'] = i.id
                        return redirect('http://127.0.0.1:8000/realestateapp/propertyview/')
            else:
                return HttpResponse('login failed')
        return HttpResponse('invalid credentials')

#tenent property view

class Tenent_PropertyView(generic.ListView):
    model = propertydetail
    template_name = 'tenent_property_view.html'
    context_object_name = 'data'


#tenent request
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

class SendRequestToLandlordView(generic.View):
    def post(self, request, tenant_id, property_interest_id):
        tenant = get_object_or_404(tenentreg, pk=tenant_id)
        property_interest = get_object_or_404(propertydetail, pk=property_interest_id)

        message = request.POST.get('message', '')

        if not message:
            return JsonResponse({'status': 'error', 'message': 'Message cannot be empty'})

        try:
            tenant_request = TenantRequest.objects.create(
                tenant=tenant,
                property_interest=property_interest,
                message=message
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})