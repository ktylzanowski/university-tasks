package Product;

public class Product implements Comparable<Product> {

    private final String code;
    private final String name;
    private final int price;
    private double discountPrice;

    public Product(String code, String name, int price) {
        this.code = code;
        this.name = name;
        this.price = price;
        this.discountPrice = price;
    }

    public String getCode() {
        return this.code;
    }

    public String getName() {
        return this.name;
    }

    public int getPrice() {
        return this.price;
    }

    public double getDiscountPrice() {
        return this.discountPrice;
    }

    public void setDiscountPrice(double discountPrice) {
        this.discountPrice = discountPrice;
    }

    @Override
    public int compareTo(Product otherProduct) {
        int priceComparison = Double.compare(this.discountPrice, otherProduct.discountPrice);
        if (priceComparison == 0) {
            return this.name.compareTo(otherProduct.name);
        }
        return priceComparison;
    }
}
