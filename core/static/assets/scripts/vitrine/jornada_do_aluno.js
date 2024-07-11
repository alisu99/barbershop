var cardContainer = document.getElementById("cardContainer");
var videoModal = document.getElementById("videoModal");
var backButton = document.getElementById("backButton");
var iframe1 = document.getElementById("iframe1");
var imageModal = document.getElementById("imageModal");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];

var opcoes = [
  { id: "opcao1", texto: "Conheça a Malta", descricao: "Conheça a Malta", imagem: "{% static '/assets/img/Jornada-do-aluno/conheça a malta.png' %}", videoLink: "https://www.youtube.com/embed/_wSmS9eh17E?si=v2hn_fAYSYVjV6Gu" },
  {
    id: "opcao2", texto: "Graduação", descricao: "GRADUAÇÃO", imagem: "{% static 'assets/img/Jornada-do-aluno/graduação.png' %}", cards: [
    ]
  }
];

selecao = [
  {
    id: "selecao1", texto: "Como Emitir Declaração e Imposto de Renda", descricao: "Como Emitir Declaração e Imposto de Renda", imagem: "{% static 'assets/img/Jornada-do-aluno/como emitir declaração de IR.png' %}", videoLink: "https://www.youtube.com/embed/X7IVPwOGa4I?si=M_GPGMXRXUCU-aVW" },
  {
    id: "selecao2", texto: "Historico e Declaração", descricao: "Historico e Declaração", imagem: "{% static 'assets/img/Jornada-do-aluno/historico e declaração.png' %}", videoLink: "https://www.youtube.com/embed/vpP32WUbR4U?si=wa9zRyrkiZf1QRRK" },
  {
    id: "selecao3", texto: "Secretaria", descricao: "Secretaria", imagem: "{% static 'assets/img/Jornada-do-aluno/secretaria.png' %}", videoLink: "https://www.youtube.com/embed/p9mIJq_zm0g?si=mkK48O-4CXp-tdfm" },
  { 
    id: "selecao12", texto: "Tutoria", descricao: "Tutoria", imagem: "{% static 'assets/img/Jornada-do-aluno/tutoria.png' %}", videoLink: "https://www.youtube.com/embed/YPC4qnUhluE?si=c6TH9e_xRNp3I2lx" },
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
      if (opcao.videoLink) {
        videoModal.style.display = "block";
        iframe1.src = opcao.videoLink;
      } else if (opcao.cards) {
        // Limpa o cardContainer
        cardContainer.innerHTML = '';

        // Cria e adiciona os novos cards de seleção ao cardContainer
        selecao.forEach(function (item) {
          var selecaoCardElement = document.createElement("div");
          selecaoCardElement.classList.add("card", "animate-left"); // Adiciona a classe de animação
          // selecaoCardElement.style.width = "18rem";
          selecaoCardElement.innerHTML = `
            <a href="${item.texto}">
              <img src="${item.imagem}" class="card-img-top">
              <div class="card-body">
                <h5 class="card-title">${item.descricao}</h5>
              </div>
            </a>
          `;
          cardContainer.appendChild(selecaoCardElement);
          backButton.style.display = "block";

          selecaoCardElement.querySelector("a").addEventListener("click", function (event) {
            event.preventDefault();
            // Limpa o cardContainer
            cardContainer.innerHTML = '';
            videoModal.style.display = "block";
          
            if (item.videoLink) {
              iframe1.src = item.videoLink;
            } else if (item.cards) {
              // Limpa o cardContainer
              cardContainer.innerHTML = '';
          
              // Cria e adiciona os novos cards de seleção ao cardContainer
              item.cards.forEach(function (finalCard) {
                var finalCardsCardElement = document.createElement("div");
                finalCardsCardElement.classList.add("card", "animate-left");
                finalCardsCardElement.innerHTML = `
                  <a href="${finalCard.link}">
                    <img src="${finalCard.imgSrc}" class="card-img-top">
                    <div class="card-body">
                      <h5 class="card-title">${finalCard.title}</h5>
                    </div>
                  </a>
                `;
                cardContainer.appendChild(finalCardsCardElement);
                backButton.style.display = "block";
          
                finalCardsCardElement.querySelector("a").addEventListener("click", function (event) {
                  event.preventDefault();
          
                  if (finalCard.videoLink) {
                    iframe1.src = finalCard.videoLink;
                  }
                });
              });
            }
          });            
        });

        // Esconda o botão Voltar
        backButton.style.display = "block";
      }
    });
  });
}

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
