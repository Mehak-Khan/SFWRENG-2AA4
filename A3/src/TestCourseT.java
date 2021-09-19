/**
 * Author: Mehak Khan
 * Revised: March 27, 2021
 * 
 * Description: Testing CourseT
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.*;

public class TestCourseT
{

	private CourseT c1;
	private CourseT c2;


	@Before 
	public void setUp() {
		c1 = new CourseT("Software Design", new IndicatorT[] {IndicatorT.math, IndicatorT.desPrinciples, IndicatorT.desProcess});
        //Duplicate indicators
        c2 = new CourseT("Software Process", new IndicatorT[] {IndicatorT.tools, IndicatorT.tools, IndicatorT.desProcess});



	}



//Equal method defined to check if two object arrays are equal where the order of elements does not matter
	public static boolean equal(Object[] a, Object[] a2) {
		Arrays.sort(a);
		Arrays.sort(a2);
		return (Arrays.equals(a,a2));		
	}

	@Test
    public void testGetNameC1()
    {
        assertTrue(c1.getName() == "Software Design");
    }

    @Test 
    public void testGetIndicators() {
    	assertTrue(this.equal(c1.getIndicators(), new IndicatorT[] {IndicatorT.math, IndicatorT.desPrinciples, IndicatorT.desProcess}));
    

    }

    @Test
    public void testGetIndicatorsDuplicates() {
        assertTrue(this.equal(c2.getIndicators(), new IndicatorT[] {IndicatorT.tools, IndicatorT.desProcess}));
    }

    @Test
    public void testAddLOandGetLOs() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	c1.addLO(IndicatorT.math, L01);

    	LOsT[] l1_exp = new LOsT[] {L01};

    	LOsT[] l1_calc = c1.getLOs(IndicatorT.math);

    	assertTrue(this.equal(l1_calc, l1_exp));



    }

    @Test
    public void testAddLOandGetLOsDuplicate() {
        LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
        c1.addLO(IndicatorT.math, L01);
        c1.addLO(IndicatorT.math, new LOsT("topic1", 3, 3, 3, 3));

        LOsT[] l1_exp = new LOsT[] {L01};

        LOsT[] l1_calc = c1.getLOs(IndicatorT.math);

        assertTrue(this.equal(l1_calc, l1_exp));



    }

   @Test
    public void test2AddLOandGetLOs() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	LOsT L02 = new LOsT("topic2", 15, 21, 5, 23);
        LOsT L03 = new LOsT("topic3", 14, 33, 3, 2);
        LOsT L04 = new LOsT("topic4", 3, 23, 55, 2);

    	c1.addLO(IndicatorT.math, L01);
    	c1.addLO(IndicatorT.math, L02);
        c1.addLO(IndicatorT.desProcess, L03);
        c1.addLO(IndicatorT.desProcess, L04);

    	LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
        LOsT[] l2_calc = c1.getLOs(IndicatorT.desProcess);

    	LOsT[] l1_exp = new LOsT[] {L02, L01};
        LOsT[] l2_exp = new LOsT[] {L03, L04};

        assertTrue(Arrays.equals(l1_calc, l1_exp));
        assertTrue(Arrays.equals(l2_calc, l2_exp));

    }

    @Test
    public void testAddLOandGetLOs_IndicatorNotInMap() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	c1.addLO(IndicatorT.tools, L01);

    	LOsT[] l1_exp = new LOsT[] {};

    	LOsT[] l1_calc = c1.getLOs(IndicatorT.tools);

    	assertTrue(Arrays.equals(l1_calc, l1_exp));



    }

    @Test
    public void testDeleteLO() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	c1.addLO(IndicatorT.math, L01);
    	c1.delLO(IndicatorT.math, L01);

		LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
    	assertTrue(Arrays.equals(l1_calc, new LOsT[] {}));

    }

    @Test
    public void test2DeleteLO() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	LOsT L02 = new LOsT("topic2", 15, 21, 5, 23);
        
    	c1.addLO(IndicatorT.math, L01);
    	c1.addLO(IndicatorT.math, L02);

    	c1.delLO(IndicatorT.math, L01);
    	
		LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
    	assertTrue(Arrays.equals(l1_calc, new LOsT[] {L02}));

}

    @Test
    public void test3DeleteLO() {
        LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
        LOsT L02 = new LOsT("topic2", 15, 21, 5, 23);
        LOsT L03 = new LOsT("topic3", 14, 33, 3, 2);
        c1.addLO(IndicatorT.math, L01);
        c1.addLO(IndicatorT.math, L02);
        c1.addLO(IndicatorT.math, L03);

        c1.delLO(IndicatorT.math, L03);
        c1.delLO(IndicatorT.math, L02);
        
        LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
        LOsT[] l1_exp = new LOsT[] {L01};

        assertTrue(Arrays.equals(l1_calc, l1_exp));

    }

    @Test
    public void test4DeleteLO() {
        LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
        LOsT L02 = new LOsT("topic2", 15, 21, 5, 23);
        LOsT L03 = new LOsT("topic3", 14, 33, 3, 2);
        c1.addLO(IndicatorT.math, L01);
        c1.addLO(IndicatorT.math, L02);
        c1.addLO(IndicatorT.math, L03);

        c1.delLO(IndicatorT.math, L03);
        
        LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
        LOsT[] l1_exp = new LOsT[] {L01, L02};

       HashSet <LOsT> set = new HashSet<LOsT>();
       set.addAll(Arrays.asList(l1_calc));
       assertTrue(set.contains(L01) & set.contains(L02));


    }

    @Test
    public void test5DeleteLOSameTopic() {
        LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
        LOsT L02 = new LOsT("topic2", 15, 21, 5, 23);
        LOsT L03 = new LOsT("topic3", 14, 33, 3, 2);
        c1.addLO(IndicatorT.math, L01);
        c1.addLO(IndicatorT.math, L02);
        c1.addLO(IndicatorT.math, L03);

        c1.delLO(IndicatorT.math, new LOsT("topic2", 5, 6, 7, 8));
        
        LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
        LOsT[] l1_exp = new LOsT[] {L01, L03};

       HashSet <LOsT> set = new HashSet<LOsT>();
       set.addAll(Arrays.asList(l1_calc));
       assertTrue(set.contains(L01) & set.contains(L03));


    }

    @Test
    public void testNullDeleteLO() {
    	c1.delLO(IndicatorT.math, new LOsT("topic3", 5, 5, 5, 5));
    	
		LOsT[] l1_calc = c1.getLOs(IndicatorT.math);
    	assertTrue(Arrays.equals(l1_calc, new LOsT[] {}));

    }


    @Test
    public void testMemberTrue() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	c1.addLO(IndicatorT.desProcess, L01);

    	assert(c1.member(IndicatorT.desProcess,new LOsT[] {L01}));


    }

     @Test
    public void tes2MemberTrue() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	LOsT L02 = new LOsT("topic2", 21, 4, 12, 29);
    	c1.addLO(IndicatorT.desProcess, L01);
    	c1.addLO(IndicatorT.desProcess, L02);

    	assert(c1.member(IndicatorT.desProcess,new LOsT[] {L01, L02}));


    }

    @Test
    public void testMemberFalse() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	c1.addLO(IndicatorT.desProcess, L01);

    	assert(!c1.member(IndicatorT.math,new LOsT[] {L01}));


    }    

    @Test
    public void test2MemberFalse() {
    	LOsT L01 = new LOsT("topic1", 22, 55, 33, 2);
    	c1.addLO(IndicatorT.desProcess, L01);

    	assert(!c1.member(IndicatorT.desProcess,new LOsT[] {}));


    }    

    @Test(expected = UnsupportedOperationException.class)
    public void testMeasuresException() {
    	c1.measures();
    }

    @Test
    public void testMeasuresInd() {
    	c1.addLO(IndicatorT.desPrinciples, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 22, 10, 5, 8));
        double[] meas_ind = c1.measures(IndicatorT.desPrinciples);
        double[] meas_ind_exp = new double[] {44, 23, 19, 85};
        assertTrue(Arrays.equals(meas_ind, meas_ind_exp));
    }

    @Test
    public void testMeasuresIndServices() {
        Norm.setNInd(true);
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic1", 5, 10, 15, 20));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 5, 10, 5, 10));
        double[] meas_ind = c1.measures(IndicatorT.desPrinciples);
        Norm.setNInd(false);
        double[] meas_ind_exp = new double[] {0.125, 0.25, 0.25, 0.375};
        assertTrue(Arrays.equals(meas_ind, meas_ind_exp));
    }

    @Test
    public void test2MeasuresIndNotEquals() {
        c1.addLO(IndicatorT.desProcess, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 22, 10, 5, 8));
        double[] meas_ind = c1.measures(IndicatorT.desPrinciples);
        double[] meas_ind_exp = new double[] {44, 23, 19, 85};
        assertTrue(!Arrays.equals(meas_ind, meas_ind_exp));
    }

    @Test
    public void testMeasuresIndNull() {
        c1.addLO(IndicatorT.desProcess, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 22, 10, 5, 8));
        double[] meas_ind = c1.measures(IndicatorT.math);
        double[] meas_ind_exp = new double[] {0, 0, 0, 0};
        assertTrue(Arrays.equals(meas_ind, meas_ind_exp));
    }

    @Test
    public void testMeasuresAtt() {
        AttributeT att1 = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.tools, IndicatorT.desPrinciples, IndicatorT.specEngKnow});
        c1.addLO(IndicatorT.desProcess, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 22, 10, 5, 8));
        c1.addLO(IndicatorT.math, new LOsT("topic3", 10, 15, 20, 7));
        double[] meas_att_exp = new double[] {32, 25, 25, 15};
        double[] meas_att = c1.measures(att1);

        assertTrue(Arrays.equals(meas_att_exp, meas_att));


    }

    @Test
    public void testMeasuresAttServices() {
        AttributeT att1 = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.tools, IndicatorT.desPrinciples, IndicatorT.specEngKnow});
        Norm.setNAtt(true);
        c1.addLO(IndicatorT.desProcess, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 10, 10, 15, 5));
        c1.addLO(IndicatorT.math, new LOsT("topic3", 22, 15, 10, 10));
        double[] meas_att_exp = new double[] {32.0/97.0, 25.0/97.0, 25.0/97.0, 15.0/97.0};
        double[] meas_att = c1.measures(att1);
        Norm.setNAtt(false);
        assertTrue(Arrays.equals(meas_att_exp, meas_att));


    }


    @Test
    public void test2MeasuresAtt() {
        AttributeT att1 = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.tools, IndicatorT.desPrinciples, IndicatorT.specEngKnow});
        c1.addLO(IndicatorT.desProcess, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 22, 10, 5, 8));
        c1.addLO(IndicatorT.math, new LOsT("topic3", 10, 15, 20, 7));
        c1.addLO(IndicatorT.math, new LOsT("topic4", 5, 2, 0, 9));
        double[] meas_att_exp = new double[] {37, 27, 25, 24};
        double[] meas_att = c1.measures(att1);

        assertTrue(Arrays.equals(meas_att_exp, meas_att));


    }


    @Test
    public void testMeasuresAttEmpty() {
        AttributeT att1 = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.tools, IndicatorT.specEngKnow});
        c1.addLO(IndicatorT.desProcess, new LOsT("topic1", 22, 13, 14, 77));
        c1.addLO(IndicatorT.desPrinciples, new LOsT("topic2", 22, 10, 5, 8));
        c1.addLO(IndicatorT.math, new LOsT("topic3", 10, 15, 20, 7));
        c1.addLO(IndicatorT.math, new LOsT("topic3", 5, 2, 0, 9));
        double[] meas_att_exp = new double[] {0, 0, 0, 0};
        double[] meas_att = c1.measures(att1);

        assertTrue(Arrays.equals(meas_att_exp, meas_att));


    }


    @Test
    public void test2MeasuresAttEmpty() {
        AttributeT att1 = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.tools, IndicatorT.desPrinciples, IndicatorT.specEngKnow});
        double[] meas_att = c1.measures(att1);
        double[] meas_att_exp = new double[] {0, 0, 0, 0};
        assertTrue(Arrays.equals(meas_att_exp, meas_att));


    }


    

    	@After
	public void tearDown() {
		c1 = null;
		c2 = null;

	}



}
