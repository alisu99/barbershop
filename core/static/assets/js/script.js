document.addEventListener('DOMContentLoaded', function () {
    const cardsServico = document.querySelectorAll('.servico .card-personalizado');
    const cardsDia = document.querySelectorAll('.dia .card-personalizado');
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
            carregarProfissionais();
            rolarParaProximo('.profissional');
            exibirBloco('.profissional');
            ocultarBloco('.hora');
            ocultarBloco('.agendamento');
            atualizarResumo();
        });
    });

    formAgendamento.addEventListener('submit', function (event) {
        event.preventDefault();

        const nome = document.querySelector('.form-nome').value;
        const telefone = document.querySelector('.form-tel').value;
        const email = document.querySelector('.form-email').value;

        fetch('/agendar/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({
                servico: estadoSelecionado.servico,
                data: estadoSelecionado.data,
                profissional: estadoSelecionado.profissional,
                horario: estadoSelecionado.horario,
                nome_cliente: nome,
                telefone_cliente: telefone,
                email_cliente: email
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
        });
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

    function carregarProfissionais() {
        const data = estadoSelecionado.data;

        fetch(`/verificar_profissionais/?data=${data}`)
            .then(response => response.json())
            .then(profissionais => {
                const profissionaisContainer = document.querySelector('.selecione-o-profissional');
                profissionaisContainer.innerHTML = '';

                profissionais.forEach(profissional => {
                    const card = document.createElement('div');
                    card.className = 'card-personalizado';
                    card.innerHTML = `<img src="static/assets/img/usuario.png" alt=""><p>${profissional.nome}</p>`;
                    card.addEventListener('click', function () {
                        selecionarItem(card, '.selecione-o-profissional .card-personalizado');
                        atualizarEstadoSelecionado('profissional', profissional.id);
                        carregarHorarios();
                        rolarParaProximo('.hora');
                        exibirBloco('.hora');
                        ocultarBloco('.agendamento');
                        atualizarResumo();
                    });
                    profissionaisContainer.appendChild(card);
                });
            });
    }

    function carregarHorarios() {
        const profissional = estadoSelecionado.profissional;
        const data = estadoSelecionado.data;

        fetch(`/verificar_horarios/?profissional=${profissional}&data=${data}`)
            .then(response => response.json())
            .then(horarios => {
                const horariosContainer = document.querySelector('.selecione-o-horario');
                horariosContainer.innerHTML = '';

                horarios.forEach(horario => {
                    const card = document.createElement('div');
                    card.className = 'card-personalizado';
                    card.textContent = horario.horario;
                    card.addEventListener('click', function () {
                        selecionarItem(card, '.selecione-o-horario .card-personalizado');
                        atualizarEstadoSelecionado('horario', horario.id);
                        rolarParaProximo('.agendamento');
                        exibirBloco('.agendamento');
                        atualizarResumo();
                    });
                    horariosContainer.appendChild(card);
                });
            });
    }
});
