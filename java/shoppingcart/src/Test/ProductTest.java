package Test;
import Product.Product;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ProductTest {

    @Test
    public void testProductInitialization() {
        Product product = new Product("P001", "Laptop", 1000);

        assertEquals("P001", product.getCode());
        assertEquals("Laptop", product.getName());
        assertEquals(1000, product.getPrice());
        assertEquals(1000, product.getDiscountPrice());
    }

    @Test
    public void testSetDiscountPrice() {
        Product product = new Product("P002", "Smartphone", 500);

        product.setDiscountPrice(450);

        assertEquals(450, product.getDiscountPrice());
    }

    @Test
    public void testCompareTo() {
        Product product1 = new Product("P004", "Tablet", 300);
        Product product2 = new Product("P005", "Camera", 250);

        assertTrue(product1.compareTo(product2) > 0);
        assertTrue(product2.compareTo(product1) < 0);
    }
}
