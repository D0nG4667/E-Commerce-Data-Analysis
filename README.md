# E-Commerce-Data-Analysis

This project demonstrates MongoDB concepts, including CRUD operations, aggregation, indexing, $lookup, schema design, and more. It uses a sample dataset to model, query, and analyze data. The project mirrors real-world scenarios encompassing building a MongoDB database for an e-commerce platform and using it to answer analytical questions.

The `project.ipynb` file in the notebook folder is detailed, explicit and insightful. The notebook consolidates all deliverables, including Python scripts for data insertion, analytical queries, and advanced tasks; MongoDB aggregation pipelines addressing analytical questions; schema design details with explanations on embedding vs. referencing and indexing strategies. Additionally, it includes a concise presentation summarizing the findings.

The JSON files in the dataset folder contains all the data that was loaded as collections to the database. The dataset used in this project has been generated solely for illustrative and educational purposes. All data, including names, email addresses, and other information, is entirely fictitious and does not correspond to any real individuals, organizations, or entities.

<a name="readme-top"></a>

## Schema Design Decisions

### 1. **Customers Collection**

- Stores customer information.
- Fields:
  - `_id`: MongoDB’s ObjectId for unique identification.
  - `customer_id`: A unique identifier for each customer.
  - `name`: Customer's full name.
  - `email`: Customer's email address.
  - `address`: Embedded document containing `street`, `city`, and `state` fields.

   **Reason**: The customer data is relatively small and self-contained, so an embedded schema is used to avoid unnecessary joins and ensure faster queries related to a customer’s full information.

### 2. **Products Collection**

- Stores product details.
- Fields:
  - `_id`: MongoDB’s ObjectId for unique identification.
  - `product_id`: A unique identifier for each product.
  - `product_name`: The name of the product.
  - `category`: The category the product belongs to.
  - `price`: The price of the product.

   **Reason**: Products are queried frequently by their `product_id`, and keeping the schema simple and normalized ensures consistency and easy updates for product information.

### 3. **Orders Collection**

- Stores information about customer orders.
- Fields:
  - `_id`: MongoDB’s ObjectId for unique identification.
  - `order_id`: A unique identifier for each order.
  - `customer_id`: Reference to the `customer_id` in the Customers collection.
  - `order_date`: Date and time when the order was placed.
  - `status`: Current status of the order (e.g., 'Shipped', 'Processing').

   **Reason**: Orders are stored in a referenced schema format. The `customer_id` field references the `Customers` collection, which keeps the order document light while allowing quick access to customer details.

### 4. **Order_Items Collection**

- Stores information about products in each order.
- Fields:
  - `_id`: MongoDB’s ObjectId for unique identification.
  - `order_item_id`: A unique identifier for each order item.
  - `order_id`: Reference to the `order_id` in the Orders collection.
  - `product_id`: Reference to the `product_id` in the Products collection.
  - `quantity`: The quantity of the product ordered.
  - `price`: The price of the product at the time of the order.

   **Reason**: This collection stores items in each order, and the references to `order_id` and `product_id` ensure that the database stays normalized. It also helps in scaling as more order items are added.

---

## Steps to Run the Scripts

1. **Setup MongoDB**:
   - Install MongoDB on your local machine or use a cloud service like MongoDB Atlas.
   - Ensure MongoDB is running on `localhost:27017` or any specified URI.

2. **Install Dependencies**:
   Install the necessary Python packages to interact with MongoDB:

### install

```bash
 pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- [Mongodb](https://cloud.mongodb.com/)

### Setup

Clone this repository to your desired folder:

```sh
  cd your-folder
  git clone https://github.com/D0nG4667/E-Commerce-Data-Analysis.git
```

Change into the cloned repository

```sh
  cd E-Commerce-Data-Analysis
  
```

After cloning this repo,

- Add an env folder in the root of the project.

- With your mongodb credentials, create an env file named `.env` using this sample

```env
# MONGO DB Atlas
MONGODB_USERNAME=bezos
MONGODB_PASSWORD=*********
MONGODB_URL=****.****.mongodb.net
```

- Navigate to notebook folder and run the project.ipynb:

```sh
cd notebook

```

## Sample Queries and Their Results

### 1. **Query: Create an Order**

- **Operation**: This operation inserts a new order into the `orders` collection and its associated items into the `order_items` collection. It also updates the product stock in the `products` collection.
- **Result**: The new order and order items are inserted atomically within a transaction.

    Example function to create an order:

    ```python
    create_order(1, [
        {"product_id": 9001, "quantity": 2, "price": 1200},
        {"product_id": 9002, "quantity": 1, "price": 800}
    ])
    ```

   **Expected Result**:

- A new order document is created in the `orders` collection with the status `Processing`.
- The `order_items` collection will contain two items linked to the created order.
- The stock of the products will be updated in the `products` collection.

### 2. **Query: Get the Maximum Product ID**

- **Operation**: The `generate_id_from_field` function uses an aggregation pipeline to find the maximum `product_id` in the `products` collection and increments it to generate a new ID.
- **Result**: The function returns the next available product ID.

   Example function to get the max product ID:

   ```python
   generate_id_from_field(products, 'product_id')
   ```

   **Expected Result**:
- The function will return the next available `product_id` (e.g., if the highest existing product ID is 120, it will return 121).

### 3. **Query: Get All Orders for a Customer**

- **Operation**: This query fetches all orders for a specific customer based on their `customer_id`.
- **Result**: A list of orders placed by the customer, including order IDs, statuses, and order dates.

   Example query:

   ```python
   orders.find({"customer_id": 1})
   ```

   **Expected Result**:
- A list of all orders placed by the customer with `customer_id = 1`.

### 4. **Query: Monitor Real-Time Changes in Orders**

- **Operation**: Uses MongoDB Change Streams to monitor changes in the `orders` collection and trigger actions when an order’s status is updated.
- **Result**: The system listens for changes (e.g., an order status update) and takes appropriate action in real-time.

   Example function to monitor changes:

   ```python
   def monitor_orders():
       change_stream = orders.watch()
       for change in change_stream:
           print(change)
   ```

   **Expected Result**:
- Real-time monitoring of any updates, deletions, or insertions in the `orders` collection.

---

## Contributions

### How to Contribute

1. Fork the repository and clone it to your local machine.
2. Explore the Jupyter Notebooks and documentation.
3. Implement enhancements, fix bugs, or propose new features.
4. Submit a pull request with your changes, ensuring clear descriptions and documentation.
5. Participate in discussions, provide feedback, and collaborate with the community.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Feedback and Support

Feedback, suggestions, and contributions are welcome! Feel free to open an issue for bug reports, feature requests, or general inquiries. For additional support or questions, you can connect with me on [LinkedIn](https://www.linkedin.com/in/dr-gabriel-okundaye).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👥 Authors <a name="authors"></a>

🕺🏻**Gabriel Okundaye**

- GitHub: [GitHub Profile](https://github.com/D0nG4667)

- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/dr-gabriel-okundaye)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟. Thank you!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 License <a name="license"></a>

This project is [MIT](/LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>