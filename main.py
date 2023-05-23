basic.show_string("Hello There")
basic.show_icon(IconNames.DIAMOND)

def on_forever():
    basic.show_leds("""
        . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . . . . .
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        . # . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # # . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . #
                . . . . #
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . #
                . . . . #
                . . . # .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . #
                . . . . #
                . . # # .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . #
                . . . . #
                . # # # .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                . . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . # # # .
                . . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_icon(IconNames.SMALL_DIAMOND)
basic.forever(on_forever)
