# Create a function named area(), that receives a rectangular ground dimensions (length and width) and show the area.

def area(length, width):
    ground_area = length * width
    print(f'The area of a ground {length} X {width} is {ground_area:.2f}m².')


# main()
length = float(input('Inform the ground length> '))
width = float(input('Now, the width> '))
area(length, width)

input() #wait