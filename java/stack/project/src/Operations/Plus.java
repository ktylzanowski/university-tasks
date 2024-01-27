package Operations;

public class Plus implements Operation {
    @Override
    public int apply(int operand1, int operand2) {
        return operand1 + operand2;
    }
}
