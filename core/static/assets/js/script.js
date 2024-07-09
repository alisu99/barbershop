document.addEventListener('DOMContentLoaded', function () {
    const cardsServico = document.querySelectorAll('.servico .card-personalizado');
    const cardsProfissional = document.querySelectorAll('.profissional .card-personalizado');
    const cardsDia = document.querySelectorAll('.dia .card-personalizado');
    const cardsHora = document.querySelectorAll('.hora .card-personalizado');

    let estadoSelecionado = {
        servico: '',
        dia: '',
        profissional: '',
        hora: ''
    };

    function selecionarItem(cards, proximoBloco, categoria) {
        cards.forEach(card => {
            card.addEventListener('click', function () {
                cards.forEach(card => card.classList.remove('selecionado'));
                card.classList.add('selecionado');
                estadoSelecionado[categoria] = card.getAttribute(`data-${categoria}`);
                document.querySelector(proximoBloco).style.display = 'block';
                document.querySelector(proximoBloco).scrollIntoView({ behavior: 'smooth', block: 'start' });
                atualizarResumo();

                if (categoria === 'dia') {
                    carregarHorariosDisponiveis(estadoSelecionado.profissional, estadoSelecionado.dia);
                }
            });
        });
    }

    function carregarHorariosDisponiveis(profissional, dia) {
        fetch(`/horarios_disponiveis/?profissional_id=${profissional}&data=${dia}`)
            .then(response => response.json())
            .then(data => {
                const horariosContainer = document.querySelector('.hora .selecione-o-horario');
                horariosContainer.innerHTML = '';
                data.horarios.forEach(horario => {
                    const div = document.createElement('div');
                    div.classList.add('card-personalizado');
                    div.setAttribute('data-hora', horario.id);
                    div.textContent = horario.horario;
                    horariosContainer.appendChild(div);
                });
                selecionarItem(document.querySelectorAll('.hora .card-personalizado'), '.agendamento', 'hora');
            });
    }

    function atualizarResumo() {
        document.getElementById('selected-servico').textContent = estadoSelecionado.servico;
        document.getElementById('selected-data').textContent = estadoSelecionado.dia;
        document.getElementById('selected-profissional').textContent = estadoSelecionado.profissional;
        document.getElementById('selected-hora').textContent = estadoSelecionado.hora;

        // Atualizar os campos ocultos do formulário
        document.getElementById('servico_id').value = estadoSelecionado.servico;
        document.getElementById('profissional_id').value = estadoSelecionado.profissional;
        document.getElementById('horario_id').value = estadoSelecionado.hora;
        document.getElementById('data').value = estadoSelecionado.dia;
    }

    selecionarItem(cardsServico, '.profissional', 'servico');
    selecionarItem(cardsProfissional, '.dia', 'profissional');
    selecionarItem(cardsDia, '.hora', 'dia');
});