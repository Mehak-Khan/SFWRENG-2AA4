/**
*  @file CourseT.java
*  @author Mehak Khan
*  @brief Abstract Data Type for CourseT 
*  @date 14 March 20201
 */

package src;
import java.util.*;

/**
* @brief This is an ADT for different courses 
* @details This ADT inherits Measures and uses IndicatorT, AttributeT, Services and Norm
*/

public class CourseT implements Measures {

  private String name;
  private HashMap<IndicatorT, HashSet<LOsT>> m;

/**
* @brief This is the constructor for the CourseT class
* @param courseName The string that indicated the name of the course
* @param indicators The sequence that represents the indicators
*/

	public CourseT(String courseName, IndicatorT[] indicators) {
		this.name = courseName;

		HashMap<IndicatorT, HashSet<LOsT>> hash_map = new HashMap<IndicatorT, HashSet<LOsT>>();

		for (int i = 0; i < indicators.length; i++) {
			HashSet<LOsT> h = new HashSet<LOsT>();
			
			hash_map.put(indicators[i], h);

			
		}
		this.m = hash_map;

	}


/**
* @brief Getter for the name of the course
* @return The name of the course
*/

	public String getName() {
		return this.name;
	}


/**
* @brief Getter for the indicators
* @return Sequence representing the indicators
*/

	public IndicatorT[] getIndicators() {
		IndicatorT[] indT = new IndicatorT[m.size()];
		int i = 0;
		for (IndicatorT ind: m.keySet()) {
			indT[i] = ind;
			i++;
			}
		
		
	
	
		return indT;
	}

/**
*  @brief Get the learning outcomes given an indicator
*  @param indicator The indicator whos learning outcome you want
*  @return The sequence of learning outcomes
*/

  public LOsT[] getLOs(IndicatorT indicator) {
  	if (this.m.containsKey(indicator)) {
  		HashSet<LOsT> h = this.m.get(indicator);
  		LOsT[] seq_h = h.toArray(new LOsT[0]);
  		return seq_h;
  	}
  	return new LOsT[0];
  }
	

/**
*  @brief Add learning outcomes for the indicator. This must be called atleast once for each indicator.
*  @param indicator The indicator you want to add learning outcome for
*  @param outcome The outcome user wants to add
*/
   public void addLO(IndicatorT indicator, LOsT outcome) {
   		if (this.m.containsKey(indicator)) {
   			HashSet<LOsT> h = this.m.get(indicator);
   			h.add(outcome);
   			this.m.put(indicator, h);
   				}
   			}

 /**
*  @brief Delete a learning coutcomes for the indicator.
*  @param indicator The indicator you want to delete learning outcome for
*  @param outcome The learning outcome you want to delete
*/
   public void delLO(IndicatorT indicator, LOsT outcome) {
   		if (this.m.keySet().contains(indicator)) {
   			HashSet<LOsT> h = m.get(indicator);
   			h.remove(outcome);
   			this.m.put(indicator, h);
   				}
   			}


 /**
 *  @brief Verify if the given indicator has all the given sequence of learning outcomes in the map
 *  @param indicator The indicator you need verification for
 *  @param outcomes The sequence of learning outcomes the indicator must have
 *  @return Boolean, return True if the indicator has the given sequence of learning outcomes mapped to it, otherwise return False
 */

   public boolean member(IndicatorT indicator, LOsT[] outcomes) {

   	if (m.keySet().contains(indicator)) {
   		HashSet<LOsT> h = new HashSet<>(Arrays.asList(outcomes));
   		return h.equals(m.get(indicator));
   	}
   	return false;

   }

 /**
 *  @brief a measures method that measures learning outcomes
*/

	 public double[] measures() {
	 	throw new UnsupportedOperationException("Not supported by this module");
	 }

/**
*  @brief a measures method based on indicators
*  @param IndicatorT The indicator to measure
*  @return A double array that returns the measures values of how well students are performing
*/

  public double[] measures(IndicatorT ind) {
  	if (this.getLOs(ind).length == 0) {
  		double[] empty = {0,0,0,0};
  		return empty;

  	}
  		double[] measureInd = {0,0,0,0};
  		LOsT[] outcomes = this.getLOs(ind);
  		for (int i =0; i < outcomes.length; i++) {
  			for (int k = 0; k < measureInd.length; k ++) {
				measureInd[k] = measureInd[k] + outcomes[i].measures()[k];
  			}
  			
  		}

  		if (Norm.getNInd()) {
  			return Services.normal(measureInd);
  	}
  	else {
  		return measureInd;
  	}
  	


  }


/**
*  @brief a measures method based on attributes
*  @param IndicatorT The indicator to measure
*  @return A double array that returns the measures values of how well students are performing
*/

  public double[] measures(AttributeT att) {
  	if (att.getIndicators().length == 0) {
  		double[] empty = {0,0,0,0};
  		return empty;

  	}
  		double[] measureInd = {0,0,0,0};
  		IndicatorT[] indicators = att.getIndicators();
  		for (int i = 0; i < indicators.length; i++) {
  			double[] ind_measures = this.measures(indicators[i]);
  			for (int k = 0; k < measureInd.length; k ++) {
				measureInd[k] = measureInd[k] + ind_measures[k];
  			}
  			
  		}

  		if (Norm.getNAtt()) {
  			return Services.normal(measureInd);
  	}
  	else {
  		return measureInd;
  	}
  	


  }



  






		 

}
