package ShoppingCart;
import Product.Product;
import Promotion.Promotion;
import SortStrategy.SortStrategy;
import java.util.ArrayList;
import java.util.List;


public class ShoppingCart {
    private final List<Product> products = new ArrayList<>();
    private final List<Promotion> promotions = new ArrayList<>();

    public void sortProducts(SortStrategy sortStrategy) {
        sortStrategy.sort(products);
    }

    public void addProduct(Product product){
        products.add(product);
    }

    public List<Product> getProducts(){
        return products;
    }

    public void addPromotion(Promotion promotion){
        promotions.add(promotion);
        promotion.applyPromotion();
    }
    public void removePromotion(){
        if (!promotions.isEmpty()) {
            promotions.getLast().unApplyPromotion();
            promotions.removeLast();
        }
    }
    public List<Promotion> getPromotions(){
        return promotions;
    }


    public double calculateTotalPrice() {
        return products.stream().mapToDouble(Product::getDiscountPrice).sum();
    }
}
