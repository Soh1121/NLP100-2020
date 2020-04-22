def something_at_that_time(hour, something, predicate):
    return "{}時の{}は{}".format(str(hour), something, str(predicate))


x = 12
y = "気温"
z = 22.4
print(something_at_that_time(x, y, z))
