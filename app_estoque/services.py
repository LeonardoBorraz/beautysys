from .models import Item_Estoque
from .forms import ItemEstoqueForm
from .exceptions import QuantidadeInsuficiente
from django.shortcuts import get_object_or_404

class EstoqueService:
    @staticmethod
    def obter_itens_estoque():
        return Item_Estoque.objects.all()

    @staticmethod
    def adicionar_item(nome, quantidade,custo_aquisicao, preco):
        Item_Estoque.objects.create(
            item=nome,
            quantidade=quantidade,
            custo_aquisicao=custo_aquisicao,
            preco = preco
            )
        
    @staticmethod
    def remover_item(request,pk, quantidade):
        item = get_object_or_404(Item_Estoque, pk=pk)
        if quantidade > item.quantidade:
            raise QuantidadeInsuficiente(
                f'Estoque insuficente, disponivel: {item.quantidade}'
            )
        else:
            item.quantidade -= quantidade
            if item.quantidade == 0:
                item.delete()
            else:
                item.save()


    @staticmethod
    def editar_item(pk, dados):
        item = get_object_or_404(Item_Estoque, pk=pk)
        form = ItemEstoqueForm(dados, instance=item)

        if form.is_valid():
            form.save()
            return True, None
        else:
            return False, form

