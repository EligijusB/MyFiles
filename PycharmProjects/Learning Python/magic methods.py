###surrounded by double underscores
# ---------- MAGIC METHODS ----------
# Magic methods are surrounded by double underscores
# We can use magic methods to define how operators
# like +, -, *, /, ==, >, <, etc. will work with our
# custom objects

# Magic methods are used for operator overloading
# in Python

# __eq__ : Equal
# __ne__ : Not Equal
# __lt__ : Less Than
# __gt__ : Greater Than
# __le__ : Less Than or Equal
# __ge__ : Greater Than or Equal
# __add__ : Addition
# __sub__ : Subtraction
# __mul__ : Multiplication
# __div__ : Division
# __mod__ : Modulus


class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
        #2 digits returned for minutes and seconds

    def __add__(self, other_time):
        new_time = Time()

        #add the seconds and correct if sum > 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = (self.second + other_time.second)

        #add minutes and correct if sum > 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = (self.minute + other_time.minute)

        #add hours and correct is sum > 24
        if (self.hour + other_time.hour) > 24:
            new_time.hour = (other_time.hour + self.hour) - 24
        else:
            new_time.hour = (self.hour + other_time.hour)

        return new_time

def main():
    time1 = Time(1, 20, 30)
    print(time1)

    time2 = Time(24, 41,30)

    print(time1 + time2)

main()