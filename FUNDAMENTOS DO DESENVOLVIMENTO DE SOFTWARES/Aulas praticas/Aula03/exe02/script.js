const num_1 = document.querySelector('#num_1')
const num_2 = document.querySelector('#num_2')
const seletor = document.querySelector('#seletor')

let resposta = document.querySelector('#resposta')

num_1.addEventListener('keyup', calcularResultado)
num_2.addEventListener('keyup', calcularResultado)

seletor.addEventListener('change', calcularResultado)

function calcularResultado() {
    resposta.classList.remove('problema')

    const val_1 = parseInt(num_1.value)
    const val_2 = parseInt(num_2.value)

    if (num_1.value != '' && num_2.value != '') {
        if (seletor.value === 'adicao') {
            resposta.innerHTML = val_1 + val_2
        }
        if (seletor.value === 'subtracao') {
            resposta.innerHTML = val_1 - val_2
        }
        if (seletor.value === 'multiplicacao') {
            resposta.innerHTML = val_1 * val_2
        }
        if (seletor.value === 'divisao') {
            resposta.innerHTML = val_1 / val_2
        }
    }
    else {
        resposta.classList.add('problema')
        resposta.innerHTML = 'Preencha os dois campos!'
    }
}