package Test;
import static org.junit.jupiter.api.Assertions.*;
import Promotion.Promotion;
import Promotion.OrderValuePromotion;
import Promotion.CouponPromotion;
import Promotion.FreeMugPromotion;
import Promotion.BuyTwoGetOneFreePromotion;
import Product.Product;
import ShoppingCart.ShoppingCart;
import SortStrategy.NameSortStrategy;
import SortStrategy.PriceSortStrategy;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.List;

class ShoppingCartTest {

    private ShoppingCart shoppingCart;

    @BeforeEach
    void setUp() {
        shoppingCart = new ShoppingCart();
    }

    @Test
    void addProduct() {
        Product product = new Product("P1", "Product 1", 50);
        shoppingCart.addProduct(product);
        assertEquals(1, shoppingCart.getProducts().size());
        assertTrue(shoppingCart.getProducts().contains(product));
    }

    @Test
    void addPromotion() {
        Promotion promotion = new OrderValuePromotion(shoppingCart);
        shoppingCart.addPromotion(promotion);
        assertEquals(1, shoppingCart.getPromotions().size());
        assertTrue(shoppingCart.getPromotions().contains(promotion));
    }

    @Test
    void applyOrderValuePromotion() {
        Product product1 = new Product("P1", "Product 1", 100);
        Product product2 = new Product("P2", "Product 2", 150);
        Product product3 = new Product("P3", "Product 3", 100);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);
        shoppingCart.addProduct(product3);
        Promotion orderValuePromotion = new OrderValuePromotion(shoppingCart);
        shoppingCart.addPromotion(orderValuePromotion);

        assertEquals(332.5, shoppingCart.calculateTotalPrice());
    }

    @Test
    void applyBuyTwoGetOneFreePromotion() {
        Product product1 = new Product("P1", "Product 1", 50);
        Product product2 = new Product("P2", "Product 2", 75);
        Product product3 = new Product("P3", "Product 3", 100);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);
        shoppingCart.addProduct(product3);

        Promotion buyTwoGetOneFreePromotion = new BuyTwoGetOneFreePromotion(shoppingCart);
        shoppingCart.addPromotion(buyTwoGetOneFreePromotion);
        assertEquals(175, shoppingCart.calculateTotalPrice());
    }

    @Test
    void applyFreeMugPromotion() {
        Product product1 = new Product("P1", "Product 1", 150);
        Product product2 = new Product("P2", "Product 2", 100);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);

        Promotion freeMugPromotion = new FreeMugPromotion(shoppingCart);
        shoppingCart.addPromotion(freeMugPromotion);

        assertEquals(250, shoppingCart.calculateTotalPrice());
        assertTrue(shoppingCart.getProducts().stream().anyMatch(product -> product.getName().equals("Firmowy Kubek")));
    }

    @Test
    void applyCouponPromotion() {
        Product product1 = new Product("P1", "Product 1", 100);
        Product product2 = new Product("P2", "Product 2", 150);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);

        Promotion couponPromotion = new CouponPromotion("P1", shoppingCart);
        shoppingCart.addPromotion(couponPromotion);

        assertEquals(220, shoppingCart.calculateTotalPrice());
    }

    @Test
    void removePromotion() {
        Product product1 = new Product("P1", "Product 1", 50);
        Product product2 = new Product("P2", "Product 2", 30);
        Product product3 = new Product("P3", "Product 3", 70);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);
        shoppingCart.addProduct(product3);

        Promotion buyTwoGetOneFreePromotion = new BuyTwoGetOneFreePromotion(shoppingCart);
        Promotion orderValuePromotion = new OrderValuePromotion(shoppingCart);


        shoppingCart.addPromotion(orderValuePromotion);
        shoppingCart.addPromotion(buyTwoGetOneFreePromotion);

        assertEquals(120, shoppingCart.calculateTotalPrice());

        shoppingCart.removePromotion();
        shoppingCart.removePromotion();

        assertEquals(150, shoppingCart.calculateTotalPrice());
        assertEquals(0, shoppingCart.getPromotions().size());
    }

    @Test
    void sortProductsByPrice() {
        Product product1 = new Product("P1", "Product 1", 50);
        Product product2 = new Product("P2", "Product 2", 30);
        Product product3 = new Product("P3", "Product 3", 70);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);
        shoppingCart.addProduct(product3);

        shoppingCart.sortProducts(new PriceSortStrategy());
        List<Product> products = shoppingCart.getProducts();

        assertEquals(30, products.get(0).getPrice());
        assertEquals(50, products.get(1).getPrice());
        assertEquals(70, products.get(2).getPrice());
    }

    @Test
    void sortProductsByName() {
        Product product1 = new Product("P1", "Product 1", 50);
        Product product2 = new Product("P2", "Apple", 30);
        Product product3 = new Product("P3", "Orange", 70);

        shoppingCart.addProduct(product1);
        shoppingCart.addProduct(product2);
        shoppingCart.addProduct(product3);

        shoppingCart.sortProducts(new NameSortStrategy());
        List<Product> products = shoppingCart.getProducts();

        assertEquals("Apple", products.get(0).getName());
        assertEquals("Orange", products.get(1).getName());
        assertEquals("Product 1", products.get(2).getName());
    }
}