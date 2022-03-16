import requests

# create an endpoint to jsonplaceholder
create_product_url = 'http://localhost:8000/api/product/'  # http://127.0.0.1:8000/

# all products endpoint
get_all_products_url = 'http://localhost:8000/api/products/'

def create_product(prodNum = 1, *args , **kwargs):
    '''create a product'''
    product = f"product{str(prodNum)}"
    print(product)
    json = {
        "name": product,
        "description": "This is a product description",
        "price": 10.00,
    }
    response = requests.post(create_product_url, json=json)
    return response


# get all products
def get_all_products():
    '''get all products'''
    response = requests.get(get_all_products_url)
    return response


# main function
def main():
    # response = create_product(1)
    response = get_all_products()
    print(response)


if __name__ == '__main__':
    main()
