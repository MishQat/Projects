import math,sys
def shape_2d():
    user_shape_name_2d = input("What shape do you want to take ((1)Circle or (2)Regular Polygon): ")
    user_shape_name_2d_info = input("Area or Circumference: ")
    if user_shape_name_2d == "1" and user_shape_name_2d_info == "Area":
        circle_radi = int(input("input Radius: "))
        circle_area = math.pi*circle_radi**2
        print(f"The area is {circle_area} unit²")
    elif user_shape_name_2d == "Cirlce" and user_shape_name_2d_info == "Circumference":
        circle_radi = int(input("input Radius: "))
        circle_cum = 2*math.pi*circle_radi
        print(f"The circumference is {circle_cum} unit")
    elif user_shape_name_2d == "2":
        polygon_sides = int(input("Input number of side of polygon: "))
        polygon_cum_length_info = float(input("Input apothem for area: "))
        polygon_length = int(input("Input length of a side: "))
        if user_shape_name_2d_info == "Area":
            area_polygon = (polygon_cum_length_info  * (polygon_sides*polygon_length)) * 0.5
            print(f"The are of the regular polygon is {area_polygon} unit²")   
        elif user_shape_name_2d_info =="Perimeter": 
            polygon_perimeter = polygon_length * polygon_sides
            print(f"The perimeter of the regular polygon is {polygon_perimeter} unit")
    else:
        sys.exit()
shape_2d()
