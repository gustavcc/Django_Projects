const hamburger = document.getElementById('menu-hamburger');
const menu = document.getElementById('menu');

hamburger.addEventListener('change', () => {
    if (hamburger.checked) {
        menu.style.left = '0';
        // window.addEventListener('click', outsideClickListener);
    } else {
        menu.style.left = '-80vw';
        // window.removeEventListener('click', outsideClickListener);
    }
});

const html = document.querySelector('html');
const dark_mode = document.getElementById('switch');

dark_mode.addEventListener('change', ()=>{
    html.classList.toggle('dark-mode')
})