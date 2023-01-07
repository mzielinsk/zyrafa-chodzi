def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # # . .
                . . # . .
                . . # # #
                . . # . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . # . . .
                . # . . .
                . # # # #
                . # . . #
                . # . . #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        . # . # .
                . # # # .
                . # . . .
                . # . . .
                # # . . .
    """)
    basic.show_leds("""
        # . # . #
                . . # . #
                # . # # #
                # . # . #
                # . . # .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
    SoundExpressionPlayMode.UNTIL_DONE)
basic.show_number(input.temperature())
basic.show_number(2)
basic.show_number(1)

def on_forever():
    basic.show_leds("""
        . # # . .
                . . # . .
                . . # . .
                . . # # #
                . . # . #
    """)
    basic.show_icon(IconNames.GIRAFFE)
    basic.show_leds("""
        # . . . .
                # . . . .
                # . . . .
                # # # . .
                # . # . .
    """)
    basic.show_leds("""
        . . . . #
                . . . . .
                . . . . .
                # # . . .
                . # . . .
    """)
    basic.show_leds("""
        . . . # #
                . . . . #
                . . . . #
                # . . . #
                # . . . #
    """)
    basic.show_leds("""
        . . # # .
                . . . # .
                . . . # .
                . . . # #
                . . . # .
    """)
basic.forever(on_forever)
