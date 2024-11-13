"""Compute and print the volume of a right circular cone."""

import math
def main():
  ex_radius = 2.8
  ex_height = 3.2
  ex_vol = cone_volume(ex_radius, ex_height)

  print("This program computes the volume of a right")
  print("circular cone. For example, if the radius of a")
  print(f"cone is {ex_radius} and the height is {ex_height}")
  print(f"then the volume is {ex_vol:.1f}")
  print()

  radius = float(input("Please enter the radius of the cone: "))
  height = float(input("Please enter the height of the cone: "))

  vol = cone_volume(radius, height)

  print(f"Radius: {radius}")
  print(f"Height: {height}")
  print(f"Volume: {vol:.1f}")



def cone_volume(radius, height):
  """Compute and return the volume of a right circular cone."""
  volume = math.pi * radius**2 * height / 3
  return volume


main()