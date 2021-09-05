document.querySelector('html').style.filter = 'saturate(0) contrast(20)';
document.querySelectorAll('*').forEach(ele => ele.style.border = `${Math.floor(Math.random() * 10)}px solid black`);