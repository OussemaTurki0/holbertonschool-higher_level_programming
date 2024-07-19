import requests

def test_products_json():
    response = requests.get('http://localhost:5000/products?source=json')
    assert response.status_code == 200, "Failed: Status code is not 200"
    content = response.json()
    assert any(product['name'] == 'Jarvis' for product in content), "Failed: Product 'Jarvis' not found in JSON source"

if __name__ == "__main__":
    test_products_json()
