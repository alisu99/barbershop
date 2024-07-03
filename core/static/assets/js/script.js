document.addEventListener('DOMContentLoaded', function () {
    const cardsServico = document.querySelectorAll('.servico .card-personalizado');
    const cardsDia = document.querySelectorAll('.dia .card-personalizado');
    const cardsProfissional = document.querySelectorAll('.profissional .card-personalizado');
    const cardsHorario = document.querySelectorAll('.hora .card-personalizado');
    const formAgendamento = document.querySelector('.form-agendamento');

    let estadoSelecionado = {
        servico: '',
        data: '',
        profissional: '',
        horario: ''
    };

    cardsServico.forEach(card => {
        card.addEventListener('click', function () {
            selecionarItem(card, '.cards-servico .card-personalizado');
            atualizarEstadoSelecionado('servico', card.nextElementSibling.querySelector('h5').textContent.trim());
            rolarParaProximo('.dia');
            exibirBloco('.dia');
            ocultarBloco('.profissional');
            ocultarBloco('.hora');
            ocultarBloco('.agendamento');
            atualizarResumo();
        });
    });

    cardsDia.forEach(card => {
        card.addEventListener('click', function () {
            selecionarItem(card, '.selecione-o-dia .card-personalizado');
            atualizarEstadoSelecionado('data', card.textContent.trim());
            rolarParaProximo('.profissional');
            exibirBloco('.profissional');
            ocultarBloco('.hora');
            ocultarBloco('.agendamento');
            atualizarResumo();
        });
    });

    cardsProfissional.forEach(card => {
        card.addEventListener('click', function () {
            selecionarItem(card, '.selecione-o-profissional .card-personalizado');
            atualizarEstadoSelecionado('profissional', card.querySelector('p').textContent.trim());
            rolarParaProximo('.hora');
            exibirBloco('.hora');
            ocultarBloco('.agendamento');
            atualizarResumo();
        });
    });

    cardsHorario.forEach(card => {
        card.addEventListener('click', function () {
            selecionarItem(card, '.selecione-o-horario .card-personalizado');
            atualizarEstadoSelecionado('horario', card.textContent.trim());
            rolarParaProximo('.agendamento');
            exibirBloco('.agendamento');
            atualizarResumo();
        });
    });

    formAgendamento.addEventListener('submit', function (event) {
        event.preventDefault();

        const nome = document.querySelector('.form-nome').value;
        const telefone = document.querySelector('.form-tel').value;

        console.log('Serviço:', estadoSelecionado.servico);
        console.log('Data:', estadoSelecionado.data);
        console.log('Profissional:', estadoSelecionado.profissional);
        console.log('Horário:', estadoSelecionado.horario);
        console.log('Nome:', nome);
        console.log('Telefone:', telefone);
    });

    function selecionarItem(elemento, selector) {
        const todosCards = document.querySelectorAll(selector);
        todosCards.forEach(card => {
            card.classList.remove('selecionado');
        });
        elemento.classList.add('selecionado');
    }

    function atualizarEstadoSelecionado(categoria, valor) {
        estadoSelecionado[categoria] = valor;
    }

    function atualizarResumo() {
        document.getElementById('selected-servico').textContent = estadoSelecionado.servico;
        document.getElementById('selected-data').textContent = estadoSelecionado.data;
        document.getElementById('selected-profissional').textContent = estadoSelecionado.profissional;
        document.getElementById('selected-hora').textContent = estadoSelecionado.horario;
    }

    function exibirBloco(seletor) {
        const bloco = document.querySelector(seletor);
        if (bloco) {
            bloco.style.display = 'block';
        }
    }

    function ocultarBloco(seletor) {
        const bloco = document.querySelector(seletor);
        if (bloco) {
            bloco.style.display = 'none';
        }
    }

    function rolarParaProximo(seletor) {
        const proximoBloco = document.querySelector(seletor);
        if (proximoBloco) {
            proximoBloco.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
});
