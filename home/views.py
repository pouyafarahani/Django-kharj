from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from .models import costsModel
from .forms import costsForms


class HomeView(View):
    form = costsForms

    def get(self, request):
        if request.user.is_authenticated:
            costs = costsModel.objects.all()
            return render(request, 'home/home.html', {'form': self.form(), 'costs': costs})
        return render(request, 'home/home.html', {'form': self.form()})

    def post(self, request):
        if request.user.is_authenticated:
            form = self.form(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'ezafe shoooood ')
                return redirect('home:home')
            else:
                messages.warning(request, 'etelaati ke ersal kardi dorost nabod :(')
        else:
            messages.warning(request, 'shoma bayad vared shode bashid.')
        return redirect('home:home')
