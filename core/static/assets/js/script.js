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
            });
        });
    }

    function atualizarResumo() {
        document.getElementById('selected-servico').textContent = estadoSelecionado.servico;
        document.getElementById('selected-data').textContent = estadoSelecionado.dia;
        document.getElementById('selected-profissional').textContent = estadoSelecionado.profissional;
        document.getElementById('selected-hora').textContent = estadoSelecionado.hora;
    }

    selecionarItem(cardsServico, '.profissional', 'servico');
    selecionarItem(cardsProfissional, '.dia', 'profissional');
    selecionarItem(cardsDia, '.hora', 'dia');
    selecionarItem(cardsHora, '.agendamento', 'hora');
});