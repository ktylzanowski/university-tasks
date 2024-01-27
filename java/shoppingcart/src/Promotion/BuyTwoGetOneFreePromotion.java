package Promotion;

import Product.Product;
import ShoppingCart.ShoppingCart;
import java.util.List;

public class BuyTwoGetOneFreePromotion implements Promotion {
    private final List<Product> products;
    public BuyTwoGetOneFreePromotion( ShoppingCart shoppingCart ){
        this.products = shoppingCart.getProducts();
    }

    @Override
    public void applyPromotion() {
        if (this.products.size() > 2) {
            this.products.sort(Product::compareTo);
            Product thirdCheapest = products.getFirst();
            thirdCheapest.setDiscountPrice(0);
        }
    }
    public void unApplyPromotion() {
        if (this.products.size() > 2) {
            this.products.sort(Product::compareTo);
            for (Product product : products) {
                if (product.getDiscountPrice() == 0 && product.getPrice() != product.getDiscountPrice()) {
                    product.setDiscountPrice(product.getPrice());
                    break;
                }
            }
        }
    }
}
