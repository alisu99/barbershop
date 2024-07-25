document.addEventListener('DOMContentLoaded', function () {
    const cardsServico = document.querySelectorAll('.servico .card-personalizado');
    const cardsProfissional = document.querySelectorAll('.profissional .card-personalizado');
    const cardsDia = document.querySelectorAll('.dia .card-personalizado');
    let cardsHora; // Inicialmente vazio, será preenchido ao carregar horários disponíveis

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
                    carregarHorariosDisponiveis(estadoSelecionado.profissional.nome, estadoSelecionado.dia);
                }
            });
        });
    }

    function carregarHorariosDisponiveis(profissionalNome, dia) {
        fetch(`/horarios_disponiveis/?profissional_nome=${profissionalNome}&data=${dia}`)
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
                cardsHora = document.querySelectorAll('.hora .card-personalizado');
                selecionarItem(cardsHora, '.agendamento', 'hora');
            });
    }

    function atualizarResumo() {
        const servicoIdElement = document.getElementById('servico_id');
        const profissionalIdElement = document.getElementById('profissional_id');
        const horarioIdElement = document.getElementById('horario_id');
        const dataElement = document.getElementById('data');

        if (servicoIdElement && profissionalIdElement && horarioIdElement && dataElement) {
            servicoIdElement.value = estadoSelecionado.servico.id;
            profissionalIdElement.value = estadoSelecionado.profissional.id;
            horarioIdElement.value = estadoSelecionado.hora.id;
            dataElement.value = estadoSelecionado.dia;

            document.getElementById('selected-servico').textContent = estadoSelecionado.servico.nome;
            document.getElementById('selected-data').textContent = estadoSelecionado.dia;
            document.getElementById('selected-profissional').textContent = estadoSelecionado.profissional.nome;
            document.getElementById('selected-hora').textContent = estadoSelecionado.hora.horario;
        } else {
            console.error("Elementos não encontrados");
        }
    }

    selecionarItem(cardsServico, '.profissional', 'servico');
    selecionarItem(cardsProfissional, '.dia', 'profissional');
    selecionarItem(cardsDia, '.hora', 'dia');
});
