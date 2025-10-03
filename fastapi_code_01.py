    

####  -------------------------------------------  code -01 

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}






####  -------------------------------------------  code -02

# from fastapi import FastAPI

# # Create a FastAPI instance
# app = FastAPI()

# # Define an asynchronous route
# @app.get("/calculate")
# async def calculate(x: int, y: int):
#     result = x + y
#     return {"result": result}




#### -----------------------------------------code -03

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float

# @app.post("/items")
# async def create_item(item: Item):
#     # Access variables like class attributes
#     item_name = item.name
#     item_price = item.price

#     return {
#         "message": f"Received item: {item_name} with price {item_price}",
#         "name": item_name,
#         "price": item_price
#     }


##### ----------------------------------------------------------- code -04 (Authentication and Authorization)
# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from passlib.context import CryptContext

# # Create a FastAPI instance
# app = FastAPI()

# # Define a password hashing context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Define an OAuth2 password bearer
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Simulated user database
# fake_users_db = {
#     "john@example.com": {
#         "username": "john@example.com",
#         "hashed_password": "$2b$12$ZfE4ifScm8Sj.VnJwp",
#         "disabled": False,
#     }
# }

# # Define a route that requires authentication
# @app.get("/protected")
# async def protected_route(token: str = Depends(oauth2_scheme)):
#     user_email = verify_token(token)
#     user = get_user(user_email)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return {"message": "You are authenticated"}

# # Verify the JWT token
# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
#         email: str = payload.get("sub")
#         if email is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return email
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

# # Get the user from the database
# def get_user(email: str):
#     if email in fake_users_db:
#         user_dict = fake_users_db[email]
#         return UserModel(**user_dict)

#     return None




#### ------------------------------------------------ code 05 ( use of get)

# from fastapi import FastAPI

# api=FastAPI()

# @api.get("/")
# def index():
#     return {"message":"Hello Shrawan , how are u?"}



# ## define a custom data base

# todo_db=[
#     {'todo_id':1, 'todo_name': 'morning', 'todo_desc':'wake up , fresh, and breakfast'},
#     {'todo_id':2, 'todo_name': 'exercise', 'todo_desc':'go for a run or workout'},
#     {'todo_id':3, 'todo_name': 'work', 'todo_desc':'complete daily tasks and meetings'},
#     {'todo_id':4, 'todo_name': 'lunch', 'todo_desc':'have a healthy meal'},
#     {'todo_id':5, 'todo_name': 'reading', 'todo_desc':'read a book or article'},
#     {'todo_id':6, 'todo_name': 'dinner', 'todo_desc':'prepare and eat dinner'},
# ]

# @api.get("/todos/{todo_id}")
# def get_todo(todo_id: int):   # 👈 declare type as int
#     for i in todo_db:
#         if todo_id==i['todo_id']:
#             return {'result': i}
        





#### ------------------------------------------------ code 06 ( use of post)



from fastapi import FastAPI
from pydantic import BaseModel


api=FastAPI()

class Todo(BaseModel):
    todo_id: int
    todo_name: str
    todo_desc: str


@api.get("/")
def index():
    return {"message":"Hello Shrawan , how are u?"}



## define a custom data base

todo_db=[
    {'todo_id':1, 'todo_name': 'morning', 'todo_desc':'wake up , fresh, and breakfast'},
    {'todo_id':2, 'todo_name': 'exercise', 'todo_desc':'go for a run or workout'},
    {'todo_id':3, 'todo_name': 'work', 'todo_desc':'complete daily tasks and meetings'},
    {'todo_id':4, 'todo_name': 'lunch', 'todo_desc':'have a healthy meal'},
    {'todo_id':5, 'todo_name': 'reading', 'todo_desc':'read a book or article'},
    {'todo_id':6, 'todo_name': 'dinner', 'todo_desc':'prepare and eat dinner'},
]



@api.post("/todos")
def create_todo(todo: Todo):
    todo_db.append(todo.dict())
    return {"message": "Todo created successfully", "todo": todo}



@api.get("/first_n_todo/{n}")
def get_n_todo_list(n:int):
    res=todo_db[:n]
    return {f"First {n} Todos":res}