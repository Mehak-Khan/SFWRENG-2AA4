## @file complex_adt.py
#  @author Mehak Khan
#  @brief Contains a class for working with complex numbers
#  @date 12th January 2020

import math

## @brief An abstract data type for complex numbers
#  @details A complex number is composed of a real part, and an imaginary part

class ComplexT:

## @brief Constructor for ComplexT
#  @details Creates instance of a ComplexT based on real part and imaginary part of the number. Assumes that user will provide the correct data type for the imaginary and real part.
#  @param x Floating point representing real part of number
#  @param y Floating point representing imaginary part of number

  def __init__(self, x, y):
    self.x = x
    self.y = y

## @brief Gets the real part of the complex number
#  @return Floating point representing the real part of the complex number

  def real (self):
    return self.x

## @brief Gets the imaginary part of the complex number
#  @return Floating point representing the imaginary part of the complex number

  def imag (self):
    return self.y

# Formula from: https://www2.clarku.edu/faculty/djoyce/complex/abs.html#:~:text=For%20a%20complex%20number%20z,on%20the%20real%20number%20line.
## @brief Calculates the absolute value of the complex number
#  @return Floating point representing the absolute value of the complex number

  def get_r (self):
    return math.sqrt(self.x*self.x + self.y*self.y)

# Formula from: https://gubner.ece.wisc.edu/notes/MagnitudeAndPhaseOfComplexNumbers.pdf
## @brief Calculates the argument of the complex number
#  @details The argument of a complex number is calculated using tan inverse. Assume the domain of this argument is (-pi, pi]. If the real part is 0, ZeroDivisionError is handled and the argument is pi/2 if the imaginary part is positive, and -pi/2 if the imaginary part is negative. Assume that the argument of 0 is 0.0.
#  @return Floating point representing the argument of the complex number in radians

  def get_phi (self):
    try:
      if self.x > 0:
        return math.atan(self.y/self.x)
      elif (self.x < 0 and self.y >= 0):
        return math.atan(self.y/self.x) + math.pi
      else:
        return math.atan(self.y/self.x) - math.pi

    except ZeroDivisionError:
      if (self.y > 0):
        return math.radians(90)
      elif (self.y < 0):
        return math.radians(90)*-1
      else:
        return 0.0

## @brief Checks equality of two complex numbers
#  @details Two complex numbers are equal if their real and imaginary part are the same
#  @param c The complex number to compare equality with
#  @return Boolean value indicating if the complex numbers are equal

  def equal(self, c):
    return (self.x == c.real()) and (self.y == c.imag())

# Formula from: https://www.mathcentre.ac.uk/resources/sigma%20complex%20number%20leaflets/sigma-complex6-2009-1.pdf
## @brief Calculates complex conjugate of current complex number
#  @return A complex number that is the cojugate

  def conj(self):
    return ComplexT(self.x, -1*self.y)

# Formula from: https://byjus.com/complex-number-formula/
## @brief Performs addition of two complex numbers
#  @param c The complex number to add to the current complex number
#  @return A complex number that is the result of the addition of the two complex numbers

  def add(self, c):
    return ComplexT(self.x + c.real(), self.y + c.imag())

# Formula from: https://byjus.com/complex-number-formula/
## @brief Subtracts a complex number from the current complex number
#  @param c The complex number that is subtracted from the current complex number
#  @return A complex number that is the result of the subtraction of the two complex numbers

  def sub(self, c):
    return ComplexT(self.x - c.real(), self.y - c.imag())

# Formula from: https://byjus.com/complex-number-formula/
## @brief Multiplies two complex numbers
#  @param c The complex number that is multiplied with the current complex number
#  @return A complex number that is the result of the multiplication of the 2 complex numbers

  def mult(self, c):
    return ComplexT(self.x*c.real() - self.y*c.imag(), self.x*c.imag() + self.y*c.real())

# Formula from: https://tinyurl.com/yxf3zmfr
## @brief Calculates reciprocal of complex number
#  @details The calculation uses division by summation of imaginary part squared and real part squared. If both values are 0, the reciprocal is undefined.
#  @throws ZeroDivisionError If both real and imaginary parts are 0, the reciprocal is undefined.
#  @return A complex number that is the resulting reciprocal

  def recip(self):
    if (self.x == 0 and self.y == 0):
      raise ZeroDivisionError("Undefined")
    else:
      return ComplexT(self.x/(self.x*self.x + self.y*self.y), -1*self.y/(self.x*self.x + self.y*self.y))

# Formula from: https://byjus.com/complex-number-formula/
## @brief Divides current complex number by given complex number
#  @throws ZeroDivisionError If complex number is being divided by a complex number with both real and imaginary parts equal to 0
#  @param c The complex number that is the divisor
#  @return A complex number that is the result of the division of the 2 complex numbers

  def div(self, c):
    if (c.real() == 0 and c.imag() == 0):
      raise ZeroDivisionError("Undefined")
    else:
      return ComplexT((self.x*c.real() + self.y*c.imag())/(c.real()*c.real() + c.imag()*c.imag()), (self.y*c.real() - self.x*c.imag())/(c.real()*c.real() + c.imag()*c.imag()))

# Formula from: https://en.wikipedia.org/wiki/Complex_number#Square_root
## @brief Calculates the positive square root of current complex number 
#  @Details The calculation of the positive square root of a complex number requires that the imaginary part cannot be 0. If the imaginary part is 0, assume the number is a normal number and take the square root of it. If the number is negative, the square root will be an imaginary number.
#  @return A complex number that is the resulting square root

  def sqrt(self):
      if (self.y == 0):
        if (self.x > 0):
          return ComplexT(math.sqrt(self.x), 0.0)
        elif (self.x < 0):
          return ComplexT(0.0, math.sqrt(-self.x))
        else:
          return ComplexT(0.0, 0.0)
      else:
        real = math.sqrt((self.x + self.get_r())/2)
        imaginary = self.y/abs(self.y) * math.sqrt((-1*self.x + self.get_r())/2)
        return ComplexT(real, imaginary)








