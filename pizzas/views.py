from email.mime import image 
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Pizza, Topping, Comment

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    
    context = {'all_pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    comments = Comment.objects.order_by('-date_added')
    image = Pizza.image
    
    context = {'pizza':p,'toppings':toppings,'comments':comments,'image':image}
    return render(request, 'pizzas/pizza.html', context)
    
def comment(request,pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = p
            comment.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form,'pizza':p}
    return render(request, 'pizzas/comment.html',context)