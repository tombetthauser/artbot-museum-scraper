const liveDiv = document.querySelector("#monitor-div")
const randId = Math.floor(Math.random() * 1000000000)
console.log("VIBRATE.JS START:", randId);

const BORDERS = ['solid', 'outset', 'inset', 'ridge', 'dotted'];
const FONTS = ['serif', 'sans-serif', 'cursive', 'monotype'];
let count = 0;

const topMargin = Math.floor(Math.random() * 500);
const leftMargin = Math.floor(Math.random() * 1000);

const yVibration = Math.floor(Math.random() * 50);
const xVibration = Math.floor(Math.random() * 50);

liveDiv.style.transition = `${Math.floor(Math.random() * 1000)}ms`;
liveDiv.style.width = `${Math.floor(Math.random() * 800) + 200}px`;

const interval = setInterval(() => {
  console.log("INTERVAL RUN:", count);
  console.log("INTERVAL ID:", randId);
  count++;
  liveDiv.style.top = `${Math.floor(Math.random() * yVibration) + topMargin}px`;
  liveDiv.style.left = `${Math.floor(Math.random() * xVibration) + leftMargin}px`;
  liveDiv.style.boxShadow = `${Math.random() < .5 ? '-' : ''}${Math.floor(Math.random() * 100)}px ${Math.floor(Math.random() * 100)}px 0px rgba(0,0,0,${Math.random() * 1})`;
  liveDiv.style.padding = `${Math.floor(Math.random() * 10) + 40}px`;
  liveDiv.style.border = `${Math.floor(Math.random() * 15)}px ${BORDERS[Math.floor(Math.random() * BORDERS.length)]} black`;
  document.querySelectorAll("#monitor-div li").forEach(ele => ele.style.fontFamily = `${FONTS[Math.floor(Math.random() * FONTS.length)]}`);
  document.querySelector("#monitor-div h3").style.fontFamily = `${FONTS[Math.floor(Math.random() * FONTS.length)]}`;
  document.querySelector("#monitor-div h3").style.fontSize = `${Math.floor(Math.random() * 5) + 25}px`;
}, 20);