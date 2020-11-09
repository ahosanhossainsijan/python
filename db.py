from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
print(client)
db = client['my_database']
print(db)
courses=db.courses
print(courses)
'''EnglishCourse={
'TotalStudent':40,
'PassedStudent':36,
'DroppedStudent':2,
'FailedStudent':2,
}
#result = courses.insert_one(EnglishCourse)
#print(EnglishCourse)
#if result.acknowledged:
# print('course added. The course id is: '+ str(result.inserted_id()))'''
courseList = [
    {
        'TotalStudent':40,
        'PassedStudent':36,
        'DroppedStudent':2,
        'FailedStudent':2,
    },{
            'TotalStudent':40,
            'PassedStudent':34,
            'DroppedStudent':3,
            'FailedStudent':3,
            },
    {
        'TotalStudent':40,
        'PassedStudent':32,
        'DroppedStudent':1,
        'FailedStudent':7,
        },
]
result = courses.insert_many(courseList)
for object_id in result.inserted_ids:
    print('Course Added. Course Id = ',str(object_id))






