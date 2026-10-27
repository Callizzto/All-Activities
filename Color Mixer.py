colors = input("Enter the colors: ").upper()
if len(colors) == 8:
    for color in colors:
        if color != "R" and color != "B" and color != "Y":
            print("An unidentified color is present, please try again.")
            exit()
    else:
        newcolors = list(colors)
        mixer = {
            ("R", "R"): "R",
            ("B", "B"): "B",
            ("Y", "Y"): "Y",
            ("R", "Y"): "B",
            ("R", "B"): "Y",
            ("Y", "R"): "B",
            ("Y", "B"): "R",
            ("B", "R"): "Y",
            ("B", "Y"): "R"
        }
        p1 = mixer[(newcolors[0], newcolors[1])]
        p2 = mixer[(newcolors[2], newcolors[3])]
        p3 = mixer[(newcolors[4], newcolors[5])]
        p4 = mixer[(newcolors[6], newcolors[7])]
        #print(f"DEBUG: First pairs: {p1}{p2}{p3}{p4}")
        p5 = mixer[(p1, p2)]
        p6 = mixer[(p3, p4)]
        #print(f"DEBUG: Second pairs: {p5}{p6}")
        p7 = mixer[(p5, p6)]
        print(f"Final Color: {p7}")
else:
    print("Length is insufficient or exceeds the 8 characters.")