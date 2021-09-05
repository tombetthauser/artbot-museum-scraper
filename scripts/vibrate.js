const liveDiv = document.querySelector("#monitor-div")
const randId = Math.floor(Math.random() * 1000000000)
console.log("VIBRATE.JS START:", randId);

let count = 0;

const interval = setInterval(() => {
  console.log("INTERVAL RUN:", count);
  console.log("INTERVAL RUN:", count);
  liveDiv.style.top = `${Math.floor(Math.random() * 20)}px`;
  liveDiv.style.left = `${Math.floor(Math.random() * 30)}px`;
}, 20);