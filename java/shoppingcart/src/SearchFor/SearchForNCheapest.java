package SearchFor;
import Product.Product;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class SearchForNCheapest {
    public static List<Product> search(List< Product > productsList , Integer n ){

        productsList.sort(Product::compareTo);

        List < Product > returnList = new ArrayList<>();

        for(int i = 0; i < n; i++){
            returnList.add(productsList.get(i));
        }
        return returnList;
    }
}
