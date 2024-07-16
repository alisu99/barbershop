var cardContainer = document.getElementById("cardContainer");
var videoModal = document.getElementById("videoModal");
var backButton = document.getElementById("backButton");
var iframe1 = document.getElementById("iframe1");
var imageModal = document.getElementById("imageModal");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];

var opcoes = [
  { id: "opcao1" , texto: "GESTÃO DO CURSO", descricao: "GESTÃO DO CURSO", imagem: "assets/img/Jornada-do-aluno/conheça a malta.png", cards: [

  ] 
  },

  {
    id: "opcao2", texto: "COORDENAÇÃO", descricao: "COORDENAÇÃO", imagem: "assets/img/Jornada-do-aluno/graduação.png", cards: [
    ]
  },

  { id: "opcao3" , texto: "NDE", descricao: "NDE", imagem: "assets/img/Jornada-do-aluno/conheça a malta.png", cards: [

  ] 
  },

];

gestao_do_curso = [
{
    id: "gestao_do_curso1", texto: "GESTÃO DO CURSO", descricao: "GESTÃO DO CURSO", imagem: "assets/img/gestao-de-cursos/MALTA-FLUXO-DE-DECISOES-DA-GESTAO-DO-CURSO.png" , texto1: "Documentos do Curso", link1: "assets/pdf/institucional/PDI_FACULDADE-MALTA.pdf", link2: "#" },
];

coordenacao = [
{
    id: "coordenacao1", texto: "COORDENAÇÃO", descricao: "COORDENAÇÃO", imagem: "" , texto1: "Documentos do Curso" },
];

nde = [
{
    id: "nde1", texto: "NDE", descricao: "NDE", imagem: "" , texto1: "Documentos do Curso" },
];

selecao = [
  {
    id: "selecao1", texto: "Como Emitir Declaração e Imposto de Renda", descricao: "Como Emitir Declaração e Imposto de Renda", imagem: "assets/img/Jornada-do-aluno/como emitir declaração de IR.png", videoLink: "https://www.youtube.com/embed/X7IVPwOGa4I?si=M_GPGMXRXUCU-aVW" },
  {
    id: "selecao2", texto: "Historico e Declaração", descricao: "Historico e Declaração", imagem: "assets/img/Jornada-do-aluno/historico e declaração.png", videoLink: "https://www.youtube.com/embed/vpP32WUbR4U?si=wa9zRyrkiZf1QRRK" },
  {
    id: "selecao3", texto: "Secretaria", descricao: "Secretaria", imagem: "assets/img/Jornada-do-aluno/secretaria.png", videoLink: "https://www.youtube.com/embed/p9mIJq_zm0g?si=mkK48O-4CXp-tdfm" },
  { 
    id: "selecao12", texto: "Tutoria", descricao: "Tutoria", imagem: "assets/img/Jornada-do-aluno/tutoria.png", videoLink: "https://www.youtube.com/embed/YPC4qnUhluE?si=c6TH9e_xRNp3I2lx" },
  // Adicione mais seleções conforme necessário
];

function createOptions() {
  opcoes.forEach(function (opcao) {
    var cardElement = document.createElement("div");
    cardElement.classList.add("card");
    // cardElement.style.width = "18rem";
    cardElement.innerHTML = `
      <a href="${opcao.texto}">
        <img src="${opcao.imagem}" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">${opcao.descricao}</h5>
        </div>
      </a>
    `;

    cardContainer.appendChild(cardElement);


    cardElement.querySelector("a").addEventListener("click", function (event) {
      event.preventDefault();
        if (opcao.id === "opcao1") {
        // Limpa o cardContainer
        cardContainer.innerHTML = '';

        // Cria e adiciona os novos cards de seleção ao cardContainer
        gestao_do_curso.forEach(function (item) {
          var gestao_do_cursoCardElement = document.createElement("div");
          gestao_do_cursoCardElement.classList.add("card", "animate-left"); // Adiciona a classe de animação
          gestao_do_cursoCardElement.style.width = "40rem";

          gestao_do_cursoCardElement.innerHTML = `
            <h1">${item.texto}</h1>
            <img src="${item.imagem}" class="card-img-top">
            <div class="card-body"">
                <h5 class="card-title">${item.texto1}</h5>
            <a href="${item.link1}">PDI - Faculdade Malta</a>
            </div>
          `;
          cardContainer.appendChild(gestao_do_cursoCardElement);
          backButton.style.display = "block";
        });
      } else if (opcao.id === "opcao2") {
        // Limpa o cardContainer
        cardContainer.innerHTML = '';

        // Cria e adiciona os novos cards de seleção ao cardContainer
        coordenacao.forEach(function (item) {
          var coordenacaoCardElement = document.createElement("div");
          coordenacaoCardElement.classList.add("animate-left"); // Adiciona a classe de animação
          // coordenacaoCardElement.style.width = "18rem";
          coordenacaoCardElement.innerHTML = `
            <h1">${item.texto}</h1>
            <img src="${item.imagem}" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">${item.descricao}</h5>
            </div>
          `;
          cardContainer.appendChild(coordenacaoCardElement);
          backButton.style.display = "block";
        });
    } else if (opcao.id === "opcao3") {
        // Limpa o cardContainer
        cardContainer.innerHTML = '';

        // Cria e adiciona os novos cards de seleção ao cardContainer
        nde.forEach(function (item) {
          var ndeCardElement = document.createElement("div");
          ndeCardElement.classList.add("card", "animate-left"); // Adiciona a classe de animação
          // ndeCardElement.style.width = "18rem";
          ndeCardElement.innerHTML = `
            <h1">${item.texto}</h1>
            <h2></h2>
            <a href="assets/pdf/nde/MALTA-REGULAMENTO-DO-NDE.pdf">REGULAMENTO - NDE</a>
            <li style="list-style-type: none;" class="nav-item dropdown">
                <button style="height: 2.5rem; width: 13rem;" type="button" class="btn btn-light dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                    ATAS DE REUINÃO - NDE
                </button>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-01-NDE-2021.1.pdf">ATA-01-NDE-2021.1</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-01-NDE-2022.1.pdf">ATA-01-NDE-2022.1</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-01-NDE-2023.1.pdf">ATA-01-NDE-2023.1</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-001.2024.1.pdf">ATA-001.2024.1</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-02-NDE-2022.1.pdf">ATA-02-NDE-2022.1</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-02-NDE-2023.1.pdf">ATA-02-NDE-2023.1</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" target="_blank" href="assets/pdf/nde/ATA-03-NDE-2021.2.pdf">ATA-03-NDE-2021.2</a></li>
                </ul>
            </li>
            <div class="card-body">
                <h5 class="card-title">${item.descricao}</h5>
            </div>
          `;
          cardContainer.appendChild(ndeCardElement);
          backButton.style.display = "block";
        });
    }});
})};

// Chame a função para criar as opções
createOptions();

// Botão Voltar
backButton.addEventListener("click", function () {
  // Limpa o cardContainer
  cardContainer.innerHTML = '';

  // Recria as opções
  createOptions();

  // Esconda o botão Voltar
  backButton.style.display = "none";
});

// Fecha o modal quando o usuário clica fora dele
window.onclick = function (event) {
  if (event.target == videoModal) {
    videoModal.style.display = "none";
  }
  if (event.target == imageModal) {
    imageModal.style.display = "none";
  }
}

// Fecha o modal de imagem quando o usuário clica no "X"
span.onclick = function () {
  imageModal.style.display = "none";
}

// Simula um atraso no carregamento para mostrar o loader
window.addEventListener('load', function () {
  // Adiciona um atraso de 1.5 segundos antes de remover o loader e exibir o conteúdo
  setTimeout(function () {
    document.getElementById('loader').style.display = 'none';
    // document.getElementById('content').style.display = 'block';
  }, 2800);
});
