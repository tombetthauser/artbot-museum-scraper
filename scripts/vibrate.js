const liveDiv = document.querySelector("#monitor-div")
const randId = Math.floor(Math.random() * 1000000000)
console.log("VIBRATE.JS START:", randId);

let count = 0;

const topMargin = Math.floor(Math.random() * 500);
const leftMargin = Math.floor(Math.random() * 1000);

const yVibration = Math.floor(Math.random() * 50);
const xVibration = Math.floor(Math.random() * 50);

liveDiv.style.transition = `${Math.floor(Math.random() * 100)}ms`;

const interval = setInterval(() => {
  console.log("INTERVAL RUN:", count);
  console.log("INTERVAL ID:", randId);
  count++;
  liveDiv.style.top = `${Math.floor(Math.random() * yVibration) + topMargin}px`;
  liveDiv.style.left = `${Math.floor(Math.random() * xVibration) + leftMargin}px`;
  liveDiv.style.boxShadow = `${Math.floor(Math.random() * xVibration)}px`;
}, 20);