from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Credito, Pagamento
from .pagbank import criar_pagamento

@login_required
def processar_pagamento(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        resposta = criar_pagamento(valor, request.user.email)
        if resposta['status'] == 'sucesso':
            # Crie o pagamento no banco de dados
            Pagamento.objects.create(usuario=request.user, valor=valor, id_transacao=resposta['id_transacao'])
            # Credite o valor na conta do usuário
            Credito.objects.create(usuario=request.user, valor=valor)
            return redirect('pagina_sucesso')  # Redirecione para uma página de sucesso
    return render(request, 'processar_pagamento.html')
