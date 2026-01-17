from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView


# class CarsView(View):
# #classe Based View, view que herda propriedades de View.

#     #função executada após a propriedade dispatch() ser executada e reconhecer um metodo get
#     def get(self, request):
#         #a variavel cars são todos os objetos cars do banco de dados ordenados por Model
#         cars = Car.objects.all().order_by('model')
#         #serch usa o metodo get para pegar o input
#         search = request.GET.get('search')
#         #se o search for usado, ele faz uma busca no banco de dados pelo input
#         if search:
#             cars = Car.objects.filter(model__icontains = search).order_by('model')
#         #função que renderiza a view 
#         return render(
#             request, 
#             #pagina html onde essa view sera renderizada
#             'cars.html',
#             {'cars': cars}
        
#         )
    
class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        #eu uso super para poder pegar o objeto da classe mãe, car
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
    




# class NewCarView(View):
    
#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, "new_car.html", {'new_car_form': new_car_form})
    
#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, "new_car.html", {'new_car_form': new_car_form})
    

class NewCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'