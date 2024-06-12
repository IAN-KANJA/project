# from Payment import payment
# payment.create_table()
# Payment1 = payment.create(
#     "Cristian", "Olufsen", "Male","20000"
# )
# main.py
from payment import Payment

# Create the table
Payment.create_table()

# Create a new payment entry
payment1 = Payment.create(
    "Cristian", "Olufsen", "Male", "20000"
)

# Print the created payment entry
# print(payment1)
