def main():
    store_a_product = {"Apples", "Bananas", "Cherries", "Watermelons"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

    # Find the common products (intersection) available in both stores
    common_products = store_a_product & store_b_products
    print(common_products)
    # alternative way
    common_products2 = store_a_product.intersection(store_b_products)
    print(common_products2)
    print()

    # Find all unique products (union) across both stores (A and B)
    all_products = store_a_product | store_b_products
    print(all_products)
    # alternative way
    all_products2 = store_a_product.union(store_b_products)
    print(all_products2)
    print()

    # Find prodcuts available in stire B but nor in store A (difference)
    store_b_exclusive = store_b_products - store_a_product
    print(store_b_exclusive)
    # alternative way
    store_b_exclusive2 = store_b_products.difference(store_a_product)
    print(store_b_exclusive2)
    print()

    # Find products that are in either store A or store B but not in both
    unique_to_either_store = store_a_product ^ store_b_products
    print(unique_to_either_store)
    # alternative way
    unique_to_either_store2 = store_a_product.symmetric_difference(store_b_products)
    print(unique_to_either_store2)
    print()

if __name__ == "__main__":
    main()