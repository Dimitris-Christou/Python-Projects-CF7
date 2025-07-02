from typing import List, Tuple, dict, Optional, Any




def get_results(products, **kwargs):
    results = [
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') >= price

    ]
    return results


def main():
    products = [("lenovo", 100), ("lenovo", 40), ("ibm", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    print(get_results(products, **criteria)) 

if __name__ == "__main__":
    main()