/**
 * Author: Mehak Khan
 * Date: March 14, 2021
 * 
 * Description: Learning Outcomes Module ADT
 */

package src;

public class LOsT implements Measures {

	private String name;
	private int n_blw;
	private int n_mrg;
	private int n_mts;
	private int n_exc;

	public LOsT(String topic, int nblw, int nmrg, int nmts, int nexc) {
		if (nblw < 0 | nmrg < 0 | nmts < 0 | nexc < 0) {
			throw new IllegalArgumentException("Provide only natural numbers for last four arguments");
		}
		if (nblw == 0 & nmrg == 0 & nmts == 0 & nexc == 0) {
			throw new IllegalArgumentException("All four arguments cannot be 0");
		}
		this.n_blw = nblw;
		this.name = topic;
		this.n_mrg = nmrg;
		this.n_mts = nmts;
		this.n_exc = nexc;

	}

	public String getName() {
		return this.name;
	}

	@Override
	public boolean equals(Object o) {
		LOsT obj = (LOsT) o;
		return (obj.getName() == this.name);

	}

	//Source: https://stackoverflow.com/questions/2265503/why-do-i-need-to-override-the-equals-and-hashcode-methods-in-java
    @Override
    public int hashCode() {
        final int num = 31;
        int code = 1;
        code = num * code
                + ((name == null) ? 0 : name.hashCode());
        return code;
    }

	public double[] measures() {
		double[] a = {Double.valueOf(this.n_blw), Double.valueOf(this.n_mrg), Double.valueOf(this.n_mts), Double.valueOf(this.n_exc)};
		if (!Norm.getNLOs()) {
			return a;
		}
		return Services.normal(a);
	}


	public double[] measures(IndicatorT ind) {
		throw new UnsupportedOperationException("Mismatched types");
	}


	public double[] measures(AttributeT att) {
		throw new UnsupportedOperationException("Mismatched types");
	}



	}

