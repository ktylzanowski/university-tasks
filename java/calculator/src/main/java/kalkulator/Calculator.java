package kalkulator;

public class Calculator {
	private int state = 0;
	private int memory = 0;

	public int getState() {return state;}

	public void setState(int state) {
		this.state = state;
	}

	public void resetState(){state = 0;}

	public int getMemory(){return memory;}

	public void setMemory(int memory){this.memory = memory;}

	public void addToMemory(int value){
		memory = Math.addExact(memory, value);
	}

	public void subFromMemory(int value){
		memory = Math.subtractExact(memory, value);
	}

	public void clearMemory(){memory = 0;}

	public void add(int value) {state = Math.addExact(state, value);}

	public void sub(int value) {state = Math.subtractExact(state, value);}

	public void mult(int value) {state = Math.multiplyExact(state, value);}

	private int divideByZero(int value){
		if (value == 0){
			throw new ArithmeticException("Div by zero");
		}
		return value;
	}

	public void div(int value) {state /= divideByZero(value);}
}