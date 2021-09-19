/**
 * Author: Mehak Khan
 * Revised: 27 March, 2021
 * 
 * Description: Testing AttributeT
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.Arrays;

public class TestAttributeT
{
	private AttributeT att1;
	private AttributeT att2;
	private AttributeT att3;


	@Before
	public void setUp() {
		att1 = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.openEnded, IndicatorT.tools});

		//With duplicates
		att2 = new AttributeT("Information", new IndicatorT[] {IndicatorT.math, IndicatorT.standards, IndicatorT.tools, IndicatorT.standards});

		//Empty 
		att3 = new AttributeT("Information", new IndicatorT[] {});
	}

	@After
	public void tearDown() {
		att1 = null;
		att2 = null;
		att3 = null;

	}


	//Method to check equality of two arrays with indicatorT values, order does not matter so sort the two arrays
	public static boolean equals(IndicatorT[] a, IndicatorT[] a2) {
		Arrays.sort(a);
		Arrays.sort(a2);
		return (Arrays.equals(a,a2));		
	}

    @Test
    public void testGetName1()
    {
        assertTrue(att1.getName() == "Knowledge");
    }

    @Test
    public void testGetName2()
    {
        assertTrue(att2.getName() == "Information");
    }

    @Test
    public void testGetIndicators1() {
    	IndicatorT[] a = att1.getIndicators();
    	assertTrue(this.equals(a, new IndicatorT[] {IndicatorT.math, IndicatorT.openEnded, IndicatorT.tools}));
    }

        @Test
    public void testGetIndicators2() {
    	IndicatorT[] a = att2.getIndicators();
    	assertTrue(this.equals(a, new IndicatorT[] {IndicatorT.math, IndicatorT.standards, IndicatorT.tools}));
    }

    @Test
    public void testGetIndicatorsEmpty() {
    	IndicatorT[] a = att3.getIndicators();
    	assertTrue(this.equals(a, new IndicatorT[] {}));
    }




}
