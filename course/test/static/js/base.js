const hamburger = document.getElementById('menu-hamburger');
const menu_activate = document.getElementById('menu-activate');

hamburger.addEventListener('change', () => {
    menu_activate.showModal();
    if (hamburger.checked) {
        menu_activate.style.left = '0';
        window.addEventListener('click', outsideClickListener);
    } else {
        menu_activate.close();
        menu_activate.style.left = '-80vw';
        window.removeEventListener('click', outsideClickListener);
    }
});

function outsideClickListener(event) {
    if (event.target === menu_activate) {
        menu_activate.close();
        menu_activate.style.left = '-80vw';
        hamburger.checked = false;
    }
};