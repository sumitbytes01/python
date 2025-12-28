def serve_coffee(flavour):
    try:
        print(f"Preparing {flavour} coffee ...")
        if flavour == "unknown":
            raise ValueError("This is an unknown flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} Coffee is Served")
    finally:
        print("Next customer please")
    
serve_coffee("unknown")
print("-----------------------------")
serve_coffee("vanilla")
        
        

    
