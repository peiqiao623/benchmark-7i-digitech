radio.onReceivedNumber(function (receivedNumber) {
    hp += 0 - receivedNumber
})
input.onButtonPressed(Button.A, function () {
    if (attack_mode == 1) {
        radio.sendNumber(1)
        hunger += -3
    } else {
        basic.showString("Hunger", 150)
basic.showString("" + hunger)
    }
})
input.onGesture(Gesture.FreeFall, function () {
    fun += 1
    hunger += -2
})
input.onButtonPressed(Button.AB, function () {
    if (attack_mode == 0) {
        attack_mode += 1
    } else {
        attack_mode += -1
    }
})
input.onButtonPressed(Button.B, function () {
    if (attack_mode == 0) {
        radio.sendNumber(4)
        hunger += -10
    } else {
    	
    }
})
input.onGesture(Gesture.Shake, function () {
    hunger += 1
    fun += -2
})
let hp = 0
let attack_mode = 0
let hunger = 0
radio.setGroup(1)
hunger = 10
let fun = 10
let money = 10
fun = 0
attack_mode = 0
images.iconImage(IconNames.Rabbit).showImage(0)
