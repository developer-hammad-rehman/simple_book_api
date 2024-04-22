from fastapi.testclient import TestClient
from simple_book_api.main import app , books,order_book
client = TestClient(app=app)
def test_home():
    response =  client.get('/')
    assert response.status_code == 200 
    assert response.json()  == {"messge" : "Welcome to simple book api"}
def test_books():
    response = client.get('/books')
    assert response.status_code == 200
    assert response.json() == books
def test_book_id():
    id : int = 10
    respones = client.get(f'/books/{id}')
    assert respones.status_code == 200
    assert respones.json() == [books[id - 1]]
def test_auth():
    email = "hammad"
    password = "12355"
    response = client.post('/auth', json={
   "email": email,
   "password":password
})
    assert response.status_code == 200
    assert response.json() == {'message' : "You are Autheniticate"}
def test_order():
    order_id : dict[str , int]  = {
        "id":1
    }
    response = client.post("/order", json = order_id)
    assert response.status_code == 200
    assert response.json() == {"message" : 'Your Order is placed'} or "No Email Id Found"
def test_myorder():
    response = client.get('/myorder')
    assert response.status_code == 200
    assert response.json() == order_book