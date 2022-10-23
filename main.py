def on_logo_pressed():
    game.resume()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    Nave.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    game.pause()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global Disparo
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            586,
            255,
            255,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    Disparo = game.create_sprite(Nave.get(LedSpriteProperty.X), Nave.get(LedSpriteProperty.Y))
    for index in range(5):
        Disparo.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Nave.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Disparo: game.LedSprite = None
Nave: game.LedSprite = None
Nave = game.create_sprite(2, 4)
Enemigo_1 = game.create_sprite(2, 0)
Disparo = game.create_sprite(2, 0)
Enemigo_1.delete()
Disparo.delete()
game.set_score(0)

def on_forever():
    if Disparo.is_touching(Enemigo_1):
        Enemigo_1.delete()
        Disparo.delete()
        game.add_score(1)
    elif Enemigo_1.is_touching(Nave):
        game.game_over()
    elif Enemigo_1.get(LedSpriteProperty.Y) == 4:
        game.game_over()
basic.forever(on_forever)

def on_forever2():
    if Disparo.get(LedSpriteProperty.Y) == 0:
        Disparo.delete()
basic.forever(on_forever2)

def on_forever3():
    global Enemigo_1
    basic.pause(randint(1000, 3000))
    if Enemigo_1.is_deleted():
        Enemigo_1 = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever3)

def on_forever4():
    basic.pause(1000)
    if not (Enemigo_1.is_deleted()):
        Enemigo_1.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever4)
