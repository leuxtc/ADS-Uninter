const azul = '#74b3e7'
const verde = '#74e783'
const vermelho  = '#d44d4d'

let bttn = document.querySelector('#bttn')

bttn.style.background = azul

let quebrado = false
let cliques = 0

bttn.addEventListener('mouseout', e => {
    if (!quebrado) {
        bttn.style.background = azul
    }
    else {
        bttn.innerHTML = 'Quebrado'
    }
})

bttn.addEventListener('mouseover', e => {
    if (!quebrado) {
        bttn.style.background = verde
    }
    else {
        bttn.innerHTML = 'Quebrado'
    }
})

bttn.addEventListener('click', e => {
    cliques++
    

    if (cliques >= 10) {
        bttn.style.background = vermelho
        bttn.innerHTML = 'Quebrado'
        quebrado = true
    }
})