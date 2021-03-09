const loginPage = document.querySelector('.login-screen');
const loginMenu = document.querySelector('.login-wrapper');
const registerPage = document.querySelector('.register-screen');
const registerMenu = document.querySelector('.register-wrapper');

loginMenu.classList.toggle('active');
let currentPage = 'login';


loginPage.addEventListener('click', () => {
    currentPage = 'login';
    registerPage.style.color = 'black';
    loginPage.style.color = 'rgb(38, 39, 38)';
    screenSwitch()
});

registerPage.addEventListener('click', () => {
    currentPage = 'register';
    loginPage.style.color = 'black'
    registerPage.style.color = 'rgb(38, 39, 38)';
    screenSwitch()
});

function screenSwitch() {
    if (currentPage == 'login') {
        loginMenu.classList.toggle('active');
        registerMenu.classList.toggle('active');
    }

    if (currentPage == 'register') {
        registerMenu.classList.toggle('active');
        loginMenu.classList.toggle('active');
}
}

screenSwitch()
