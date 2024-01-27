package Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import org.junit.Before;
import org.junit.Test;
import Operations.*;
import RPN.RPN;

import java.util.NoSuchElementException;

public class RPNTest {
    private RPN rpn;

    @Before
    public void setup() {
        rpn = new RPN();
        rpn.addOperation("+", new Plus());
        rpn.addOperation("-", new Subtraction());
        rpn.addOperation("*", new Multiplication());
        rpn.addOperation("/", new Divide());
    }

    @Test
    public void testEvaluateValidRPN() {
        String expression = "5 3 +";
        int result = rpn.evaluateRPN(expression);
        assertEquals(8, result);
    }

    @Test
    public void testEvaluateComplexValidRPN() {
        String expression = "5 3 + 2 * 6 4 - /";
        int result = rpn.evaluateRPN(expression);
        assertEquals(8, result);
    }

    @Test
    public void testEvaluateInvalidRPN() {
        String expression = "5 3 2 +";
        assertThrows(IllegalArgumentException.class, () -> rpn.evaluateRPN(expression));
    }

    @Test
    public void testEvaluateRPNWithCustomOperation() {
        rpn.addOperation("^", (operand1, operand2) -> (int) Math.pow(operand1, operand2));
        String expression = "2 3 ^";
        int result = rpn.evaluateRPN(expression);
        assertEquals(8, result);
    }
    @Test
    public void testEvaluateRPNWithDivByZero() {
        String expression = "2 0 /";
        assertThrows(ArithmeticException.class, () -> rpn.evaluateRPN(expression));
    }

    @Test
    public void testEvaluateRPNWithSingleOperand() {
        String expression = "5";
        int result = rpn.evaluateRPN(expression);
        assertEquals(5, result);
    }

    @Test
    public void testEvaluateRPNWithMultipleOperations() {
        String expression = "5 3 + 2 * 6 - ";
        int result = rpn.evaluateRPN(expression);
        assertEquals(10, result);
    }


    @Test
    public void testEvaluateRPNWithInvalidExpression() {
        String expression = "5 + 3";
        assertThrows(NoSuchElementException.class, () -> rpn.evaluateRPN(expression));
    }

    @Test
    public void testEvaluateRPNWithEmptyExpression() {
        String expression = "";
        assertThrows(IllegalArgumentException.class, () -> rpn.evaluateRPN(expression));
    }

    @Test
    public void testEvaluateRPNWithInvalidOperation() {
        String expression = "5 3 $";
        assertThrows(IllegalArgumentException.class, () -> rpn.evaluateRPN(expression));
    }
}
