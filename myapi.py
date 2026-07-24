# ## API notes
# 1. GET - read or get data
# 2. POST - create date
# 3. PATCH - partial update
# 4. PUT - replace an entire resource
# 5. DELETE - remove a resource

# RESTfil principles:
# 1. Client-Server seraration
# 2. Statekessness - server stories no session state about the client
# 3. Cachebility - response need to indicate weather they are chaceable
# 4. Uniform interface 
# 5. Layered System 
# 6. Code on demand (optional)

from fastapi import FastAPI

app = FastAPI()

# Fake DB
books = [
    {"id":1, "title":"Harry Potter", "available":True},
    {"id":2, "title":"Game of Thrones", "available":True},
    {"id":3, "title":"Dune", "available":True}
]

# Home route
@app.get("/")
def home():
    return {"message":"Joes library API"}


# get all books
@app.get("/books")
def get_books():
    # connect to db
    # run sql
    # get outputs
    # tidy
    # format and return
    return books