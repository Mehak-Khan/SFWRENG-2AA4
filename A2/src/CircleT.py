## @file CircleT.py
#  @author Mehak Khan
#  @brief Contains the CircleT type to represent circles as a shape
#  @date February 2nd, 2021

from Shape import Shape

## @brief CircleT is a class the implements an ADT for the concept of
#   shapes moving through 2D space
#  @details The ADT contains the x, y coordinate of center of mass,
#   mass and radius of the circle


class CircleT(Shape):

    ## @brief Constructor for CircleT
    #  @details The constructor assumes that the arguments provided to the access program will
    #  of the correct type.
    #  @throws ValueError If the radius or mass arguments provided are not greater than 0
    #  @param x Representing x coordinate of center of mass
    #  @param y Representing y coordinate of center of mass
    #  @param r Representing radius of circle
    #  @param m Representing mass of circle
    def __init__(self, x, y, r, m):
        if (not (r > 0 and m > 0)):
            raise ValueError
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    ## @brief Getter for the x coordinate of center of mass
    #  @return Real number representing x coordinate of center of mass
    def cm_x(self):
        return self.x

    ## @brief Getter for the y coordinate of center of mass
    #  @return Real number representing the y coordinate of center of mass
    def cm_y(self):
        return self.y

    ## @brief Getter for the mass of the circle
    #  @return Real number representing mass of circle
    def mass(self):
        return self.m

    ## @brief Calculates the moment of inertia of the circle
    #  @return Real number representing the moment of inertia of the circle
    def m_inert(self):
        return ((self.m * (self.r * self.r)) / 2)
