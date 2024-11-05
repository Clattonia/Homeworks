def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(str(a) + str(b))
    
    
add_everything_up("мда", 22.33)
add_everything_up(3, 22.33)
add_everything_up(13.37, "иди своей дорогой сталкер")