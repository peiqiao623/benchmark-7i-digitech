def on_received_number(receivedNumber):
    global hp
    hp += 0 - receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global hunger
    if attack_mode == 1:
        radio.send_number(1)
        hunger += -3
    else:
        basic.show_string("Hunger:" + str(hunger))
        basic.show_string("HP:" + str(hp))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    global hunger, fun
    hunger += 1
    fun += -2
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    global attack_mode
    if attack_mode == 0:
        attack_mode += 1
    else:
        attack_mode += -1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global hunger
    if attack_mode == 0:
        radio.send_number(4)
        hunger += -10
    else:
        basic.show_string("Fun:" + str(fun))
        basic.show_string("Money:" + str(money))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global fun, hunger
    fun += 1
    hunger += -2
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

attack_mode = 0
money = 0
fun = 0
hunger = 0
hp = 0
radio.set_group(1)
hp = 10
hunger = 10
fun = 10
money = 10
fun = 0
attack_mode = 0
images.icon_image(IconNames.RABBIT).show_image(0)

def on_forever():
    global money, hp
    if 0 > hp:
        money += -10
    elif 20 < hunger:
        money += 4
    elif 0 > hunger:
        hp += -1
    else:
        pass
    if 0 > money:
        basic.show_string("Game Over")
basic.forever(on_forever)
