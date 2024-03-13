// Menu
const hamburger = document.getElementById('menu-hamburger');
const menu = document.getElementById('menu');

hamburger.addEventListener('change', () => {
    if (hamburger.checked) {
        menu.style.left = '0';
    } else {
        menu.style.left = '-80vw';
    }
});

// Dark Mode 
const html = document.querySelector('html');
const dark_mode = document.getElementById('switch');

dark_mode.addEventListener('change', ()=>{
    html.classList.toggle('dark-mode')
})

// paginacao.js
const questoes = document.querySelectorAll('.questoes');
const numPorPagina = 10;
const paginas = document.querySelectorAll('.pagina');

paginas.forEach(pagina => {
    pagina.addEventListener('click', function() {
        const numeroPagina = parseInt(this.dataset.pagina);
        mostrarPagina(numeroPagina);
    });
});

function mostrarPagina(pagina) {
    const inicio = (pagina - 1) * numPorPagina;
    const fim = pagina * numPorPagina;

    questoes.forEach((questao, index) => {
        if (index >= inicio && index < fim) {
            questao.style.display = 'block';
        } else {
            questao.style.display = 'none';
        }
    });
}

mostrarPagina(1); // Mostra a primeira página por padrão
