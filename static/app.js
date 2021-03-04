const loginPage = document.querySelector('.login-screen');
const loginMenu = document.querySelector('.login-wrapper');
const registerPage = document.querySelector('.register-screen');
const registerMenu = document.querySelector('.register-wrapper');

loginMenu.classList.toggle('active');
let currentPage = 'login';


loginPage.addEventListener('click', () => {
    currentPage = 'login';
    screenSwitch()
});

registerPage.addEventListener('click', () => {
    currentPage = 'register';
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
