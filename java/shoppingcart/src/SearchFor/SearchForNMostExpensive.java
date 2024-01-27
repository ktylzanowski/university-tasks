package SearchFor;

import Product.Product;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class SearchForNMostExpensive {
    public static List<Product> search(List< Product > products , Integer n ){
        products.sort(Comparator.reverseOrder());
        List < Product > returnList = new ArrayList<>();
        for(int i = 0; i < n; i++){
            returnList.add(products.get(i));
        }
        return returnList;
    }
}
