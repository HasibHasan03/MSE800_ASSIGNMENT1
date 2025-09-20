from graphviz import Digraph

# Create a new directed graph
dot = Digraph("CarRentalERD", format="png")
dot.attr(rankdir="LR", size="8")

# Define entities (tables)
dot.node("User", """User
--------------------
user_id (PK)
username
password
role""", shape="record")

dot.node("Car", """Car
--------------------
car_id (PK)
make
model
year
mileage
available
min_rent_days
max_rent_days
daily_rate""", shape="record")

dot.node("Rental", """Rental
--------------------
rental_id (PK)
customer_id (FK)
car_id (FK)
start_date
end_date
status""", shape="record")

# Define relationships
dot.edge("User", "Rental", label="1..*")
dot.edge("Car", "Rental", label="1..*")

# Render to file
output_path = "car_rental_erd"
dot.render(output_path, format="png", cleanup=True)

output_path + ".png"
