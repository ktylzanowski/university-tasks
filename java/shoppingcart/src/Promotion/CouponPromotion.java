package Promotion;

import Product.Product;
import ShoppingCart.ShoppingCart;

import java.util.List;

public class CouponPromotion  implements Promotion{
    private final String productCode;
    private final List< Product > products;

    public CouponPromotion(String productCode, ShoppingCart shoppingCart) {
        this.productCode = productCode;
        this.products = shoppingCart.getProducts();
    }
    @Override
    public void applyPromotion() {
        double discount = 0.7;
        this.products.stream()
                .filter(product -> product.getCode().equals(productCode))
                .findFirst()
                .ifPresent(selectedProduct -> selectedProduct.setDiscountPrice(selectedProduct.getDiscountPrice() *
                        discount));
    }
    @Override
    public void unApplyPromotion(){
        this.products.stream()
                .filter(product -> product.getCode().equals(productCode))
                .findFirst().ifPresent(selectedProduct -> selectedProduct.setDiscountPrice(selectedProduct.getPrice()));
    }
}
