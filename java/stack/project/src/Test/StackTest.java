package Test;
import Stack.Stack;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class StackTest {
    private Stack stack;

    @Before
    public void setUp() {
        stack = new Stack();
    }

    @Test
    public void testPushAndPop() {
        stack.push(1);
        stack.push(2);
        stack.push(3);

        assertEquals(3, stack.pop());
        assertEquals(2, stack.pop());
        assertEquals(1, stack.pop());
    }

    @Test
    public void testPeek() {
        stack.push("A");
        stack.push("B");

        assertEquals("B", stack.peek());
    }

    @Test
    public void testSize() {
        assertEquals(0, stack.size());

        stack.push(1);
        stack.push(2);
        stack.push(3);

        assertEquals(3, stack.size());
    }

    @Test
    public void testEmptyStack() {
        assertTrue(stack.isEmpty());
    }

    @Test
    public void testNonEmptyStack() {
        stack.push("Element");
        assertFalse(stack.isEmpty());
    }
}
