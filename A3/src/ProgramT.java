/**
 * Author: Mehak Khan
 * Date: March 23, 2021
 * 
 * Description: Program Module ADT
 */

package src;
import java.util.*;

public class ProgramT extends HashSet<CourseT> implements Measures {

	private HashSet<CourseT> s = this;

	public double[] measures() {
	 	throw new UnsupportedOperationException("Not supported by this module");
	 }

	public double[] measures(IndicatorT ind) {
	 	throw new UnsupportedOperationException("Not supported by this module");
	 }

	public double[] measures(AttributeT att) {
		double[] sumMeas  = {0,0,0,0};
	 	for (CourseT course : this.s) {
	 		double[] att_meas = course.measures(att);
	 		for (int i = 0; i < sumMeas.length; i ++) {
	 			sumMeas[i] = sumMeas[i] + att_meas[i];
	 		}

	 	}
	 	return Services.normal(sumMeas);
	 		



	 }
}
