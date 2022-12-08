def is_leap(year):
    leap = False
    task = year
    if task % 400 == 0:
        leap = True
    elif task % 4 == 0 and task % 100 != 0 :
        leap = True
        
    return leap