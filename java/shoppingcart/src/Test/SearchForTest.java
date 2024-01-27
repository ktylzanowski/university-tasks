package Test;
import static org.junit.jupiter.api.Assertions.*;

import Product.Product;
import SearchFor.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SearchForTest {

    private List<Product> products;

    @BeforeEach
    void setUp() {
        products = new ArrayList<>();
        products.add(new Product("P1", "Product 1", 50));
        products.add(new Product("P2", "Product 2", 30));
        products.add(new Product("P3", "Product 3", 70));
        products.add(new Product("P4", "Product 4", 90));
    }

    @Test
    void testSearchForCheapest() {
        Product cheapestProduct = SearchForCheapest.search(products);
        assertEquals("Product 2", cheapestProduct.getName());
    }

    @Test
    void testSearchForMostExpensive() {
        Product mostExpensiveProduct = SearchForMostExpensive.search(products);
        assertEquals("Product 4", mostExpensiveProduct.getName());
    }

    @Test
    void testSearchForNCheapest() {
        List<Product> cheapestProducts = SearchForNCheapest.search(products, 2);
        assertEquals(2, cheapestProducts.size());
        assertEquals("Product 2", cheapestProducts.get(0).getName());
        assertEquals("Product 1", cheapestProducts.get(1).getName());
    }

    @Test
    void testSearchForNMostExpensive() {
        List<Product> mostExpensiveProducts = SearchForNMostExpensive.search(products, 2);
        assertEquals(2, mostExpensiveProducts.size());
        assertEquals("Product 4", mostExpensiveProducts.get(0).getName());
        assertEquals("Product 3", mostExpensiveProducts.get(1).getName());
    }
}
