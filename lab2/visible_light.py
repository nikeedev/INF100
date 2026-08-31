def wavelength_color(wavelength):
    if 380 <= wavelength <= 450:
        return "Violet"
    elif 450 < wavelength <= 485:
        return "Blue"
    elif 485 < wavelength <= 500:
        return "Cyan"
    elif 500 < wavelength <= 565:
        return "Green"
    elif 565 < wavelength <= 590:
        return "Yellow"
    elif 590 < wavelength <= 625:
        return "Orange"
    elif 625 < wavelength <= 750:
        return "Red"
    else:
        return "None"

def thz_color(wavelength):
    if 400 <= wavelength < 480:
        return "Red"
    elif 480 <= wavelength < 510:
        return "Orange"
    elif 510 <= wavelength < 530:
        return "Yellow"
    elif 530 <= wavelength < 600:
        return "Green"
    elif 600 <= wavelength < 620:
        return "Cyan"
    elif 620 <= wavelength < 670:
        return "Blue"
    elif 670 <= wavelength < 790:
        return "Violet"
    else:
        return "None"



unit = input("Angi enhet (nm eller THz):\n")

if unit == "nm" or unit == "THz":
    value = int(input(f"Angi verdi i {unit}:\n"))

    if unit == "THz":
        color = thz_color(value)

    if unit == "nm":
        color = wavelength_color(value)
    
    if color != "None":
        print(f"\n{color}")
    else:
        print(f"\n{value} {unit} er utenfor det synlige spekteret.")
    
else:
    print(f"\nEnheten må være i nm eller THz, det kan ikke være {unit}.")
    exit(0)


