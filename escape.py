def new_coord(x: int, y:int, vx:int, vy: int, w:int, h:int) -> list:
    if vx<0:
        tx = abs(x/vx)
    elif vx>0:
        tx = abs((w-x)/vx)
    else:
        tx = float('inf')
    if vy<0:
        ty = abs(y/vy)
    elif vy>0:
        ty = abs((h-y)/vy)
    else:
        ty = float('inf')
    if tx < ty:
        t = tx
    else:
        t = ty
    x = round(x + vx*t)
    y = round(y + vy*t)
    if (x==0 or x==w) and (y==0 or y==h):
        vx = -vx
        vy = -vy
    elif x==0 or x==w:
        vx = -vx
        vy = vy
    elif y==0 or y==h:
        vx = vx
        vy = -vy
    return [x,y,vx,vy]
        


def escape(container: list, fly: list) -> bool:
    #pdb.set_trace()
    w,h,d = container
    x,y,vx,vy = fly
    hole_center = w/2
    hole_left_border = round(hole_center - d/2)
    hole_right_border = round(hole_center + d/2)
    n = 0
    while n < 20:
        n += 1
        x,y,vx,vy = new_coord(x,y,vx,vy,w,h)
        if hole_left_border < x < hole_right_border and y==h:
            return True   
    return False


if __name__ == '__main__':
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    print()
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    print()
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    print()
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    print()
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
