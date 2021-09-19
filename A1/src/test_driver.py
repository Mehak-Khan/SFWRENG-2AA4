## @file test_driver.py
#  @author Mehak Khan
#  @brief Tests for complex_adt.py and triangle_adt.py
#  @date 14 January 2021

import math
from complex_adt import ComplexT
from triangle_adt import TriangleT, TriType

#ComplexT used for testing
testComplex = ComplexT(2.56,5.34)
negativeImag = ComplexT(5.33, -5.05)
negativeReal = ComplexT(-4, 7.0)
negativeComplex = ComplexT (-7.33, -33.56)
zeroComplex = ComplexT(0.0,0.0)
zeroReal = ComplexT(0.0, 44.0)
zeroRealNeg = ComplexT(0.0, -100.3)
zeroImag = ComplexT(8.5, 0.0)
zeroImagNeg = ComplexT(-4.7, 0.0)

# Keeping track of total tests and tests passed
totTest = 0
passed = 0

#Testing approximate equality due to Python floating point arithmetic
#From: https://www.python.org/dev/peps/pep-0485/#proposed-implementation
def isClose(a, b, rel_tol = 1e-05, abs_tol = 0.0):
  return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

#Test the real number getter
def test_real():
  global totTest, passed
  totTest += 1

  try:
    expected_real = 2.56
    #TEST CASE 1: get real 
    assert (testComplex.real() == expected_real)
    passed += 1
    print ("real() test passed")
  except AssertionError:
    print ("real() test failed")
   
   

#Test the imaginary number getter
def test_imag():
  global totTest, passed
  totTest += 1
 
  try:
    expected_imag = 5.34
    #TEST CASE 1: get imaginary
    assert(testComplex.imag() == expected_imag)
    passed += 1
    print("imag() test passed")
  except AssertionError:
   print("imag() test failed")

#Test the absolute value calculation. Use isClose.
def test_get_r():
  global totTest, passed
  totTest += 1
 
  try: 
    #TEST CASE 1: get absolute value with zero real part
    expected_answer = 44.0
    assert(zeroReal.get_r() == expected_answer)

    #TEST CASE 2: get absolute value normal 
    expected_ans = 5.9219254
    assert isClose(testComplex.get_r(), expected_ans)

    passed += 1
    print("get_r() test passed")
  except AssertionError:
   print("get_r() test failed")

#Test the argument calculation. Use isClose to test.
def test_get_phi():
  global totTest, passed
  totTest += 1

  try:

    #TEST CASE 1: Test negative real part and 0 imaginary part
    expected_and_zeroImagNeg = 3.14159265359
    assert isClose(zeroImagNeg.get_phi(), expected_and_zeroImagNeg)

    #TEST CASE 2: Test negative real part and negative imaginary part
    expected_ans_negativeComplex = -1.78583409192
    assert isClose(negativeComplex.get_phi(), expected_ans_negativeComplex)
   
    #TEST CASE 3: Test positive real part and 0 imaginary part
    expected_ans_zeroImag = 0.0
    assert isClose(zeroImag.get_phi(), expected_ans_zeroImag)

    #TEST CASE 4: Test zero complex number
    expected_ans_zeroComplex = 0.0
    assert isClose(zeroComplex.get_phi(), expected_ans_zeroComplex)

    #TEST CASE 5: Test zero real part with positive imaginary part
    expected_ans_zeroReal = 1.57079632679
    assert isClose(zeroReal.get_phi(), expected_ans_zeroReal)

    #TEST CASE 6: Test zero real part with negative imaginary part
    expected_ans_zeroRealNeg = -1.57079632679
    assert isClose(zeroRealNeg.get_phi(), expected_ans_zeroRealNeg)

    #TEST CASE 7: Test non zero real part complex number
    expected_ans_negativeImag = -0.758429752
    assert isClose(negativeImag.get_phi(), expected_ans_negativeImag)

    passed+= 1
    print("get_phi() test passed")
 
  except AssertionError:
    print("get_phi() test failed")

 

#Test equality of two complex numbers
def test_equal():

  global totTest, passed
  totTest += 1

  try:
    #TEST CASE 1: Equal numbers
    assert(zeroImag.equal(zeroImag))

    #TEST CASE 2: Unequal numbers
    assert(not zeroImag.equal(zeroReal))

    passed+=1
    print("equal() test passed")
  except AssertionError:
    print("equal() test failed")

#Test the conjugate of a complex number calculation
def test_conj():
  global totTest, passed
  totTest += 1 
 
  try:
    #TEST CASE 1: Test positive imaginary number 
    expected_ans_real = 2.56
    expected_ans_imag = -5.34
    assert(testComplex.conj().real() == expected_ans_real )
    assert(testComplex.conj().imag() == expected_ans_imag )

    #TEST CASE 2: Test negative imaginary number
    expected_ans_real = 5.33
    expected_ans_imag = 5.05
    assert(negativeImag.conj().real() == expected_ans_real )
    assert(negativeImag.conj().imag() == expected_ans_imag )

    passed +=1
    print("conj() test passed")

  except AssertionError:
    print("conj() test failed")

#Test the adding complex numbers calculation
def test_add():
  global totTest, passed
  totTest += 1
 
  try:
    expected_ans_real = -1.44
    expected_ans_imag = 12.34

    #TEST CASE 1: Addition
    assert(testComplex.add(negativeReal).real() == expected_ans_real)
    assert(testComplex.add(negativeReal).imag() == expected_ans_imag)

    #TEST CASE 2: Addition with zero
    assert(testComplex.add(zeroComplex).real() == testComplex.real())
    assert(testComplex.add(zeroComplex).imag() == testComplex.imag())

    passed+=1 
    print("add() test passed")

  except AssertionError:
   print("add() test failed")

#Test the subtraction. Use isClose to test.
def test_sub():
  global totTest, passed
  totTest += 1
  
  try:
    expected_ans_real = 6.56
    expected_ans_imag = -1.66
 
    #TEST CASE 1: Subtraction 

    assert isClose (testComplex.sub(negativeReal).real(), expected_ans_real)
    assert isClose(testComplex.sub(negativeReal).imag(), expected_ans_imag)

    #TEST CASE 2: Subtracting zero
    assert(testComplex.sub(zeroComplex).real() == testComplex.real())
    assert(testComplex.sub(zeroComplex).imag() == testComplex.imag())

    passed+=1 
    print("sub() test passed")

  except AssertionError:
    print("sub() test failed")

#Test the multiplication calculation. Use isClose to test.
def test_mult():
  global totTest, passed
  totTest += 1

  try:
    #TEST CASE 1: Normal test case
    expected_ans_real = -47.62
    expected_ans_imag = -3.44
    assert isClose(testComplex.mult(negativeReal).real(), expected_ans_real)
    assert isClose(testComplex.mult(negativeReal).imag(), expected_ans_imag)

    #TEST CASE 2: Test multiplication with zero complex number 
    expected_ans_real = 0.0
    expected_ans_imag = 0.0
    assert isClose(testComplex.mult(zeroComplex).real(), expected_ans_real)
    assert isClose(testComplex.mult(zeroComplex).imag(), expected_ans_imag)

    passed+=1
    print("mult() test passed")

  except AssertionError:
    print("mult() test failed")

#Test the reciprocal of complex number. Use isClose to test.
def test_recip():
  global totTest, passed
  totTest += 1
  try:
    #TEST CASE 1: Normal Test Case
    expected_ans_real = 0.07299852862
    expected_ans_imag = -0.1522703683
    assert isClose(testComplex.recip().real(), expected_ans_real)
    assert isClose(testComplex.recip().imag(), expected_ans_imag)

    #TEST CASE 2: Test zero imaginary part
    expected_ans_real = -0.21276595744
    expected_ans_imag = 0.0
    assert isClose(zeroImagNeg.recip().real(), expected_ans_real)
    assert isClose(zeroImagNeg.recip().imag(), expected_ans_imag)

    #TEST CASE 3: Test zero real part
    expected_ans_real = 0.0
    expected_ans_imag = -0.02272727272
    assert isClose(zeroReal.recip().real(), expected_ans_real)
    assert isClose(zeroReal.recip().imag(), expected_ans_imag)

    #TEST CASE 4: Test zero complex number
    #Expected result: Undefined
    try:
      zeroComplex.recip()
      print("recip() test failed")

    except ZeroDivisionError:
      passed+=1
      print("recip() test passed")

  except AssertionError:
    print("recip() test failed")

#Test division. Use isClose to test.
def test_div():
  global totTest, passed
  totTest += 1
  try:
    #TEST CASE 1: Normal test case
    expected_ans_real = 0.41753846153
    expected_ans_imag = -0.6043076923
    assert isClose(testComplex.div(negativeReal).real(), expected_ans_real)
    assert isClose(testComplex.div(negativeReal).imag(), expected_ans_imag)

    #TEST CASE 2: Test division by zero imaginary part
    expected_ans_real = 0.30117647058
    expected_ans_imag = 0.62823529411
    assert isClose(testComplex.div(zeroImag).real(), expected_ans_real)
    assert isClose(testComplex.div(zeroImag).imag(), expected_ans_imag)

    #TEST CASE 3: Test division by zero real part
    expected_ans_real = -0.05324027916
    expected_ans_imag = 0.02552342971
    assert isClose(testComplex.div(zeroRealNeg).real(), expected_ans_real)
    assert isClose(testComplex.div(zeroRealNeg).imag(), expected_ans_imag)

    try:
      #TEST CASE 4: Test divison by zero complex number
      #Raise ZeroDivisonError: Undefined
      testComplex.div(zeroComplex)
      print("div() test failed")

    except ZeroDivisionError:
      passed+=1
      print("div() test passed")

  except AssertionError:
    print("div() test failed")

#Test square root of complex number. Use isClose to test. 
def test_sqrt():
  global totTest, passed
  totTest += 1
  try:
    #TEST CASE 1: Normal Test Case
    expected_ans_real = 2.0593598
    expected_ans_imag = 1.2965195
    assert isClose(testComplex.sqrt().real(), expected_ans_real)
    assert isClose(testComplex.sqrt().imag(), expected_ans_imag)
  
    #TEST CASE 2: Test zero imaginary part with negative real part
    expected_ans_real = 0.0
    expected_ans_imag = 2.1679483
    assert isClose(zeroImagNeg.sqrt().real(), expected_ans_real)
    assert isClose(zeroImagNeg.sqrt().imag(), expected_ans_imag)

    #TEST CASE 3: Test zero imaginary part with positive real part
    expected_ans_real = 2.9154759
    expected_ans_imag = 0.0
    assert isClose(zeroImag.sqrt().real(), expected_ans_real)
    assert isClose(zeroImag.sqrt().imag(), expected_ans_imag)

    #TEST CASE 4: Test zero real part
    expected_ans_real = 4.6904158
    expected_ans_imag = 4.6904158
    assert isClose(zeroReal.sqrt().real(), expected_ans_real)
    assert isClose(zeroReal.sqrt().imag(), expected_ans_imag)

    #TEST CASE 5: Test zero complex number
    expected_ans_real = 0.0
    expected_ans_imag = 0.0
    assert isClose(zeroComplex.sqrt().real(), expected_ans_real)
    assert isClose(zeroComplex.sqrt().imag(), expected_ans_imag)

    passed+=1
    print("sqrt() test passed")


  except AssertionError:
    print("sqrt() test failed")


#TriangleT objects for testing
validTriangle = TriangleT(7,10,5)
validTriangleEqual = TriangleT(5,7,10)
scaleneTriangle = TriangleT(2,3,4)
isoscelesTriangle = TriangleT(5,5,2)
equilateralTriangle = TriangleT(10,10,10)
rightTriangle = TriangleT(8,10,6)

#Keep track of passed and total tests
passedT = 0
totTestT = 0

#Test for constructor creating an invalid triangle - should raise Exception
def test_constructor():
  global totTestT, passedT
  totTestT+=1
  #TEST CASE 1: Create invalid triangle
  try:
    invalidTriangle = TriangleT(5,2,2)
    print("Constructor test failed")
  except Exception:
    passedT+=1
    print("Constructor test passed")

#Test for getting side lengths of triangle 
def test_get_sides():
  global passedT, totTestT
  totTestT += 1
  try:
    #TEST CASE 1: Normal test case
    side1 = 7
    side2 = 10
    side3 = 5
    assert(validTriangle.get_sides()[0] == side1)
    assert(validTriangle.get_sides()[1] == side2)
    assert(validTriangle.get_sides()[2] == side3)
    passedT+= 1
    print("get_sides() test passed") 

  except AssertionError:
    print("get_sides() test failed")

#Test for equality of triangles
def test_equal_T():
  global passedT, totTestT
  totTestT+= 1

  try:
    #TEST CASE 1: Test with same ordering of side lengths 
    assert(validTriangle.equal(validTriangle))

    #TEST CASE 2: Test with different orientation of triangle
    assert(validTriangle.equal(validTriangleEqual))

    #TEST CASE 3: Test unequal triangles
    assert (not validTriangle.equal(isoscelesTriangle))

    passedT += 1
    print("test_equal() test passed")

  except AssertionError:
    print("equal() test failed")

#Test for perimeter of triangle
def test_perim():
  global passedT, totTestT
  totTestT +=1 

  try:
    #TEST CASE 1: Calculate perimeter
    validTriangleP = 22
    assert(validTriangle.perim() == validTriangleP)
    passedT+=1
    print("perim() test passed")

  except AssertionError:
    print("perim() test failed")

#Test for area of triangle. Use isClose to test.
def test_area():
  global passedT, totTestT
  totTestT += 1

  try:
    #TEST CASE 1: Normal test case for area
    validTriangleA = 16.24808
    assert isClose(validTriangle.area(), validTriangleA)

    passedT += 1
    print ("area() test passed")

  except AssertionError:
    print("area() test failed")

#Test for validity of triangle
def test_is_valid():
  global passedT, totTestT
  totTestT+= 1
  try:
    #TEST CASE 1: Test valid triangle. Invalid triangles cannot be constructed.
    assert(validTriangle.is_valid() == True)
    passedT+= 1
    print("is_valid() test passed")

  except AssertionError:
    print("is_valid() test failed")

#Test the types of triangle 
def test_tri_type():
  global passedT, totTestT
  totTestT+= 1
  try:
    #TEST CASE 1: Scalene - Priority 4
    assert(scaleneTriangle.tri_type() == TriType.scalene)
    #TEST CASE 2: Right - Priority 3
    assert(rightTriangle.tri_type() == TriType.right)
    #TEST CASE 3: Isosceles - Priority 2
    assert(isoscelesTriangle.tri_type() == TriType.isosceles)
    #TEST CASE 4: Equilateral - Priority 1
    assert(equilateralTriangle.tri_type() == TriType.equilat)
    passedT+=1
    print("tri_type() test passed")
  except AssertionError:
    print("tri_type() test failed")
   





#Call the tests for complex_adt.py
print("Tests for complex.adt:\n")
test_real()
test_imag()
test_get_r()
test_get_phi()
test_equal()
test_conj()
test_add()
test_sub()
test_mult()
test_recip()
test_div()
test_sqrt()
print('\n',passed,"of ",totTest,"passed for complex_adt")

#Call the tests for triangle_adt.py
print("\nTests for triangle.adt:\n")
test_constructor()
test_get_sides()
test_equal_T()
test_perim()
test_area()
test_is_valid()
test_tri_type()
print('\n',passedT,"of ",totTestT,"passed for triangle_adt")






