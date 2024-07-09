document.addEventListener('DOMContentLoaded', function () {
    const cardsServico = document.querySelectorAll('.servico .card-personalizado');
    const cardsProfissional = document.querySelectorAll('.profissional .card-personalizado');
    const cardsDia = document.querySelectorAll('.dia .card-personalizado');
    const cardsHora = document.querySelectorAll('.hora .card-personalizado');

    let estadoSelecionado = {
        servico: { id: '', nome: '' },
        dia: '',
        profissional: { id: '', nome: '' },
        hora: { id: '', horario: '' }
    };

    function selecionarItem(cards, proximoBloco, categoria) {
        cards.forEach(card => {
            card.addEventListener('click', function () {
                cards.forEach(card => card.classList.remove('selecionado'));
                card.classList.add('selecionado');
                
                if (categoria === 'servico') {
                    estadoSelecionado.servico.id = card.getAttribute('data-servico-id');
                    estadoSelecionado.servico.nome = card.getAttribute('data-servico-nome');
                } else if (categoria === 'profissional') {
                    estadoSelecionado.profissional.id = card.getAttribute('data-profissional-id');
                    estadoSelecionado.profissional.nome = card.getAttribute('data-profissional-nome');
                } else if (categoria === 'dia') {
                    estadoSelecionado.dia = card.getAttribute('data-dia');
                } else if (categoria === 'hora') {
                    estadoSelecionado.hora.id = card.getAttribute('data-hora-id');
                    estadoSelecionado.hora.horario = card.getAttribute('data-hora-horario');
                }

                document.querySelector(proximoBloco).style.display = 'block';
                document.querySelector(proximoBloco).scrollIntoView({ behavior: 'smooth', block: 'start' });
                atualizarResumo();

                if (categoria === 'dia') {
                    carregarHorariosDisponiveis(estadoSelecionado.profissional.id, estadoSelecionado.dia);
                }
            });
        });
    }

    function carregarHorariosDisponiveis(profissionalId, dia) {
        fetch(`/horarios_disponiveis/?profissional_id=${profissionalId}&data=${dia}`)
            .then(response => response.json())
            .then(data => {
                const horariosContainer = document.querySelector('.hora .selecione-o-horario');
                horariosContainer.innerHTML = '';
                data.horarios.forEach(horario => {
                    const div = document.createElement('div');
                    div.classList.add('card-personalizado');
                    div.setAttribute('data-hora-id', horario.id);
                    div.setAttribute('data-hora-horario', horario.horario);
                    div.textContent = horario.horario;
                    horariosContainer.appendChild(div);
                });
                selecionarItem(document.querySelectorAll('.hora .card-personalizado'), '.agendamento', 'hora');
            });
    }

    function atualizarResumo() {
        document.getElementById('selected-servico').textContent = estadoSelecionado.servico.nome;
        document.getElementById('selected-data').textContent = estadoSelecionado.dia;
        document.getElementById('selected-profissional').textContent = estadoSelecionado.profissional.nome;
        document.getElementById('selected-hora').textContent = estadoSelecionado.hora.horario;

        // Atualizar os campos ocultos do formulário
        document.getElementById('servico_id').value = estadoSelecionado.servico.id;
        document.getElementById('profissional_id').value = estadoSelecionado.profissional.id;
        document.getElementById('horario_id').value = estadoSelecionado.hora.id;
        document.getElementById('data').value = estadoSelecionado.dia;
    }

    selecionarItem(cardsServico, '.profissional', 'servico');
    selecionarItem(cardsProfissional, '.dia', 'profissional');
    selecionarItem(cardsDia, '.hora', 'dia');
});