def brew_coffee(flavour):
    if flavour not in ["espresso", "mocha", "copa"]:
        raise ValueError(f"Unsupported coffee flavour {flavour}...")
    else:
        print(f"Brewing {flavour}..")

brew_coffee("espresso")

brew_coffee("masala")
    