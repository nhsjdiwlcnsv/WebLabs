const boot = document.getElementById('boot');
const string = document.getElementById('string');
const textContainer = document.getElementById('welcome-text-container');
const text = document.getElementById('welcome-text');


window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const leftOffset = scrollY / 3;
    const rightOffset = scrollY / 3;

    boot.style.left = `calc(${rightOffset}px - 400px)`;
    string.style.left = `calc(${leftOffset}px - 400px)`;

    const rotate = scrollY * 0.8;

    textContainer.style.transform = `rotate(${rotate}deg)`;
})