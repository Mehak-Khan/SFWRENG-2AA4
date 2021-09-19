## @file triangle_adt.py
#  @author Mehak Khan
#  @brief Contains a class for working with triangles
#  @date 13 January 2021

import math
from enum import Enum, auto

## @brief An enumerated type for type of triangle
#  @details A triangle is either one of the following types: isosceles, right, scalene or equilateral.

class TriType(Enum):
  equilat = auto()
  isosceles = auto()
  right = auto()
  scalene = auto()

## @brief An abstract data type for triangles
#  @details A triangle is composed of three side lengths

class TriangleT:

## @brief Constructor for TriangleT
#  @details Creates instance of a ComplexT based on three side lengths. Assume that the type of side lengths provided will be Integer.
#  @throws Exception If the triangle lengths do not form a valid triangle or have negative or 0 lengths.
#  @param x Integer representing side 1 of a triangle
#  @param y Integer representing side 2 of a triangle
#  @param z Integer representing side 3 of a triangle

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    if (self.is_valid() == False or self.x < 1 or self.y < 1 or self.z < 1 ):
      raise Exception("Invalid Triangle!")

## @brief Gets the side lengths of a triangle
#  @return Tuple of the three side lengths of the triangle

  def get_sides(self):
    return (self.x, self.y, self.z)

## @brief Checks equality of two triangles
#  @details Two trianges are equal if they have the same side lengths. Assume the orientation of triangle does not matter.
#  @param t TriangleT The triangle to compare equality with
# @return Boolean indicating if the triangles are equal

  def equal(self, t):
    sorted_self = sorted(self.get_sides())
    sorted_t = sorted(t.get_sides())
    return (sorted_self == sorted_t)

## @brief Calculates the perimeter of a triangle
#  @return Integer representing the perimeter value of the triangle

  def perim(self):
    return self.x + self.y + self.z

#From: https://en.wikipedia.org/wiki/Heron%27s_formula#:~:text=In%20geometry%2C%20Heron's%20formula%20(sometimes,distances%20in%20the%20triangle%20first.
## @brief Calculates the area of a triangle
#  @details The area is calculated with the three sides of the triangle using Heron's formula
#  @return Float representing the area of the triangle

  def area(self):
    p = self.perim()/2
    return math.sqrt(p*(p-self.x)*(p-self.y)*(p-self.z))

# From: https://www.geeksforgeeks.org/check-whether-triangle-valid-not-sides-given/#:~:text=Approach%3A%20A%20triangle%20is%20valid,three%20conditions%20should%20be%20met.
## @brief Calculates if the sides of the current triangle form a valid triangle
#  @details A valid triangle is formed when the sum of any two sides is greater than the third side.
#  @return Boolean indicating the validity of the triangle

  def is_valid(self):
    return (self.x + self.y > self.z and self.x + self.z > self.y and self.y + self.z > self.x)

## @brief Calculates the type of the current triangle 
#  @details A triangle is equilateral if all the sides have the same side length, isosceles if two sides have the same length, right is the sum of the square of two side lengths equals the square of the third side length, and scalene if it meets none of these and has 3 different side lengths. Assume the priority of triangle types is in the order Equilateral, Isosceles, Right and Scalane.
#  @return TriType The type of triangle - isosceles, scalene, right or equilateral

  def tri_type(self):
    if self.x == self.y and self.x == self.z and self.y == self.z:
      return TriType.equilat
    elif (self.x == self.y or self.x == self.z or self.y == self.z):
      return TriType.isosceles
    elif self.x*self.x + self.y*self.y == self.z*self.z or self.y*self.y + self.z*self.z == self.x*self.x or self.z*self.z + self.x*self.x == self.y*self.y:
      return TriType.right
    else:
      return TriType.scalene
    
    













