radio.onReceivedNumber(function (receivedNumber) {
    hp += 0 - receivedNumber
})
input.onButtonPressed(Button.A, function () {
    if (attack_mode == 1) {
        radio.sendNumber(1)
        hunger += -3
    } else {
        basic.showString("Hunger:" + hunger)
        basic.showString("HP:" + hp)
    }
})
input.onGesture(Gesture.LogoUp, function () {
    hunger += 1
    fun += -2
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
        basic.showString("Fun:" + fun)
        basic.showString("Money:" + money)
    }
})
input.onGesture(Gesture.Shake, function () {
    fun += 1
    hunger += -2
})
let attack_mode = 0
let money = 0
let fun = 0
let hunger = 0
let hp = 0
radio.setGroup(1)
hp = 10
hunger = 10
fun = 10
money = 10
fun = 0
attack_mode = 0
images.iconImage(IconNames.Rabbit).showImage(0)
basic.forever(function () {
    if (0 > hp) {
        money += -10
    } else if (20 < hunger) {
        money += 4
    } else if (0 > hunger) {
        hp += -1
    } else {
    	
    }
    if (0 > money) {
        basic.showString("Game Over")
    }
})
