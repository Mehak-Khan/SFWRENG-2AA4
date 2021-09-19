/**
 * Author: Mehak Khan
 * Date: March 14, 2021
 * 
 * Description: Attribute ADT class
 */


package src;
import java.util.*;

public class AttributeT {
	private String name;
	private IndicatorT[] s;

	public AttributeT(String attribName, IndicatorT[] indicators) {
		this.name = attribName;
		Set<IndicatorT> set_indicators = new HashSet<IndicatorT>(Arrays.asList(indicators));
		this.s = set_indicators.toArray(new IndicatorT[0]);


	}

	public String getName() {
		return name;
	}

	public IndicatorT[] getIndicators() {
		return s;
	}





}

