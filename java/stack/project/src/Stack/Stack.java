package Stack;

import java.util.NoSuchElementException;

public class Stack {
    private Object[] array;
    private int size;

    public Stack(){
        this.array = new Object[10];
        this.size = 0;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public int size(){
        return size;
    }

    public void push(Object element) {
        if (size == array.length) {
            int newCapacity = array.length * 2;
            Object[] newArray = new Object[newCapacity];
            if (size > 0) {
                System.arraycopy(array, 0, newArray, 0, size);
            }
            array = newArray;
        }
        array[size] = element;
        size++;
    }
    public Object pop() {
        if (isEmpty()) {
            throw new NoSuchElementException("Empty array");
        } else {
            Object element = array[size - 1];
            array[size - 1] = null;
            size--;
            return element;
        }
    }

    public Object peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Empty array");
        } else {
            return array[size - 1];
        }
    }
}
