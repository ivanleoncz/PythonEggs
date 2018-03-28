#!/usr/bin/python3


def answer(area): # -> 43
    solar_panels = []
    while area != 0:
        # initial area from function input, later on updated
        high = area
        low  = 1
        print("\nHigh:", high)
        print("Low: ", low)
        while (high - low) > 1:
            ans = (high + low) // 2
            squared = ans**2
            if squared > area:
                high = ans
            elif squared < area:
                low = ans 
        panel = low**2
        solar_panels.append(panel)
        print("Solar Panel:", panel,"->",low)
        # updating area for the remainder of the solar panel area
        area = area - panel 
        # reseting low variable
        low = 1
    return solar_panels

area = int(input("\nArea of Solar Panels: "))
print(answer(area))


