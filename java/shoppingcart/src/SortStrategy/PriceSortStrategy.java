package SortStrategy;
import Product.Product;
import java.util.Comparator;
import java.util.List;

public class PriceSortStrategy implements SortStrategy {
    @Override
    public void sort(List<Product> products) {
        products.sort(Product::compareTo);
    }
}