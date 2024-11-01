input.onButtonPressed(Button.A, function () {
    enviar_mensaje("quiero")
})
function enviar_mensaje (mensaje: string) {
    radio.sendString(mensaje)
}
radio.onReceivedString(function (mensaje) {
    manejar_mensaje(mensaje)
})
function manejar_mensaje (mensaje: string) {
    if (mensaje == "truco") {
        basic.showString("T")
        basic.pause(1000)
        if (input.buttonIsPressed(Button.A)) {
            enviar_mensaje("aceptar")
        } else {
            enviar_mensaje("rechazar")
        }
    } else if (mensaje == "quiero") {
        basic.showString("Q")
        basic.pause(1000)
        if (input.buttonIsPressed(Button.A)) {
            puntos += 1
            enviar_mensaje("aceptado")
        } else {
            enviar_mensaje("rechazado")
        }
    }
}
input.onButtonPressed(Button.B, function () {
    asignar_carta()
    enviar_mensaje("truco")
})
function asignar_carta () {
    mi_carta = Math.randomRange(1, 10)
    basic.showNumber(mi_carta)
}
let mi_carta = 0
let puntos = 0
let rondas = 0
radio.setGroup(7)
basic.forever(function () {
    basic.showString("Puntos: " + puntos)
    basic.pause(2000)
})
