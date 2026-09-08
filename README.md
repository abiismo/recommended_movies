# Splitwise CLI — Shared Expense Manager

## About

This algorithm takes a group of people as input. A lead person joins the group and pays the total amount. It also calculates the amount each person owes, and if someone has paid, the algorithm receives this information and saves the changes to the database.

## Prerequisites


##### Before you continue, ensure you have met the following requirements:

* you have the latest version of python 
* you have the flask librarie already installed 
* have a knowledge about SQL statements 
* and basic use of postman app to apply people inside of the algorithm


## Installation

##### Follow these steps to install everything correctly.

* Clone the repository
* Install dependencies 
* Configure the .env
    ```
    DB_HOST=
    DB_USER=
    DB_PASSWORD=
    DB_NAME=
    ```
* Create a database with the schema
* run main.py


```bash
git clone https://github.com/tuusuario/splitwise.git
cd splitwise
pip install flask mysql-connector-python python-dotenv
```


## Usage

### GET /owes
Returns the net debt between two users.

**Params:** `user_a`, `user_b`

**Example:** http://localhost:5000/owes?user_a=2&user_b=1

**Response:**
```json
{"deuda_neta": 30000.00}
```
 
### POST /payment
record a payment between the person who owes money and the person who paid all the expenses

**Params:** `payer_id`, `receiver_id`, `amount`

**Example:** http://127.0.0.1:5000/payment

**Body:**

```json
{
    "payer_id": 2,
    "receiver_id": 1,
    "amount": 30000
}



### POST /expenses
Insert a record of expense into a database

**Params:** `paid_by`, `amount`, `id_group`, `description`, `list_participants`

**Example:** http://127.0.0.1:5000/expenses

**Response:**
```json
{"detalle_gasto": "22"}
```

**Body:**

```json
{
    "paid_by": 1,
    "amount": 90000,
    "id_group": 1,
    "description": "Cena",
    "list_participants": [
        [1, 30000],
        [2, 30000],
        [3, 30000]
    ]
}   
```




















