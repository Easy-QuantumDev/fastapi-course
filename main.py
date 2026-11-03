from fastapi import FastAPI
from fastapi.responses import JSONResponse




"""
this is for test model for user

"""
# from pydantic import BaseModel

# class User(BaseModel):
#     name:str
#     age:int
    
    
app= FastAPI()
@app.get('/')
def hello():
    return{
        'message':'hello world'
    }


# @app.get('/about')
# def about():
#     return {
#     "name": "Mohammad",
#     "job": "Backend Developer",
#     "framework": "FastAPI"
# }    



    """
    path parameters
    """

# @app.get('/users/{user_id}')
# def find_user(user_id:int):
#     return{
#         'user_id':user_id
#     }


# @app.get("/products/{product_id}")
# def find_product(product_id:int):
#     return {
#         'product_id':product_id
#     }


    """
    query parameters
    """
# @app.get('/products')
# def get_product(category:str,limit:int):
#     return{
#         'category':category,
#         "limit":limit,
#     }
    
    
"""
optional parameters

 """    
# @app.get("/products")
# def get_product(category:str|None=None, limit:int=10):
    
#     return{
#         'category':category,
#         'limit':limit
#     }



"""

create user with post method with JsonBody

"""


    
# @app.post('/users')
# def create_user(user:User):
#     return{
#         'message':'User Created',
#         'name':user.name,
#         'age':user.age,
        
#     }    



# products = [
#     {
#         "id": 1,
#         "name": "Laptop",
#         "price": 1200
#     },
#     {
#         "id": 2,
#         "name": "Phone",
#         "price": 800
#     },
#     {
#         "id": 3,
#         "name": "Headphone",
#         "price": 150
#     }
# ]



"""
show all products

"""
# @app.get("/products")
# def get_products():
#     return products



"""
find product with query parameters

"""

# @app.get("/products/{id}")
# def find_product(id:int):
#     for product in products:
#         if product['id'] == id:
#             return product
#     return {
#         'messages':"product not found"
#            }




"""

HTTPException , Status Code

"""

# from fastapi import HTTPException

# products = [
#     {
#         "id": 1,
#         "name": "Laptop",
#         "price": 1200
#     },
#     {
#         "id": 2,
#         "name": "Phone",
#         "price": 800
#     },
#     {
#         "id": 3,
#         "name": "Headphone",
#         "price": 150
#     }
# ]




# @app.get("/products/{id}")
# def find_product(id:int):
#     for product in products:
#         if product['id'] == id:
#             return product
#     raise HTTPException(status_code=404,detail='Product Not Found! ')



"""

json response

"""
users = [
    {
        "id": 1,
        "name": "mohammadreza",
    },
    {
        "id": 2,
        "name": "alireza",
    },
    
]



@app.get("/users")
def get_users():
    return JSONResponse(
        status_code=200,
        content={
            'message':'hello world',
            'data':users
        }
        
    )