package SearchFor;

import Product.Product;

import java.util.Comparator;
import java.util.List;

public class SearchForMostExpensive {
    public static Product search(List< Product > products){
        products.sort(Comparator.reverseOrder());
        return products.getFirst();
    }
}
