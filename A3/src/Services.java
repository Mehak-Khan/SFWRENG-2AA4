/**
 * Author: Mehak Khan
 * Date: March 14, 2021
 * 
 * Description: Servies module
 */

package src;

public class Services {

	public static double[] normal(double[] array) {
		double sum_list = sum(array);
		double[] normal = new double[array.length];
		for (int i = 0; i < array.length; i++) {
			normal[i] = array[i]/sum_list;
		}

		return normal;
	}

	public static double sum(double[] array) {
    double sum = 0;
    for (double value : array) {
        sum += value;
    }
    return sum;
}

} 
