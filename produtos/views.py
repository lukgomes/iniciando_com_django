from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def cadastrar(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        produtos = Produto.objects.all()
        return render(request, 'cadastrar.html', {'status': status, 'produtos': produtos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        if float(preco) <= 0:
            return redirect('/produtos/cadastro/?status=0')
        
        produto = Produto(
            nome = nome,
            preco = preco
        )
        produto.save()

        return redirect('/produtos/cadastro/?status=1')
    
def excluir(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()

    return redirect('cadastrar')

def visualizar(request):
    return HttpResponse('Estou no visualizar')