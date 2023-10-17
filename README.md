# Contact_Manager
This is Contact Manager Api Created Using Django Rest Framework, where One can post the data of person (name,phone,email,address) and store it to database 
One can see the data by following steps , Search data using name or phone number , and delete the data from database

#Steps
It us an API for Contact Manager problem
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser #e.g. Email : super@example.com Organizer name : name of user password : 1234
5. python manage.py runserver

After that on any API Tool (like postman)
1. to add user POST request on http://127.0.0.1:8000/ example : json data
{
    "name": "Radha",
    "phone": 63878788,
    "email": "abc@jh.com",
    "address": "vishwakarma Nagar"
}
This will add the Contact

2. To see all data GET request on http://127.0.0.1:8000
it will show data like following
[
    {
        "id": 3,
        "name": "Ramesh",
        "phone": 6387886,
        "email": "abc@jh.com",
        "address": "vishwakarma Nagar"
    },
    {
        "id": 4,
        "name": "Sunita",
        "phone": 938789786,
         "email": "asc@jh.com",
        "address": "vishwakarma Nagar"
    },
    {
        "id": 5,
        "name": "Radha",
        "phone": 63878788,
        "email": "fgj@jh.com",
        "address": "vishwakarma Nagar"
    }
]
3. To search the user using phone no or name
GET request on http://127.0.0.1:8000?name=Radha or http://127.0.0.1:8000?phone=63878788.
 It will show results as following.
[
    {
        "id": 5,
        "name": "Radha",
        "phone": 63878788,
        "email": "abc@jh.com",
        "address": "vishwakarma Nagar"
    }
]

4. To search the user using phone no or name
DELETE request on http://127.0.0.1:8000/functions/?name=Radha . It will show results as following.
{
    "msg": "contact deleted"
}
