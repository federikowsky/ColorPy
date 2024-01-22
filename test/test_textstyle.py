from pycolor import FG, BG

def prova():
    # FG._palette
    # FG._rainbow_palette
    # FG._color_legend

    # BG._palette
    # BG._rainbow_palette
    # BG._color_legend

    print(FG.Aquamarine2, "ciaooo", FG.RESET)
    print(FG.num2escape(78), "ciaooo", FG.RESET)

    print(FG.blink(f"{FG.SeaGreen3}ciaooooooooooo{FG.RESET}"))
    print(FG.underline("ciaooooooooooo"))
    print(FG.bold("ciaooooooooooo"))
    print(FG.dim("ciaooooooooooo"))
    print(FG.italic("ciaooooooooooo"))
    print(FG.invert("ciaooooooooooo"))
    print(FG.hidden("ciaooooooooooo"))
    print(FG.strikethrough("ciaooooooooooo"))

    print(f"{FG.BOLD} # Set style to bold, red foreground.{FG.BOLD_RST}")
    print("\x1b[5;31m # Set style to bold, red foreground.")
    print("\x1b[5;32m # Set style to bold, red foreground.")
    print("\x1b[5;33m # Set style to bold, red foreground.")
    print("\x1b[4;33m # Set style to bold, red foreground.")
    print("\x1b[38;2;0;0;255m # Set style\x1b[0m")
    print("\x1b[1;37;46m # Set style to dimmed black foreground with red background.\33[22m ciaoooo")

    
    
if __name__ == "__main__":
    prova()