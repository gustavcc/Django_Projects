// Menu
const hamburger = document.getElementById('menu-hamburger');
const menu = document.getElementById('menu');

hamburger.addEventListener('change', () => {
    if (hamburger.checked) {
        menu.style.left = '-15px';
    } else {
        menu.style.left = '-90vw';
    }
});

// Dark Mode 
const html = document.querySelector('html');
const dark_mode = document.getElementById('switch');

dark_mode.addEventListener('change', ()=>{
    html.classList.toggle('dark-mode')
})

// paginacao.js
// const questoes = document.querySelectorAll('.questoes');
// const numPorPagina = 10;
// const paginas = document.querySelectorAll('.pagina');

// paginas.forEach(pagina => {
//     pagina.addEventListener('click', function() {
//         const numeroPagina = parseInt(this.dataset.pagina);
//         mostrarPagina(numeroPagina);
//     });
// });

// function mostrarPagina(pagina) {
//     const inicio = (pagina - 1) * numPorPagina;
//     const fim = pagina * numPorPagina;

//     questoes.forEach((questao, index) => {
//         if (index >= inicio && index < fim) {
//             questao.style.display = 'block';
//         } else {
//             questao.style.display = 'none';
//         }
//     });
// }

// mostrarPagina(1); // Mostra a primeira página por padrão

// Questões
const  questoes = document.querySelectorAll(".questoes"); //elemento das respostas (div com os botões)
let score = 0;

questoes.forEach(questao => {
    const respostas = questao.querySelectorAll(".btn");
    const indexQuestao = questao.querySelector('.indexQuestao');
    respostas.forEach(resposta  => {
        if(resposta.id == resposta.value){
            resposta.id = 'correct';
        }
        resposta.addEventListener('click', selecionaResposta_Correta);
    });
});

//* funcao que seleciona a resposta correta
function selecionaResposta_Correta(e){ 
    const botaoSelecionado = e.target; 
    let isCorrect = false;
    console.log(botaoSelecionado.id);
    if (botaoSelecionado.id == 'correct'){
        isCorrect = true;
    }
    if(isCorrect){ 
        botaoSelecionado.classList.add("correct");
        score++;
    }
    else{
        botaoSelecionado.classList.add("incorrect");
    }
    botaoSelecionado.style
    console.log(score);
}