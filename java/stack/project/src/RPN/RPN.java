package RPN;
import Stack.Stack;
import java.util.Map;
import java.util.HashMap;
import Operations.Operation;

public class RPN {
    private final Stack stack;
    private final Map<String, Operation> operationMap;

    public RPN() {
        this.stack = new Stack();
        this.operationMap = new HashMap<>();
    }

    public void addOperation(String operator, Operation operation) {
        operationMap.put(operator, operation);
    }

    public void removeOperation(String operator) {
        operationMap.remove(operator);
    }

    public int evaluateRPN(String expression) {
        String[] tokens = expression.split(" ");
        for (String token : tokens) {
            if (isNumeric(token)) {
                stack.push(Integer.parseInt(token));
            } else if (operationMap.containsKey(token)) {
                int operand2 = (int) stack.pop();
                int operand1 = (int) stack.pop();
                int result = operationMap.get(token).apply(operand1, operand2);
                stack.push(result);
            } else {
                throw new IllegalArgumentException("Invalid operator: " + token);
            }
        }
        if (stack.size() != 1) {
            throw new IllegalArgumentException("Invalid RPN expression");
        }
        return (int) stack.pop();
    }

    private boolean isNumeric(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
