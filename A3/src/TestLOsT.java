/**
 * Author: Mehak Khan
 * Revised: 27 March 2021
 * 
 * Description: Testing LOsT Class
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.Arrays;

public class TestLOsT
{

	private LOsT L03, L04;

	@Before 
	public void setUp() {
		L03 = new LOsT("topic3", 33, 77, 88, 2);
		L04 = new LOsT("topic4", 2, 2, 2, 2);
	}

	@After
	public void tearDown() {
		L03 = null;
		L04 = null;
	}


    @Test(expected = IllegalArgumentException.class) 
    public void testConstructorException1() {
        LOsT L05 = new LOsT("topic5", 0, 0, -1, 10);
    }


    @Test(expected = IllegalArgumentException.class) 
    public void testConstructorException2() {
        LOsT L05 = new LOsT("topic5", 0, 0, 0, 0);
    }
    

    @Test
    public void tesstGetName()
    {
        assertTrue(L03.getName() == "topic3");
        assertTrue(L04.getName() == "topic4");
    }

    @Test
    public void testNotEquals() {
    	assertTrue(!L03.equals(L04));
    	
    }

    @Test
    public void testEqualsSameName() {
    	LOsT L05 = new LOsT("topic4", 55, 66, 77, 88);
    	assertTrue(L04.equals(L04));
    	assertTrue(L04.equals(L05));
    }


    @Test(expected = UnsupportedOperationException.class)
    public void testMeasuresExceptionInd() {
    	L03.measures(IndicatorT.math);
    }   

    @Test(expected = UnsupportedOperationException.class)
    public void testMeasuresExceptionAtt() {
    	L03.measures(new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math}));
    } 

    @Test 
    public void testMeasures() {
    	double[] measures3 = L03.measures();
        double[] measures4 = L04.measures();
    	double[] measures_exp = new double[] {33.0,77.0,88.0,2.0};
        Arrays.equals(measures3, measures_exp);


    }

    @Test 
    public void testMeasuresServices() {
    	Norm.setNorms(true, false, false);
    	double[] measures = L04.measures();
    	Norm.setNorms(false,false,false);
    	double[] measures_exp = new double[] {0.25, 0.25, 0.25, 0.25};
        assertTrue(Arrays.equals(measures, measures_exp));

    }


    @Test 
    public void test2MeasuresServices() {
    	Norm.setNorms(true, false, false);
    	double[] measures = L03.measures();
    	Norm.setNorms(false,false,false);
    	double[] measures_exp = new double[] {0.165, 0.385, 0.44, 0.01};
        assertTrue(Arrays.equals(measures, measures_exp));

    }

}
