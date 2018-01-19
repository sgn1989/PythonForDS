def cylinder_surface_area(radius, height, has_top_and_bottom):
    """ Function to compute surface area of cylinder

    radius: int or float. Radius of the cylinder
    height: int or float. Height of the cylinder
    has_top_and_bottom: boolean. Variable to denote if cylinder is full or hollow.
    """
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return 2 * top_area + side_area
    else:
        return side_area

print(cylinder_surface_area(10, 5, True))
