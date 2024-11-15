import math


def main():

    print_efficiency('#1 Picnic', 6.83, 10.16)
    print_efficiency('#1 Tall', 7.78, 11.91)
    print_efficiency('#2', 8.73, 11.59)
    print_efficiency('#2.5', 10.32, 11.91)


def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume



def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area



def storage_efficiency(volume, surface_area):
    
    strg_efficiency = volume / surface_area
    return strg_efficiency


def print_efficiency(name,radius,height):
    volume = compute_volume(radius,height)
    surface = compute_surface_area(radius, height)
    efficiency = storage_efficiency(volume,surface)
    print(f'{name}: {efficiency:.2f}')


main()
