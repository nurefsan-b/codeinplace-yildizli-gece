from karel.stanfordkarel import *

def main():
    paint_black_row_1()
    new_row_left()
    paint_midnightblue_row_2()
    turn_around()
    paint_black_row_2()
    paint_navy_row_2()
    new_row_left()
    paint_midnightblue_row_3()
    paint_black_row_3()
    paint_navy_row_3()
    new_row_left()
    paint_row_4()
    new_row_right()
    paint_row_5()
    new_row_left()
    paint_row_6()
    new_row_right()
    paint_row_7()
    new_row_left()
    paint_row_8()
    new_row_right()
    paint_row_9()
    new_row_left()
    paint_row_10()
    new_row_right()
    paint_row_11()
    new_row_left()
    paint_row_12()
    new_row_right()
    paint_row_13()
    new_row_left()
    paint_row_14()
    new_row_right()
    paint_row_15()
    new_row_left()
    paint_row_16()
    new_row_right()
    paint_row_17()
    new_row_left()
    paint_row_18()
    new_row_right()
    paint_row_19()
    new_row_left()
    paint_row_20()
    turn_around()


def turn_around():
    turn_left()
    turn_left()

def new_row_right():
    for i in range(3):
        turn_left()
    move()
    for j in range(3):
        turn_left()

def new_row_left():
    turn_left()
    move()
    turn_left()

def paint_black_row_1():
    while front_is_clear():
        paint_corner('Black')
        move()
    paint_corner("Black")

def paint_midnightblue_row_2():
    for i in range(8):
        paint_corner("MidnightBlue")
        move()
    while front_is_clear():
        move()
    paint_corner("MidnightBlue")

def paint_black_row_2():
    move()
    for i in range(7):
        paint_corner("Black")
        move()

def paint_navy_row_2():
    for i in range(4):
        paint_corner("Navy")
        move()
    while front_is_clear():
        move()

def paint_midnightblue_row_3():
    for i in range(3):
        paint_corner("MidnightBlue")
        move()
    for j in range(2):
        move()
    paint_corner("MidnightBlue")
    for k in range(4):
        move()
    paint_corner("MidnightBlue")
    move()
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("MidnightBlue")
    while front_is_clear():
        move()
    paint_corner("MidnightBlue")
    turn_around()
        
def paint_black_row_3():
    move()
    for i in range(6):
        paint_corner("Black")
        move()
    
def paint_navy_row_3():
    while front_is_clear():
        if corner_color_is("MidnightBlue"):
            move()
        else:
            paint_corner("Navy")
            move()
def paint_row_4():
    for i in range(2):
        paint_corner("MidnightBlue")
        move()
    for j in range(4):
        paint_corner("Navy")
        move()
    for k in range(4):
        paint_corner("MidnightBlue")
        move()
    paint_corner("Gold")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Gold")
    move()
    for l in range(6):
        paint_corner("Black")
        move()
    paint_corner("Navy")

def paint_row_5():
    paint_corner("Navy")
    move()
    for i in range(5):
        paint_corner("Black")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Navy")
    move()
    for j in range(2):
        paint_corner("DarkBlue")
        move()
    for k in range(3):
        paint_corner("Navy")
        move()
    for l in range(2):
        paint_corner("DarkBlue")
        move()
    for m in range(2):
        paint_corner("Navy")
        move()
    for n in range(2):
        paint_corner("MidnightBlue")
        move()
    paint_corner("MidnightBlue")

def paint_row_6():
    paint_corner("DarkBlue")
    move()
    for i in range(6):
        paint_corner("MediumBlue")
        move()
    for j in range(6):
        paint_corner("DarkBlue")
        move()
    paint_corner("MediumBlue")
    move()
    paint_corner("DarkBlue")
    move()
    for k in range(3):
        paint_corner("Black")
        move()
    for l in range(2):
        paint_corner("DarkBlue")
        if front_is_clear():
            move()
    
def paint_row_7():
    paint_corner("MediumBlue")
    move()
    paint_corner("DarkBlue")
    move()
    for i in range(3):
        paint_corner("Black")
        move()
    for j in range(2):
        paint_corner("LightSkyBlue")
        move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    for k in range(5):
        paint_corner("Navy")
        move()
    for l in range(2):
        paint_corner("DarkBlue")
        move()
    for m in range(2):
        paint_corner("Navy")
        move()
    paint_corner("MediumBlue")

def paint_row_8():
    paint_corner("MediumBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("DarkBlue")
    move()
    for i in range(2):
        paint_corner("CornflowerBlue")
        move()
    for j in range(4):
        paint_corner("LightBlue")
        move()
    paint_corner("MediumBlue")
    move()
    paint_corner("LightBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("LightBlue")
    move()
    for k in range(2):
        paint_corner("DarkBlue")
        move()
    paint_corner("Black")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Black")
    move()
    for l in range(2):
        paint_corner("RoyalBlue")
        if front_is_clear():
            move()

def paint_row_9():
    paint_corner("Blue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("Black")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("Yellow")
    move()
    paint_corner("Gold")
    move()
    for i in range(2):
        paint_corner("Navy")
        move()
    for j in range(2):
        paint_corner("DarkBlue")
        move()
    paint_corner("Navy")
    move()
    for k in range(2):
        paint_corner("RoyalBlue")
        move()
    paint_corner("DarkBlue")
    move()
    paint_corner("LightBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    for l in range(2):
        paint_corner("DarkBlue")
        if front_is_clear():
            move()

def paint_row_10():
    paint_corner("DarkBlue")
    move()
    for i in range(2):
        paint_corner("CornflowerBlue")
        move()
    paint_corner("LightBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("Navy")
    move()
    for j in range(2):
        paint_corner("MediumBlue")
        move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("Navy")
    move()
    for k in range(2):
        paint_corner("Yellow")
        move()
    paint_corner("Navy")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Black")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("MediumBlue")
    
def paint_row_11():
    paint_corner("DarkBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("Black")
    move()
    paint_corner("MidnightBlue")
    move()
    for i in range(2):
        paint_corner("Navy")
        move()
    paint_corner("DarkBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    for j in range(2):
        paint_corner("CornflowerBlue")
        move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("LightBlue")
    move()
    for k in range(2):
        paint_corner("CornflowerBlue")
        if front_is_clear():
            move()
        
def paint_row_12():
    for i in range(2):
        paint_corner("LightBlue")
        move()
    paint_corner("DarkBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("MidnightBlue")
    move()
    for i in range(2):
        paint_corner("LightSkyBlue")
        move()
    paint_corner("DarkBlue")
    move()
    for j in range(2):
        paint_corner("RoyalBlue")
        move()
    paint_corner("MediumBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    for k in range(3):
        paint_corner("Navy")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Black")
    move()
    for l in range(2):
        paint_corner("MediumBlue")
        if front_is_clear():
            move()
        
def paint_row_13():
    paint_corner("DarkBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("Black")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("Gold")
    move()
    paint_corner("Navy")
    move()
    for i in range(2):
        paint_corner("LightSkyBlue")
        move()
    paint_corner("DarkBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("MidnightBlue")
    
def paint_row_14():
    paint_corner("RoyalBlue")
    move()
    for i in range(4):
        paint_corner("DarkBlue")
        move()
    for j in range(2):
        paint_corner("MediumBlue")
        move()
    paint_corner("DarkBlue")
    move()
    paint_corner("MediumBlue")
    move()
    for k in range(2):
        paint_corner("RoyalBlue")
        move()
    paint_corner("DarkBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("CornflowerBlue")
    move()
    for l in range(2):
        paint_corner("LightSkyBlue")
        move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("Black")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("CornflowerBlue")
    
def paint_row_15():
    paint_corner("DarkBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("MediumBlue")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("MediumBlue")
    move()
    for i in range(2):
        paint_corner("DarkBlue")
        move()
    paint_corner("RoyalBlue")
    move()
    for j in range(2):
        paint_corner("LightSkyBlue")
        move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("DarkBlue")
    
def paint_row_16():
    paint_corner("CornflowerBlue")
    move()
    paint_corner("Yellow")
    move()
    for i in range(2):
        paint_corner("Gold")
        move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("DarkBlue")
    move()
    for j in range(3):
        paint_corner("MidnightBlue")
        move()
    for k in range(2):
        paint_corner("RoyalBlue")
        move()
    for l in range(3):
        paint_corner("MediumBlue")
        move()
    paint_corner("Gold")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("MidnightBlue")
    
def paint_row_17():
    for i in range(2):
        paint_corner("Navy")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Yellow")
    move()
    paint_corner("Navy")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("Navy")
    move()
    for j in range(3):
        paint_corner("MediumBlue")
        move()  
    paint_corner("Navy")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("Yellow")
    move()
    paint_corner("Gold")
    move()
    paint_corner("Yellow")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("CornflowerBlue")
    
def paint_row_18():
    paint_corner("CornflowerBlue")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("Gold")
    move()
    paint_corner("Yellow")
    move()
    paint_corner("LightSkyBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("Gold")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Gold")
    move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("DarkBlue")
    move()
    for i in range(2):
        paint_corner("Navy")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("Navy")

def paint_row_19():
    for i in range(2):
        paint_corner("Navy")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("Gold")
    move()
    paint_corner("Navy")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("Navy")
    move()
    paint_corner("MidnightBlue")
    move()
    for j in range(2):
        paint_corner("Navy")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("CornflowerBlue")
    move()
    for k in range(2):
        paint_corner("LightSkyBlue")
        move()
    paint_corner("CornflowerBlue")
    move()
    paint_corner("RoyalBlue")
    
def paint_row_20():
    paint_corner("RoyalBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    paint_corner("DarkBlue")
    move()
    paint_corner("RoyalBlue")
    move()
    for i in range(2):
        paint_corner("DarkBlue")
        move()
    for j in range(2):
        paint_corner("MidnightBlue")
        move()
    for k in range(3):
        paint_corner("DarkBlue")
        move()
    for l in range(2):
        paint_corner("MidnightBlue")
        move()
    for m in range(3):
        paint_corner("DarkBlue")
        move()
    paint_corner("MidnightBlue")
    move()
    paint_corner("DarkBlue")
    
    












# don't change this code
if __name__ == '__main__':
    
    main()