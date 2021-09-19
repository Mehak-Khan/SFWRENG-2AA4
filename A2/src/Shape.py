## @file Shape.py
#  @author Mehak Khan
#  @brief An interface for modules that implement shape entities
#  @date February 2nd, 2021

from abc import ABC, abstractmethod

## @brief Shape provides an interface for shape entities
#  @details The methods in the interface are abstract and have to
#   be overriden by modules to be implemented


class Shape(ABC):

    @abstractmethod
    ## @brief A generic method for x coordinate of center of mass
    #  @return A real number indicating the x coordinate of center of mass
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief A generic method for y coordinate of center of mass
    #  @return A real number indicating the y coordinate of center of mass
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief A generic method for the mass of a 2D shape
    #  @return A real number indicating the mass of a 2D shape
    def mass(self):
        pass

    @abstractmethod
    ## @brief A generic method for the moment of inertia of a 2D shape
    #  @return A real number indicating the moment of inertia of a 2D shape
    def m_inert(self):
        pass
