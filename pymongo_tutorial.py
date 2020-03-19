# Set up MongoDB sever
import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)

database = client.get_database("ConvenienceStore") # get database
coll_fruits = database.get_collection("Fruits") # get collection for fruits
coll_household_necessities = database.get_collection("HouseholdNecessities") # get collection for fruits

'''
# MongoDB assigns a unique ID to each document

coll_fruits.insert_one({"Type": "Banana",
                        "Brand": "Dole",
                        "Price": 2.50,
                        "ExpiryDate": "23/09/2020",
                        "DiscountCodes": "5% off"})

coll_household_necessities.insert_one({"Type": "ToiletPaper",
                                       "Brand": "Kleenex",
                                       "Price": 3.50,
                                       "DiscountCodes": ["10% off", "SUPERTOILETPAPER"]})

# Check the databases we have
databases = client.list_database_names()
print("Databases:", databases)
'''

''''
fruits = [{"Type": "Apple", "Brand": "Fuji", "Price": 1.10, "ExpiryDate": "21/10/2020"},
          {"Type": "Strawberry", "Brand": "Foxi", "Price": 3.10, "Quantity": 12, "ExpiryDate": "28/08/2020"}]
coll_fruits.insert_many(fruits)
'''


coll_fruits.delete_one({"Price": {"$lte": 3.10}})

# Check the Fruits collection
query = {}
all_fruits = coll_fruits.find(query)
print("Fruits:")
for fruit in all_fruits:
    print(fruit)


'''
# Check the HouseholdNecessities collection
all_household_necessities = coll_household_necessities.find({})
print("Household Necessities:")
for household_necessities in all_household_necessities:
    print(household_necessities)
'''
    
client.close()


