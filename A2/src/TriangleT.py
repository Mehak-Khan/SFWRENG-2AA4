## @file TriangleT.py
#  @author Mehak Khan
#  @brief Contains the TriangleT type to represent triangles as a shape
#  @date February 2nd, 2021

from Shape import Shape

## @brief TriangleT is a class the implements an ADT for the concept of
#   shapes moving through 2D space
#  @details The ADT contains the x, y coordinate of center of mass,
#   mass and side length of the triangle


class TriangleT(Shape):

    ## @brief Constructor for TriangleT
    #  @details The constructor assumes that the arguments provided to the access program will
    #  of the correct type. The class also assumes that all triangles are equilateral
    #  therefore only one side length is provided.
    #  @throws ValueError If the side length or mass arguments provided are not greater than 0
    #  @param x Representing x coordinate of center of mass
    #  @param y Representing y coordinate of center of mass
    #  @param r Representing side length of triangle
    #  @param m Representing mass of triangle
    def __init__(self, x, y, s, m):
        if (not (s > 0 and m > 0)):
            raise ValueError
        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief Getter for x coordinate of center of mass
    #  @return Real number representing the x coordinate of center of mass
    def cm_x(self):
        return self.x

    ## @brief Getter for the y coordinate of center of mass
    #  @return Real number representing y coordinate of center of mass
    def cm_y(self):
        return self.y

    ## @brief Getter for the mass of the triangle
    #  @return Real number representing mass of triangle
    def mass(self):
        return self.m

    ## @brief Calculates the moment of inertia of the triangle
    #  @return Real number representing the moment of inertia of the triangle
    def m_inert(self):
        return ((self.m * (self.s * self.s)) / 12)
