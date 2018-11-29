def sun_angle(time):
    hour, minutes = [int(x) for x in time.split(':')]
    t_minutes  =  60*hour + minutes 
    sunrise, sunset = 360, 1080
    if sunrise <= t_minutes <=  sunset:
        return round((t_minutes-sunrise)/720*180,2)
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("all good")
