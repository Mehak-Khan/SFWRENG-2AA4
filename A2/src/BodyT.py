## @file BodyT.py
#  @author Mehak Khan
#  @brief  Contains the BodyT type to represent sequence of masses
#  @date February 2nd, 2021

from Shape import Shape

## @brief ShapeT is responsible for representing a system of shapes
#  @details ShapeT is a class that implements the ADT for the concept of shapes in 2D space.
#   The ADT contains the x, y coordinate of center of mass,
#   moment of inertia and mass of the body


class BodyT(Shape):

    ## @brief constructor for BodyT
    #  @details The constructor builds a body with the x, y coordinates of center of mass,
    #   mass moment of inertia, and mass of the sequence of masses
    #  @throws ValueError If the lengths of the sequences provided as arguments are not equal
    #   Else if any mass value in the sequence of mass values is not greater than 0
    #  @param x Sequeunce of real numbers representing x coordinate of center of mass
    #  @param y Sequence of real numbers representing  y coordinate of center of mass
    #  @param m Sequence of real numbers representing masses
    def __init__(self, x, y, m):
        if (not (len(x) == len(y) == len(m))):
            raise ValueError
        elif any(u <= 0 for u in m):
            raise ValueError

        self.cmx = self.__cm(x, m)
        self.cmy = self.__cm(y, m)
        self.m = self.__sum(m)
        squared_val = self.cmx * self.cmx + self.cmy * self.cmy
        self.moment = self.__mmom(x, y, m) - self.__sum(m) * squared_val

    ## @brief Getter for the x coordinate of center of mass
    #  @return Real number representing x coordinate of center of mass
    def cm_x(self):
        return self.cmx

    ## @brief Getter for the y coordinate of center of mass
    #  @return Real number representing y coordinate of center of mass
    def cm_y(self):
        return self.cmy

    ## @brief Getter for the mass of the body
    #  @return Real number representing the mass of the body
    def mass(self):
        return self.m

    ## @brief Getter for the moment of inertia of the body
    #  @return Real number representing the moment of inertia of the body
    def m_inert(self):
        return self.moment

    ## @brief Sum up values in a list
    #  @param m List to sum up values of
    #  @return Real number representing the sum of the values in the list
    def __sum(self, m):
        total = 0
        for u in m:
            total = total + u
        return total

    ## @brief Calculate the center of mass of point masses
    #  @param z Sequence of real numbers representing coordinates
    #  @param m Sequence of real numbers representing mass
    #  @return cmx Real number representing the center of mass
    def __cm(self, z, m):
        total = 0
        for i in range(len(m)):
            total = total + (z[i] * m[i])
        return total / self.__sum(m)

    ## @brief Calculate the moment of inertia of point masses
    #  @param x The x coordinate of the centre of mass
    #  @param y The y coordinate of the centre of mass
    #  @param m Sequence of real numbers representing mass of shapes
    #  @return mmom Real number representing the moment of inertia
    def __mmom(self, x, y, m):
        total = 0
        for i in range(len(m)):
            total = total + (m[i] * ((x[i] * x[i]) + (y[i] * y[i])))
        return total
