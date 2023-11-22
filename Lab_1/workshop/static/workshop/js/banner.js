let currentBanner = 0;
let bannerContainer = document.querySelectorAll('#banner-container')[0];
let global_interval = bannerContainer.dataset['interval'];

console.log("Banner, banner interval", {bannerContainer, global_interval})

let banners = bannerContainer.querySelectorAll('.banner');
let intervalId;

rotateBanner();
startRotation();

window.addEventListener('focus', startRotation);
window.addEventListener('blur', stopRotation);

function rotateBanner()
{
    for (let i = 0; i < banners.length; i++)
        banners[i].hidden = banners[i] !== currentBanner;

    currentBanner++;

    if (currentBanner === banners.length)
        currentBanner = 0;
}

function startRotation() {
    intervalId = setInterval(rotateBanner, global_interval);

}

function stopRotation() {
    clearInterval(intervalId);
}