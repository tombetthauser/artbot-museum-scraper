const body = document.querySelector("body");
const monitorDiv = document.createElement("div");

monitorDiv.setAttribute("id", "monitor-div");
// monitorDiv.style.display = "block";
monitorDiv.style.position = "sticky";
monitorDiv.style.zIndex = "5";
monitorDiv.style.top = "25px";
monitorDiv.style.marginRight = "100px";
monitorDiv.style.width = "500px";
monitorDiv.style.height = "350px";
monitorDiv.style.backgroundColor = "white";
monitorDiv.style.border = "5px solid black";
monitorDiv.innerText = "MONITOR DIV";

body.appendChild(monitorDiv);