const cards = document.querySelectorAll(".employee-card");

cards.forEach(
card_w => {
  card_w.addEventListener('mousemove', event=>{
   //console.log(card_w.getBoundingClientRect());
   const [x, y] = [event.offsetX, event.offsetY];
   const rect = card_w.getBoundingClientRect();
   const [width, height] = [rect.width, rect.height];
   const middleX = width / 2;
   const middleY = height / 2;
   const offsetX = ((x - middleX) / middleX) * 25;
   const offsetY = ((y - middleY) / middleY) * 25;
   const offX = 50 + ((x - middleX) / middleX) * 25;
   const offY = 50 - ((y - middleY) / middleY) * 25;
   card_w.style.setProperty("--rotateX", 1 * offsetX + "deg");
   card_w.style.setProperty("--rotateY", -1 * offsetY + "deg");
   card_w.style.setProperty("--posx", offX + "%");
   card_w.style.setProperty("--posy", offY + "%");
  });
  card_w.addEventListener('mouseleave', eve=>{

    card_w.addEventListener("animationend", e=>{
      card_w.style.setProperty("--rotateX", "0deg");
      card_w.style.setProperty("--rotateY", "0deg");
      card_w.style.setProperty("--posx", "50%");
      card_w.style.setProperty("--posy", "50%");
    }, {
      once: true
    });
  });
});