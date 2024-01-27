package SearchFor;

import Product.Product;

import java.util.Comparator;
import java.util.List;

public class SearchForCheapest {
    public static Product search(List< Product > products){
        products.sort(Product::compareTo);
        return products.getFirst();
    }
}
