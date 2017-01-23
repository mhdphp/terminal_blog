
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

# student = [student for student in collection.find({})]
# print(student)

student_lastname = [student['last_name'] for student in collection.find({})]
print(student_lastname)
