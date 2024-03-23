import matplotlib.pyplot as plt
import numpy as np

image_path ="ata.png"
image = plt.imread(image_path)

image_width_cm = 21
image_height_cm = 29.7

image_height, image_width, _ = image.shape

def scale_coordinates(x, y):
    scaled_x = x / image_width * image_width_cm
    scaled_y = (image_height - y) / image_height * image_height_cm
    return scaled_x, scaled_y

element_coordinates = {'x': [], 'y': []}

def onclick(event):
    x_pixel, y_pixel = event.xdata, event.ydata
    x, y = scale_coordinates(x_pixel, y_pixel)
    
    element_coordinates['x'].append(x)
    element_coordinates['y'].append(y)
    
    plt.imshow(image)
    plt.title('Selected Object with Finite Elements')
    plt.scatter(element_coordinates['x'], element_coordinates['y'], color='red')
    plt.show()

plt.imshow(image)
plt.title('Selected Object')
plt.gca().set_aspect('equal', adjustable='box')
plt.connect('button_press_event', onclick)
plt.show()

print("Scaled Coordinates:")
for x, y in zip(element_coordinates['x'], element_coordinates['y']):
    print(f"({x}, {y})")
