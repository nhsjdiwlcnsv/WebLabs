const timer = document.getElementById('timer');
const totalTime = 60 * 60 * 1000; // 1 hour
let targetTime = parseInt(localStorage.getItem('timerTargetTime')) || (Date.now() + totalTime); // 1 hour
let timeCounterInterval;

function updateTimeCounter() {
    if (targetTime > Date.now()) {
        const timeLeft = targetTime - Date.now();
        const hours = Math.floor((timeLeft / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((timeLeft / (1000 * 60)) % 60);
        const seconds = Math.floor((timeLeft / 1000) % 60);
        timer.innerHTML = `Time left: ${hours}h ${minutes}m ${seconds}s`;
        localStorage.setItem('timerTargetTime', targetTime);
    } else {
        timer.innerHTML = `Time's up, friendo!`;
        clearInterval(timeCounterInterval);
        localStorage.removeItem('timerTargetTime');
    }
}

function startCounter() {
    updateTimeCounter();
    timeCounterInterval = setInterval(updateTimeCounter, 1000);
}

if (targetTime > Date.now()) {
    startCounter();
} else {
    targetTime = Date.now() + totalTime;
    startCounter();
}