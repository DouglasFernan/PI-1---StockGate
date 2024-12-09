document.querySelectorAll('.dropdown-btn').forEach(button => {
    button.addEventListener('click', () => {
        const dropdown = button.parentElement;
        dropdown.classList.toggle('active');
 });
});

function toggleModal(event) {
    // Prevenir o evento de clique de se propagar para evitar que o clique no modal feche o modal
    event.stopPropagation();

    // Verifica se o clique foi no #info ou no #openModalBtn
    const modal = document.getElementById("modal");
    const isVisible = modal.style.display === "block";

    // Se o modal já está aberto, esconde-o, caso contrário, exibe-o
    if (isVisible) {
        modal.style.display = "none";
    } else {
        // Exibe o modal abaixo da área clicada
        const position = event.target.getBoundingClientRect();
        modal.style.top = (position.top + position.height + window.scrollY) + 'px';
        modal.style.left = position.left + 'px';
        modal.style.display = "block";
    }
}

// Fecha o modal se o clique ocorrer fora do modal
window.onclick = function(event) {
    var modal = document.getElementById("modal");
    if (!modal.contains(event.target) && !event.target.closest('#openModalBtn') && !event.target.closest('#info')) {
        modal.style.display = "none";
    }
}
