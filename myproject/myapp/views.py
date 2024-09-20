from django.shortcuts import redirect, render

from myapp.models import Produto


def home(request):
    # Obtém todos os produtos do banco de dados
    produtos_list = Produto.objects.all()  # Corrigido para usar o modelo Produto
    return render(request, "globals/home.html", {"produtos": produtos_list})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco')
        
        if nome and quantidade and preco:
            # Cria um novo produto usando o modelo Produto
            Produto.objects.create(
                nome=nome,
                quantidade=quantidade,
                preco=preco
            )

    return render(request, 'globals/cadastro.html')

def deletar(request, id):
    Produto.objects.get(id=id).delete()
    
    return redirect(home)