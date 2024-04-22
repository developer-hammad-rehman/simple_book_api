import random
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="Simple Book Api",
)
class Order_Books(BaseModel):
    id : int
class Auth(BaseModel):
    email : str
    password:str
class Update(BaseModel):
    id : int
email : str =''
password : str = ''
books = [
    {
        "id": 1,
        "name": "Python",
        "author": "Hammad",
        "price": 100,
        "genre": "Programming",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 2,
        "name": "Javascript",
        "author": "Bilal",
        "price": 400,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 3,
        "name": "TypeScript",
        "author": "Saqib",
        "price": 300,
        "genre": "Programming",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 4,
        "name": "Nextjs",
        "author": "Fatima",
        "price": 200,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 5,
        "name": "Data Science with Python",
        "author": "Alex",
        "price": 250,
        "genre": "Data Science",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 6,
        "name": "React.js Essentials",
        "author": "Emily",
        "price": 180,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 7,
        "name": "Java Fundamentals",
        "author": "Michael",
        "price": 150,
        "genre": "Programming",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 8,
        "name": "Angular Mastery",
        "author": "Sophie",
        "price": 300,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 9,
        "name": "Machine Learning in Practice",
        "author": "David",
        "price": 280,
        "genre": "Machine Learning",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 10,
        "name": "DevOps Handbook",
        "author": "Lisa",
        "price": 220,
        "genre": "DevOps",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 11,
        "name": "Cybersecurity Essentials",
        "author": "Jake",
        "price": 260,
        "genre": "Cybersecurity",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 12,
        "name": "Vue.js for Beginners",
        "author": "Olivia",
        "price": 170,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 13,
        "name": "Django Unleashed",
        "author": "Daniel",
        "price": 190,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 14,
        "name": "Swift Programming",
        "author": "Emma",
        "price": 230,
        "genre": "Programming",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 15,
        "name": "Azure Cloud Essentials",
        "author": "Ryan",
        "price": 320,
        "genre": "Cloud Computing",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 16,
        "name": "GraphQL Basics",
        "author": "Sophia",
        "price": 200,
        "genre": "Web Development",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 17,
        "name": "Rust Programming",
        "author": "William",
        "price": 250,
        "genre": "Programming",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
    {
        "id": 18,
        "name": "AWS Solutions Architect",
        "author": "Victoria",
        "price": 380,
        "genre": "Cloud Computing",
        "rating": random.uniform(3.0, 5.0),
        "published_year": random.randint(2000, 2022),
        "language": "English",
    },
]
order_book : list[dict[str , int|str]] = []
@app.get('/')
def root_route():
    print(email , password)
    print(order_book)
    return {"messge" : "Welcome to simple book api"}
@app.get('/books')
def books_home_route():
    return books
@app.get('/books/{id}')
def book_routes(id : int):
   fil = filter(lambda x : x['id'] == id , books)
   book = list(fil)
   if book:
        return book
   else :
       return "No book Avaliable"
@app.post('/order')
def order_books(id : Order_Books):
    if email and password:
     fil = filter(lambda x : x['id'] == id.id, books)
     book = list(fil)
     print(book)
     order_book.append(*book)
     return {"message" : 'Your Order is placed'}
    else:
        return "No Email Id Found"
@app.post('/auth')
def auth_route(auth:Auth):
    global email
    global password 
    email = auth.email
    password = auth.password
    return {'message' : "You are Autheniticate"}
@app.get('/myorder')
def myorder_route():
    return order_book
@app.patch('/order/{id}')
def order_update_route(id: int ,  orderId : Update):
     fil = list(filter(lambda x : x['id'] == orderId.id , books))
     for  i  in order_book:
         if i["id"] == id:
            order_book[order_book.index(i)] = fil[0]
            return order_book
         else:
             "Not any data found"
@app.delete('/order/{id}')
def order_delete_route(id : int):
   for  i  in order_book:
         if i["id"] == id:
            order_book.pop(order_book.index(i))
   return order_book