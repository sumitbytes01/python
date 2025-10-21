device_status = "active"
current_temp=36

if device_status == "active":
    if current_temp>35:
        print("Warning!!! High Temperature")
    else:
        print("Temperature Normal")
else:
    print("Device is offline")