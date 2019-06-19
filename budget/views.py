from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import ExpenseItem, Leena
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, 'home.html', context)


@login_required
def addnew(request):
    context = {}
    return render(request, 'addnew.html', context)


@login_required
def profile(request):
    context = {}
    return render(request, 'profile.html', context)


@login_required
def viewall(request):
    context = {}
    return render(request, 'viewall.html', context)


class AddItemView(CreateView):
    queryset = ExpenseItem.objects.all()
    template_name = 'addnew.html'
    fields = ['title', 'description', 'amount', 'date', 'account', 'category']
    success_url = '/'


class ListItemView(ListView):
    queryset = ExpenseItem.objects.all()
    template_name = 'viewall.html'


class DetailItemView(DetailView):
    queryset = ExpenseItem.objects.all()
    # budget/expenseitem_detail.html


class UpdateItemView(UpdateView):
    queryset = ExpenseItem.objects.all()
    template_name = 'expense_update.html'
    fields = ['title', 'description', 'amount', 'date', 'account', 'category']

    # success_url = '/'

    def get_success_url(self):
        return '/view/' + str(self.object.id)


class DeleteItemView(DeleteView):
    queryset = ExpenseItem.objects.all()
    success_url = '/viewall'


@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Form validated')
            Leena.objects.create(name=request.POST.get('name'),query=request.POST.get('query'),email=request.POST.get('email'))
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
