package Promotion;

import Product.Product;
import ShoppingCart.ShoppingCart;

import java.util.List;

public class OrderValuePromotion implements Promotion {

    private final List < Product > products;
    private final double totalPrice;

    public OrderValuePromotion( ShoppingCart shoppingCart ){
        this.products = shoppingCart.getProducts();
        this.totalPrice = shoppingCart.calculateTotalPrice();
    }
    @Override
    public void applyPromotion() {
        if (this.totalPrice > 300) {
            double discount = 0.95;
            for (Product product : products) {
                product.setDiscountPrice(product.getDiscountPrice() * discount);
            }
        }
    }
    @Override
    public void unApplyPromotion(){
        if (this.totalPrice * 1.05 > 300) {
            for (Product product : products) {
                product.setDiscountPrice(product.getDiscountPrice() * 1.05);
            }
        }
    }
}
