package Operations;

public class Divide implements Operation {
    @Override
    public int apply(int operand1, int operand2) {
        if (operand2 == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return operand1 / operand2;
    }
}
