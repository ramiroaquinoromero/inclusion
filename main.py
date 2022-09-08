import json
import datetime

"""
QUESTION #1

Create a base class with:
●	Three properties initialized at construction
●	One empty classmethod
●	One empty instance method

"""


class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    @classmethod
    def make_string_name_age(cls, name, age):
        pass

    def get_age(self):
        pass


"""
QUESTION #2

Create a derived class from the base class
●	Inherits all properties and methods from the base class
●	Initialize the properties differently from the base class
●	Add code to the empty methods

"""


class User(Person):
    def __init__(self, name, sex, age, mail):
        super().__init__(name, sex, age)
        self.mail = mail

    def get_age(self):
        return f"The current age is: {self.age}"

    @classmethod
    def make_string_name_age(cls, name, age):
        return f"The user {name} is {age} years old."


p = Person("Ramiro", "Male", 28)
# print(p)
# print(p.name)

u = User("Ramiro", "Male", 28, "ramiroaquinoromero@gmail.com")
# print(u.get_age())
# print(u.make_string_name_age(u.name, u.age))


"""
QUESTION #3

Use list comprehension and a lambda function to extract all of the even integers out of a list of integers.

"""

list_comprehension = [1, 2, 3, 4, 5, 6]
list_comprehension_1 = [x for x in range(1, 11)]

even_integer_list = [number for number in list_comprehension_1 if number % 2 == 0]
# print(even_integer_list)

even_integers_lambda = list(filter(lambda num: (num % 2 == 0), list_comprehension))
# print(even_integers_lambda)


"""
QUESTION #4

Use the next() function to find the first element in a list of dictionaries whose attribute ‘x’ = 5. 
Default to an empty dictionary if not found.

"""

values = [
    {"name": "A", "x": 10},
    {"name": "B", "x": 5},
    {"name": "C", "x": 7},
    {"name": "D", "x": 10}
]
result = next((item for item in values if item["x"] == 10), {})
# print(result)

"""
QUESTION #5

●	Read in the document from a file
●	Find and print:
●	The Payee ID value
●	Any invoices that contain the text “583”
●	Change any date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
●	Hint: The format of the date/time fields are integer timestamp. To create a datetime object from an integer 
    timestamp, use the following: datetime_obj = datetime.datetime.fromtimestamp(integer_timestamp / 1e3)
●	Write the json document back out to a new file

"""

with open('./data.json', 'r') as f:
    data = json.load(f)

# The Payee ID value
payee_id_value = data.get("payee", {}).get("id", None)

# Any invoices that contain the text “583
invoice_values = data.get("invoiceIds", [])
contain_text = "583"
result = []

if len(invoice_values) > 0:
    result = [invoice for invoice in invoice_values if contain_text in invoice]
# print(result)


def convert_integer_timestamp(integer_timestamp: int):
    return datetime.datetime.fromtimestamp(integer_timestamp / 1e3).strftime('%Y-%m-%dT%H:%M:%S')


fields_datetime = ["claimDateTime", "fileDateTime", "receivedDateTime"]

for field in fields_datetime:
    value = data.get(field, None)
    if value is not None:
        data[field] = convert_integer_timestamp(value)
with open("./new_data.json", "w") as outfile:
    json.dump(data, outfile)

print("Json File created correctly.")

