function showContent(contentId) {
  // Remove a classe 'show' de todos os conteúdos
  var contents = document.querySelectorAll('.content');
  contents.forEach(function (content) {
      content.classList.remove('show');
  });

  // Adiciona a classe 'show' ao conteúdo selecionado
  var contentToShow = document.getElementById(contentId);
  contentToShow.classList.add('show');
}

function handleMobileSelect(selectElement) {
  var selectedContentId = selectElement.value;
  showContent(selectedContentId);
}

