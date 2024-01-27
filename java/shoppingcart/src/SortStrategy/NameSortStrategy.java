package SortStrategy;
import Product.Product;

import java.util.Comparator;
import java.util.List;

public class NameSortStrategy implements SortStrategy {
    @Override
    public void sort(List<Product> products) {
        products.sort(Comparator.comparing(Product::getName));
    }
}