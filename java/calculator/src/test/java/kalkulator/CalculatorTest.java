package kalkulator;
import org.junit.*;
import static org.junit.Assert.assertEquals;

public class CalculatorTest {
	private Calculator sut;
	@Before
	public void setUp() {
		sut = new Calculator();
	}
	@Test
	public void testAddOne(){
		sut.add(1);
		assertEquals("0+1 = 1", 1, sut.getState());
	}
	@Test(expected = ArithmeticException.class)
	public void testAddOverflow(){
		sut.setState(1);
		sut.add(Integer.MAX_VALUE);
	}

	@Test
	public void testMultOneByTwo(){
		sut.setState(1);
		sut.mult(2);
		assertEquals("1*2 = 2", 2, sut.getState());
	}

	@Test
	public void testSubFive(){
		sut.setState(2);
		sut.sub(5);
		assertEquals("2-5 = -3", -3, sut.getState());
	}

	@Test
	public void testDivByTwo(){
		sut.setState(6);
		sut.div(2);
		assertEquals("6/2 = 3", 3, sut.getState());
	}

	@Test(expected = ArithmeticException.class)
	public void testDivByZero() {
		Calculator sut = new Calculator();
		sut.div(0);
	}

	@Test
	public void testAddToMemory(){
		sut.setMemory(10);
		sut.addToMemory(20);
		assertEquals("10+20 = 30", 30, sut.getMemory());
	}

	@Test
	public void testSubFromMemory(){
		sut.setMemory(30);
		sut.subFromMemory(10);
		assertEquals("30-10 = 20", 20, sut.getMemory());
	}

	@Test
	public void testActionWithMemory(){
		sut.setMemory(30);
		sut.subFromMemory(10);
		sut.add(sut.getMemory());
		assertEquals("0+20 = 20", 20, sut.getState());
	}

	@Test
	public void testAddMultipleNumbers() {
		sut.add(5);
		sut.add(10);
		sut.add(7);
		assertEquals("0+5+10+7 = 22", 22, sut.getState());
	}

	@Test
	public void testMultMultipleNumbers() {
		sut.setState(2);
		sut.mult(3);
		sut.mult(4);
		assertEquals("2*3*4 = 24", 24, sut.getState());
	}

	@Test
	public void testSubMultipleNumbers() {
		sut.setState(20);
		sut.sub(5);
		sut.sub(7);
		assertEquals("20-5-7 = 8", 8, sut.getState());
	}

	@Test
	public void testDivMultipleNumbers() {
		sut.setState(64);
		sut.div(4);
		sut.div(2);
		assertEquals("64/4/2 = 8", 8, sut.getState());
	}

	@Test
	public void testResetState() {
		sut.setState(42);
		sut.resetState();
		assertEquals("Reset calculator state", 0, sut.getState());
	}

	@Test
	public void testClearMemory() {
		sut.setMemory(15);
		sut.clearMemory();
		assertEquals("Clear calculator memory", 0, sut.getMemory());
	}

	@Test
	public void testDivByZeroWithOperations(){
		sut.add(5);
		try{
			sut.div(0);
		}catch(ArithmeticException e){
			System.out.println(e.getMessage());
		}
		assertEquals("0+5=5", 5, sut.getState());
	}
}
