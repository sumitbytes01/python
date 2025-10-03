seat_type = input("Enter seat type(sleeper, AC, general or luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper it is, enjoy")
    case "ac":
        print("AC it is, enjoy")
    case "general":
        print("General it is, enjoy")
    case "luxury":
        print("Luxury it is, enjoy")
    case _:
        print("Invalid seat type!!!")

