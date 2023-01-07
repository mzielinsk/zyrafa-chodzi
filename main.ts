input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # # . .
        . . # . .
        . . # # #
        . . # . #
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # . . .
        . # . . .
        . # # # #
        . # . . #
        . # . . #
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        # # . . .
        `)
    basic.showLeds(`
        # . # . #
        . . # . #
        # . # # #
        # . # . #
        # . . # .
        `)
})
music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
basic.showNumber(3)
basic.showNumber(2)
basic.showNumber(1)
basic.forever(function () {
    basic.showLeds(`
        . # # . .
        . . # . .
        . . # . .
        . . # # #
        . . # . #
        `)
    basic.showIcon(IconNames.Giraffe)
    basic.showLeds(`
        # . . . .
        # . . . .
        # . . . .
        # # # . .
        # . # . .
        `)
    basic.showLeds(`
        . . . . #
        . . . . .
        . . . . .
        # # . . .
        . # . . .
        `)
    basic.showLeds(`
        . . . # #
        . . . . #
        . . . . #
        # . . . #
        # . . . #
        `)
    basic.showLeds(`
        . . # # .
        . . . # .
        . . . # .
        . . . # #
        . . . # .
        `)
})
