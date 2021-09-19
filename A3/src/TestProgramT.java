/**
 * Author: Mehak Khan
 * Revised: 27 March 2021
 * 
 * Description: Testing Program Class
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.Arrays;

public class TestProgramT
{

	private ProgramT P1;

	@Before
	public void setUp() {
		P1 = new ProgramT();

	}

	@After
	public void tearDown() {
		P1 = null;
	}

	
	@Test
    public void testAdd()
    {
        CourseT math = new CourseT("Math", new IndicatorT[] {IndicatorT.math, IndicatorT.estOutcomes});
		CourseT eng = new CourseT("Eng", new IndicatorT[] {IndicatorT.specEngKnow, IndicatorT.engInSoc});
		P1.add(math);
		P1.add(eng);
		assertTrue(P1.contains(math));
		assertTrue(P1.contains(eng));

    }

    @Test
    public void testEmpty() {
    	assertTrue(P1.isEmpty());
    }


    @Test(expected = UnsupportedOperationException.class)
    public void testMeasuresException() {
    	P1.measures();
    }


    @Test(expected = UnsupportedOperationException.class)
    public void testMeasuresExceptionInd() {
    	P1.measures(IndicatorT.math);
    }

    @Test
    public void testMeasuresAtt() {
       CourseT math = new CourseT("Math", new IndicatorT[] {IndicatorT.math, IndicatorT.estOutcomes});
       math.addLO(IndicatorT.math, new LOsT("topic1", 2, 33, 4, 77));
       math.addLO(IndicatorT.math, new LOsT("topic2", 22, 12, 5, 8));
       math.addLO(IndicatorT.estOutcomes, new LOsT("topic1", 3, 4, 5, 6));

       CourseT eng = new CourseT("Eng", new IndicatorT[] {IndicatorT.specEngKnow, IndicatorT.engInSoc});
       eng.addLO(IndicatorT.specEngKnow, new LOsT("topic1", 22, 3, 6, 12));

       P1.add(math);
       P1.add(eng);

       AttributeT knowledge = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.estOutcomes, IndicatorT.specEngKnow});

       double[] measures = P1.measures(knowledge);
       double[] measures_exp = new double[] {49/224.0, 52/224.0, 20/224.0, 103/224.0};

       assertTrue(Arrays.equals(measures, measures_exp));
   }

       @Test
       public void testMeasuresAttEmpty() {
       	AttributeT knowledge = new AttributeT("Knowledge", new IndicatorT[] {IndicatorT.math, IndicatorT.estOutcomes, IndicatorT.specEngKnow});
       	double[] measures = P1.measures(knowledge);
       	double[] measures_exp = new double[] {0,0,0,0};

      //due to division by 0
       int i = 0;
       for (double x: measures) {
       	assertTrue(Double.isNaN(x));
       	i++;
       }

       }



    }




