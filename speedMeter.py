#to check and return the speed status using function
def get_speed_status(speed):
    if speed < 60:
        print("Normal")
    elif speed >= 60 and speed < 80:
        print("Warning")
    elif speed >= 80:
        print("Over Speed")

speed = int(input("Enter the speed: "))
get_speed_status(speed)