Table Customers {
  customer_id int [pk]
  first_name varchar
  last_name varchar
  email varchar
  phone varchar
}

Table Customer_Addresses {
  address_id int [pk]
  customer_id int
  address varchar
  city varchar
  postcode varchar
}

Table Products {
  product_id int [pk]
  product_name varchar
  price decimal
  category_id int
}

Table Categories {
  category_id int [pk]
  category_name varchar
}

Table Orders {
  order_id int [pk]
  customer_id int
  order_date date
}

Table Order_Items {
  order_item_id int [pk]
  order_id int
  product_id int
  quantity int
}

Ref: Customer_Addresses.customer_id > Customers.customer_id
Ref: Orders.customer_id > Customers.customer_id
Ref: Order_Items.order_id > Orders.order_id
Ref: Order_Items.product_id > Products.product_id
Ref: Products.category_id > Categories.category_id