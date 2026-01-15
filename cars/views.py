from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View


class CarsView(View):
#classe Based View, view que herda propriedades de View.

    #função executada após a propriedade dispatch() ser executada e reconhecer um metodo get
    def get(self, request):
        #a variavel cars são todos os objetos cars do banco de dados ordenados por Model
        cars = Car.objects.all().order_by('model')
        #serch usa o metodo get para pegar o input
        search = request.GET.get('search')
        #se o search for usado, ele faz uma busca no banco de dados pelo input
        if search:
            cars = Car.objects.filter(model__icontains = search).order_by('model')
        #função que renderiza a view 
        return render(
            request, 
            #pagina html onde essa view sera renderizada
            'cars.html',
            {'cars': cars}
        
        )
#method fuction based views
# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render(request, 'new_car.html', {'new_car_form':new_car_form})

class NewCarView(View):
    
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, "new_car.html", {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, "new_car.html", {'new_car_form': new_car_form})
        
