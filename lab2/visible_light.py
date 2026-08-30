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

unit = input("Angi enhet (nm eller THz):\n")

if unit == "nm" or unit == "THz":
    value = int(input(f"Angi verdi i {unit}:\n"))

    if unit == "THz":
        speed_of_light = 300_000_000 # m/s

        color = wavelength_color(int((value * 10**12) / speed_of_light))

    if unit == "nm":
        color = wavelength_color(value)
    
    if color != "None":
        print(f"\n{color}")
    else:
        print(f"\n{value} {unit} er utenfor det synlige spekteret.")
    
else:
    print(f"\nEnheten må være i nm eller THz, det kan ikke være {unit}.")
    exit(0)


