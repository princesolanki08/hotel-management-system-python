from pymongo import MongoClient

#  connect to Mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client["School"]
details = db["Student"]

#  Insert 5 document in the student collection
details.insert_many([
    {"Rollno": 1,"Name": "Prince", "Cource": "MCA", "Marks": 93, "Grade_Point": "A"},
    {"Rollno": 2,"Name": "Pravin", "Cource": "MCA", "Marks": 83, "Grade_Point": "B"},
    {"Rollno": 3,"Name": "Akshay", "Cource": "MBA", "Marks": 78, "Grade_Point": "B"},
    {"Rollno": 4,"Name": "Vishwa", "Cource": "MCA", "Marks": 91, "Grade_Point": "A"},
    {"Rollno": 5,"Name": "Bihari", "Cource": "MBA", "Marks": 72, "Grade_Point": "B"},
])

#  find Student having marks 80 to 90
for det in details.find({"Marks": {"$gte":80,"$lte":90}}):
    print(det)
    
#  Update name of a Student whose roll no is 5
details.update_one({"Rollno":5},{"$set":{"Name":"Harsh"}})

    
#  Display top 3 student according to their grade point
for det in details.find().sort("Grade_Point",1).limit(3):
    print(det)


#  display Student having highest grade point
for det in details.find().sort("Grade_Point",-1).limit(1):
    print(det)


#  Find all student having cource MCA
for det in details.find({"Cource": "MCA"}):
    print(det)
    
#  Display all student in descending order of marks
for det in details.find().sort("Marks",-1):
    print(det)