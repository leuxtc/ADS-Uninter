let pessoa = {
    nome: "José",
    idade: 115,
}

let listaDesejos = [
    'Camisa do corinthians',
    'Geladeira eletrolux',
    'Tênis de rodinha'
]

console.log(pessoa)
console.log(pessoa.nome)

console.log(listaDesejos)
console.log(listaDesejos[0])

let paragrafo = document.getElementById("prg_1")

paragrafo.addEventListener("mouseover", fundoVerde)
paragrafo.addEventListener("mouseout", fundoAmarelo)
paragrafo.addEventListener("click", addLista)

function addLista() {
    paragrafo.innerHTML = listaDesejos
}

function fundoVerde() {
    paragrafo.style.background = "green"
}

function fundoAmarelo() {
    paragrafo.style.background = "yellow"
}


