const body = document.querySelector("body");
const monitorDiv = document.createElement("div");

monitorDiv.setAttribute("id", "monitor-div");
monitorDiv.style.position = "sticky";
monitorDiv.style.top = "0";
monitorDiv.style.zIndex = "5000";
monitorDiv.style.marginRight = "100px";
monitorDiv.style.width = "500px";
// monitorDiv.style.height = "350px";
monitorDiv.style.backgroundColor = "white";
monitorDiv.style.border = "3px dotted black";
monitorDiv.style.padding = "50px";
monitorDiv.style.color = "black";
monitorDiv.innerHTML = "<h3>artbot_monitor 🤖💬</h3>";

body.prepend(monitorDiv);