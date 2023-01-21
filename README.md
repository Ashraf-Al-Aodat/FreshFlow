# **Fresh Flow Microservice**

This microservice is designed to help supermarkets efficiently place orders for items based on sales predictions, inventory levels, and order intake.

## **Getting Started**

To run this microservice, you will need to have Docker installed on your machine.

Clone the repository and navigate to the project directory in your terminal.

Run the following command to build the Docker image:

```
docker build -t docker/ .
```

Start the service by running:

```
docker run -p 5000:5000 --name flow flow
```

The microservice will be running on http://localhost:5000/.

You can access the data through the endpoint http://localhost:5000/orders

## **Project Structure**

The project is structured as follows:

- run.py: The entry point of the application.
- models.py: contain all the database models.
- views.py: contain the endpoint that serves the data.
- requirements.txt: contains all the python packages needed for the application to run.
- Dockerfile: contains instructions for building the Docker image.
- docker-compose.yml: contains configurations for the services that make up the application.

## **Data**

The data is served as a list of dicts, in JSON.

Each dict represents an order, for an item, for a day.

An order is a collection of information about the item, when it can be ordered, when it will be delivered, what’s the suggested retail price, what’s the profit margin, the purchase price, in which categories this item is in, any labels, how much there’s in a case of this stuff, how much they should order, and how much do they have in the inventory.
