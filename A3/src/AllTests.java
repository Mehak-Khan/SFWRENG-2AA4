/**
 * Author: Mehak Khan
 * Revised: 27 March, 2021
 * 
 * Description: All tests
 */

package src;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
   TestAttributeT.class,	
   TestLOsT.class,
   TestCourseT.class,
   TestProgramT.class
})

public class AllTests
{
}
