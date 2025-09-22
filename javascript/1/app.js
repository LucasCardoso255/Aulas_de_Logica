const botao1 = document.getElementById("btn1");
const botao2 = document.getElementById("btn2");
let input = document.getElementById("bussanha");

function funcaofoda(){
    alert("Você clicou!");
}
function funcaodois(){
    const textbussanha = input.value;
    alert("Digitastes: " + textbussanha);
}

botao1.addEventListener("click", funcaofoda);
botao2.addEventListener("click", funcaodois);
