package Promotion;

import Product.Product;
import ShoppingCart.ShoppingCart;

import java.util.List;

public class FreeMugPromotion implements Promotion{
    private final List< Product > products;
    private final double totalPrice;
    private final Product freeMug = new Product("MUG", "Firmowy Kubek", 0);

    public FreeMugPromotion( ShoppingCart shoppingCart ){
        this.products = shoppingCart.getProducts();
        this.totalPrice = shoppingCart.calculateTotalPrice();
    }

    @Override
    public void applyPromotion() {
        if (this.totalPrice > 200) {
            products.add(this.freeMug);
        }
    }

    @Override
    public void unApplyPromotion() {
        products.remove(this.freeMug);
    }
}
