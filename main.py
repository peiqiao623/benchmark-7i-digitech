def on_button_pressed_a():
    global hunger
    if attack_mode == 1:
        radio.send_number(1)
        hunger += -3
    else:
        basic.show_string("Hunger", 150)
        basic.show_string("" + str(hunger))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_free_fall():
    global fun, hunger
    fun += 1
    hunger += -2
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

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
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global hunger, fun
    hunger += 1
    fun += -2
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

attack_mode = 0
hunger = 0
radio.set_group(1)
hunger = 10
fun = 10
money = 10
fun = 0
attack_mode = 0
images.icon_image(IconNames.RABBIT).show_image(0)