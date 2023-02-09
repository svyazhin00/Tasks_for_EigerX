def priceCheck(products: list, productPrices: list, productSold: list, soldPrice: list):
    errors = 0
    product_dict = dict(zip(products, productPrices))

    for i in range(len(productSold)):
        if productSold[i] in products:
            if product_dict[productSold[i]] != soldPrice[i]:
                errors += 1
        else:
            raise KeyError(f'Product {productSold[i]} is not in the stores database')
    return errors


print(priceCheck(
    products=['eggs', 'milk', 'cheese'],
    productPrices=[2.89, 3.29, 5.79],
    productSold=['eggs', 'eggs', 'cheese', 'milk'],
    soldPrice=[2.89, 2.99, 5.97, 3.29]
))
