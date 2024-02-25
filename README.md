<h3>Product inventory management system</h3>

1. First you need to make a git clone of our project
> git@github.com:tturdumamatovv/reviro.git


2. Here we create a virtual environment (for linux)
> python3 -m venv venv


3. Next, download all the libraries
> pip install -r requirements.txt


4. Then you need to create tables in the database
> alembic upgrade head


5. Then we can launch our website using docker
> sudo docker-compose up -d --build

or
> docker-compose up -d --build 


6. Next we go to swagger,
here is a link to swagger after launching docker
> http://localhost:8080/docs#/


7. We can go through all the queries for products and establishments, just do not rush to delete products and establishments with id = 1, we will need them to check the tests
----------------------
<h3>Products</h3>

1. - To create a product, endpoint(post) "/products"
> {
  "name": "Banana",
  "description": "Yellow",
  "price": 10,
  "quantity_in_stock": 20
}
* We are sending such a request, this is just an example, you can transfer any data, and after sending we successfully create a product


2. - Get a list of products, endpoint(get) "/products"
> there is nothing here to transfer to the body, because we receive all the products, however, there are limits, we can supply at will or there is a default from 0 to 10 products coming out


3. - Get one product, endpoint(get) "products/{product_id}"
> here we pass in product_id, the id of the product we want to get, and successfully get one product


* Delete a product, endpoint(delete) "products/{product_id}"
> here we pass in product_id, the id of the product we want to delete, and successfully delete the product

<h3>Establishments</h3>

1. - To create a establishments, endpoint(post) "/establishments"
> {
  "name": "Jiraffe",
  "description": "They make the best coffee",
  "locations": "Gorky Street crosses Panfilov",
  "opening_hours": "from 08:00 to 00:00"
}
* We are sending such a request, this is just an example, you can transfer any data, and after sending we successfully create a establishment


2. - Get a list of establishment, endpoint(get) "/establishments"
> there is nothing here to transfer to the body, because we receive all the establishments, however, there are limits, we can supply at will or there is a default from 0 to 10 establishments coming out


3. - Get one establishment, endpoint(get) "establishments/{establishment_id}"
> here we pass in establishment_id, the id of the establishment we want to get, and successfully get one establishment


4. - Delete a establishment, endpoint(delete) "establishment/{establishment_id}"
> here we pass in establishment_id, the id of the establishment we want to delete, and successfully delete the establishment

------------------------------------------------------

8. To run the tests, we use the container id, to get the container id we use the following code
> sudo docker ps 

or
> docker ps

9. Now we can run the tests with this code and take the container_id with the code above
> sudo docker exec <container_id> pytest tests/

or
> docker exec <container_id> pytest tests/



<h2>A private message that has nothing to do with the project launches</h2>


<h4>I would like to add something from myself, in the beginning the test could only be done on flask or fastapi. And I chose fastapi, then you updated the test assignment and added django, I can say that I know django better than fastapi or flask, but I think there is no need to write everything in django, I hope those who did the test assignment on flask or fastapi will have more privileges to join you for an internship. Thank you, I hope you enjoy everything.

Good luck!</h4>