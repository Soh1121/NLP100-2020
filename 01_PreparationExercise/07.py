def somthing_at_that_time(hour, somthing, predicate):
    return "{}時の{}は{}".format(str(hour), somthing, str(predicate))


x = 12
y = "気温"
z = 22.4
print(somthing_at_that_time(x, y, z))
