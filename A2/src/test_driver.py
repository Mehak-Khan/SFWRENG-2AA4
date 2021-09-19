## @file test_All.py
#  @author Mehak Khan
#  @brief Testing driver
#  @date 5th February, 2021
#  @details This file tests CircleT.py, TriangleT.py, Scene.py, and BodyT.py using pytest.

import pytest
from CircleT import *
from TriangleT import *
from Scene import *
from BodyT import *
import math


class TestCircle:

    def setup_method(self, method):
        self.c1_x = 2.0
        self.c1_y = 5.0
        self.c1_r = 15.0
        self.c1_m = 3.0
        self.c1 = CircleT(self.c1_x, self.c1_y, self.c1_r, self.c1_m)

    def teardown_method(self, method):
        self.c1 = None

    def test_getter_cm_x(self):
        assert self.c1.cm_x() == self.c1_x

    def test_getter_cm_y(self):
        assert self.c1.cm_y() == self.c1_y

    def test_getter_mass(self):
        assert self.c1.mass() == self.c1_m

    def test_inertia(self):
        assert self.c1.m_inert() == 337.5

    def test_exception_mass_zero(self):
        with pytest.raises(ValueError):
            CircleT(1.0, 3.0, 4.0, 0)

    def test_exception_mass_neg(self):
        with pytest.raises(ValueError):
            CircleT(1.0, 3.0, 4.0, -5)

    def test_exception_radius_neg(self):
        with pytest.raises(ValueError):
            CircleT(1.0, 3.0, -10, 20)


class TestTriangle:

    def setup_method(self, method):
        self.t1_x = 3.6
        self.t1_y = 7.8
        self.t1_s = 4.7
        self.t1_m = 1.5
        self.t1 = TriangleT(self.t1_x, self.t1_y, self.t1_s, self.t1_m)

    def teardown_method(self, method):
        self.t1 = None

    def test_getter_cm_x(self):
        assert self.t1.cm_x() == self.t1_x

    def test_getter_cm_y(self):
        assert self.t1.cm_y() == self.t1_y

    def test_getter_mass(self):
        assert self.t1.mass() == self.t1_m

    def test_inertia(self):
        assert self.t1.m_inert() == pytest.approx(2.76125)

    def test_exception_mass_zero(self):
        with pytest.raises(ValueError):
            TriangleT(1.0, 3.0, 4.0, 0)

    def test_exception_mass_neg(self):
        with pytest.raises(ValueError):
            TriangleT(1.0, 3.0, 4.0, -5)

    def test_exception_side_neg(self):
        with pytest.raises(ValueError):
            TriangleT(1.0, 3.0, -6, 20)


class TestBody:

    def setup_method(self, method):
        self.b1_x = [3.6, 4.8, 9.5, 2.3]
        self.b1_y = [7.8, 6.6, 3.7, 2.2]
        self.b1_m = [8.9, 9.9, 1.2, 0.5]
        self.b1 = BodyT(self.b1_x, self.b1_y, self.b1_m)

    def teardown_method(self, method):
        self.b1 = None

    def test_cm_x(self):
        assert self.b1.cm_x() == pytest.approx(4.493170732)

    def test_cm_y(self):
        assert self.b1.cm_y() == pytest.approx(6.843902439)

    def test_mass(self):
        assert self.b1.mass() == pytest.approx(20.5)

    def test_m_inert(self):
        assert self.b1.m_inert() == pytest.approx(71.88753166)

    def test_exception_unequal_length(self):
        with pytest.raises(ValueError):
            BodyT([1, 2], [1, 2], [1])

    def test_2_exception_unequal_length(self):
        with pytest.raises(ValueError):
            BodyT([1], [1], [1, 2])

    def test_exception_zero_mass(self):
        with pytest.raises(ValueError):
            BodyT([1, 2, 3], [2, 3, 4], [5, 9, 0])

    def test_exception_neg_mass(self):
        with pytest.raises(ValueError):
            BodyT([1, 2, 3], [2, 3, 4], [-5, 9, 7])


class TestScene:

    def Fx(self, t):
        return 0

    def Fy(self, t):
        return -self.g * self.m

    def Fx_2(self, t):
        return 3 if t < 5 else 0

    def Fy_2(self, t):
        return -self.g * self.m if t < 3 else self.g * self.m

    def setup_method(self, method):
        self.g = 9.81  # gravity
        self.m = 1  # mass
        self.e = 2e-3  # small

        self.c1 = CircleT(2.7, 7.8, 4.5, 1.0)
        self.t1 = TriangleT(7.7, 4.5, 3.9, 1.0)
        self.b1 = BodyT([1, 3, 4, 0.5], [2, 7, 8, 0.3], [6, 2, 1, 0.2])

        theta = 30
        v = 5.7

        self.s1_Vx = v * math.cos(theta)
        self.s1_Vy = v * math.sin(theta)

        self.s1 = Scene(self.c1, self.Fx, self.Fy, self.s1_Vx, self.s1_Vy)
        self.s2 = Scene(self.t1, self.Fx, self.Fy, 0, 0)
        self.s3 = Scene(self.b1, self.Fx_2, self.Fy_2, 0, 0)

        self.time1, self.ode1 = self.s1.sim(5, 5)
        self.time2, self.ode2 = self.s2.sim(6, 5)
        self.time3, self.ode3 = self.s3.sim(7, 5)

    def teardown_method(self, method):
        self.s1 = None
        self.t1 = None
        self.c1 = None

    def test_getter_s_s1(self):
        assert self.s1.get_shape() == self.c1

    def test_getter_s_s2(self):
        assert self.s2.get_shape() == self.t1

    def test_getter_s_s3(self):
        assert self.s3.get_shape() == self.b1

    def test_getter_vx_s1(self):
        assert self.s1.get_init_velo() == (self.s1_Vx, self.s1_Vy)

    def test_getter_vx_s2(self):
        assert self.s2.get_init_velo() == (0, 0)

    def test_getter_vx_s3(self):
        assert self.s3.get_init_velo() == (0, 0)

    def test_setter_s1(self):
        self.s1.set_shape(self.t1)
        assert self.s1.get_shape() == self.t1

    def test_setter_s2(self):
        self.s2.set_shape(self.b1)
        assert self.s2.get_shape() == self.b1

    def test_setter_s3(self):
        self.s3.set_shape(self.c1)
        assert self.s3.get_shape() == self.c1

    def test_setter_init_velo_s1(self):
        self.s1.set_init_velo(0, 0)
        assert self.s1.get_init_velo() == (0, 0)

    def test_setter_init_velo_s1_setback(self):
        self.s1.set_init_velo(self.s1_Vx, self.s1_Vy)
        assert self.s1.get_init_velo() == (self.s1_Vx, self.s1_Vy)

    def calculate_sequence_error(self, cal_seq, true_seq):
        new_seq = []
        for i in range(len(cal_seq)):
            new_seq.append(cal_seq[i] - true_seq[i])
        return new_seq

    def test_sim_t1(self):
        t_expected = [0.0, 1.25, 2.5, 3.75, 5.0]
        t_new = self.calculate_sequence_error(self.time1, t_expected)
        assert abs(max(t_new, key=abs)) / abs(max(t_expected, key=abs)) < self.e

    def test_sim_t2(self):
        t_expected = [0.0, 1.5, 3.0, 4.5, 6.0]
        t_new = self.calculate_sequence_error(self.time2, t_expected)
        assert abs(max(t_new, key=abs)) / abs(max(t_expected, key=abs)) < self.e

    def test_sim_t3(self):
        t_expected = [0.0, 1.75, 3.5, 5.25, 7.0]
        t_new = self.calculate_sequence_error(self.time3, t_expected)
        assert abs(max(t_new, key=abs)) / abs(max(t_expected, key=abs)) < self.e

    def test_sim_ode1_rx(self):
        rx_expected = [2.7, 3.7990, 4.8981, 5.9971, 7.0961]
        rx = self.ode1[0:, 0]
        rx_new = self.calculate_sequence_error(rx, rx_expected)
        assert abs(max(rx_new, key=abs)) / abs(max(rx_expected, key=abs)) < self.e

    def test_sim_ode1_ry(self):
        ry_expected = [7.8, -6.8960, -36.9045, -82.2254, -142.8589]
        ry = self.ode1[0:, 1]
        ry_new = self.calculate_sequence_error(ry, ry_expected)
        assert abs(max(ry_new, key=abs)) / abs(max(ry_expected, key=abs)) < self.e

    def test_sim_ode1_vx(self):
        vx_expected = [0.8792, 0.8792, 0.8792, 0.8792, 0.8792]
        vx = self.ode1[0:, 2]
        vx_new = self.calculate_sequence_error(vx, vx_expected)
        assert abs(max(vx_new, key=abs)) / abs(max(vx_expected, key=abs)) < self.e

    def test_sim_ode1_vy(self):
        vy_expected = [-5.6318, -17.8818, -30.1318, -42.3818, -54.6318]
        vy = self.ode1[0:, 3]
        vy_new = self.calculate_sequence_error(vy, vy_expected)
        assert abs(max(vy_new, key=abs)) / abs(max(vy_expected, key=abs)) < self.e

    def test_sim_ode2_rx(self):
        rx_expected = [7.7, 7.7, 7.7, 7.7, 7.7]
        rx = self.ode2[0:, 0]
        rx_new = self.calculate_sequence_error(rx, rx_expected)
        assert abs(max(rx_new, key=abs)) / abs(max(rx_expected, key=abs)) < self.e

    def test_sim_ode2_ry(self):
        ry_expected = [4.5, -6.525, -39.6, -94.725, -171.9]
        ry = self.ode2[0:, 1]
        ry_new = self.calculate_sequence_error(ry, ry_expected)
        assert abs(max(ry_new, key=abs)) / abs(max(ry_expected, key=abs)) < self.e

    def test_sim_ode2_vx(self):
        vx_expected = [0.0, 0.0, 0.0, 0.0, 0.0]
        vx = self.ode2[0:, 2]
        vx_new = self.calculate_sequence_error(vx, vx_expected)
        assert abs(max(vx_new, key=abs)) == 0.0

    def test_sim_ode2_vy(self):
        vy_expected = [0.0, -14.7, -29.4, -44.1, -58.8]
        vy = self.ode2[0:, 3]
        vy_new = self.calculate_sequence_error(vy, vy_expected)
        assert abs(max(vy_new, key=abs)) / abs(max(vy_expected, key=abs)) < self.e

    def test_sim_ode3_rx(self):
        rx_expected = [1.75, 2.24932, 3.74728, 6.23370, 9.086956]
        rx = self.ode3[0:, 0]
        rx_new = self.calculate_sequence_error(rx, rx_expected)
        assert abs(max(rx_new, key=abs)) / abs(max(rx_expected, key=abs)) < self.e

    def test_sim_ode3_ry(self):
        ry_expected = [3.70217, 2.071060, -2.555978, -5.58519, -5.35217]
        ry = self.ode3[0:, 1]
        ry_new = self.calculate_sequence_error(ry, ry_expected)
        assert abs(max(ry_new, key=abs)) / abs(max(ry_expected, key=abs)) < self.e

    def test_sim_ode3_vx(self):
        vx_expected = [0.0, 0.570652, 1.14130, 1.63043, 1.63043]
        vx = self.ode3[0:, 2]
        vx_new = self.calculate_sequence_error(vx, vx_expected)
        assert abs(max(vx_new, key=abs)) / abs(max(vx_expected, key=abs)) < self.e

    def test_sim_ode3_vy(self):
        vy_expected = [0.0, -1.8641, -2.66304, -0.79891, 1.065217]
        vy = self.ode3[0:, 3]
        vy_new = self.calculate_sequence_error(vy, vy_expected)
        assert abs(max(vy_new, key=abs)) / abs(max(vy_expected, key=abs)) < self.e
