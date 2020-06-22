# DRF
### Examples on django rest framework. 

### Python 3.6.10 

- **step1**: Install dependancies from /Ecommerce/requirement.txt
- **step2**: Run commands
```
./manage.py makemigrations 
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

- **step3**: Login with superuser 
    - Add products from admin panel

- **APIs**:
    - Login with super user : (POST)http://127.0.0.1:8000/login (Token will be received in response. Use this token to add new user.)
        - Body : {
                    "username": "admin",
                    "password": "admin" }
                    
    - Register a user in app : (POST)http://localhost:8000/shop/users/add
        - Body : {
                "name": "aditya",
                "email": "adtiya@sharma.com",
                "contact_number": "99819287233",
                "username":"aditya",
                "password":"12345678"}
        - Header : Authorization:Token *your_token*
    - Login with newly created user : (POST)http://127.0.0.1:8000/login (Token will be received in response. Use this token to perform crud operations.)
        - Body : {
                    "username": "aditya",
                    "password": "12345678" }
        - Header : Authorization:Token *your-token*
                    
    - Added product in cart: (POST)http://localhost:8000/shop/users/cart/add
        - Body : {
                        "user":1,
                        "product": 1,
                        "quantity": 11
                    }
        - Header : Authorization:Token *your_token*
    - Fetch user cart items : (GET)http://localhost:8000/shop/users/**user-id**/cart
        - Header : Authorization:Token *your-token*

    - Delete cart item: (DELETE)http://localhost:8000/shop/users/**user-id**/cart/item/**product-id**
        - Header : Authorization:Token *your-token*
    
    - Update cart item: (PUT)http://localhost:8000/shop/users/**user-id**/cart/item/**product-id**
        - Body : {"quantity": 5}
        - Header : Authorization:Token *your_token*
        
        
#### Admin user can perform all CRUD operation

#### But Newly added user can only view cart and add product in cart but cann't remove/update cart item.
        
    
    
    
    
    
