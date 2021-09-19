## @file Scene.py
#  @author Mehak Khan
#  @brief Contains the Scene type for simulation of masses
#  @date 3rd February, 2021

from scipy.integrate import odeint


## @brief Scene class is responsible for representing simulation of
#   objects in 2D space
#  @details Implements the ADT for Scene class. The ADT contains
#   the shapes in 2D space, velocities in x, y directions and
#   forces in x, y directions.


class Scene():

    ## @brief Constructor for Scene class
    #  @param s Shape object
    #  @param Fx Unbalanced force function in x direction
    #  @param Fy Unbalanced force function in y direction
    #  @param Vx Initial velocity in x direction
    #  @param Vy Initial velocity in y direction
    def __init__(self, s, Fx, Fy, Vx, Vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.Vx = Vx
        self.Vy = Vy

    ## @brief Getter for the shape object state variable
    #  @return Shape object
    def get_shape(self):
        return self.s

    ## @brief Getter for the unbalanced forces
    #  @return A tuple of the unbalanced force functions in x and y direction
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief Getter for the inital velocities
    #  @return A tuple of the initial velocities in x and y direction
    def get_init_velo(self):
        return self.Vx, self.Vy

    ## @brief Mutator to set the shape object
    #  @param s1 new shape object
    def set_shape(self, s1):
        self.s = s1

    ## @brief Mutator to set the unbalanced forces
    #  @param fx the unabalanced force function in x direction
    #  @param fy the unbalanced force function in y direction
    def set_unbal_forces(self, fx, fy):
        self.Fx = fx
        self.Fy = fy

    ## @brief Mutator to set the intial velocities
    #  @param vx the initial velocity in x direction
    #  @param vy the initial velocity in y direction
    def set_init_velo(self, vx, vy):
        self.Vx = vx
        self.Vy = vy

    ## @brief Calculates ode for simulation of 2D objects in space
    #  @param t_final Real number representing final time
    #  @param n_steps Natural number representing number of time intervals
    #  @return A tuple of sequence of real numbers representing time and four sequences
    #   of sequences of real numbers representing the ode integration
    def sim(self, t_final, n_steps):
        t = []
        for i in range(n_steps):
            t.append((i * t_final) / (n_steps - 1))

        ode_seq = odeint(self.__ode, [self.s.cm_x(), self.s.cm_y(), self.Vx, self.Vy], t)

        return t, ode_seq

    ## @brief A local function for ordinary differential equation
    #  @param w A sequence of real numbers representing position and velocity
    #  @param t A real number representing time
    #  @return A sequence of real numbers used to calculate ode integration
    def __ode(self, w, t):
        return [w[2], w[3], self.Fx(t) / self.s.mass(), self.Fy(t) / self.s.mass()]
