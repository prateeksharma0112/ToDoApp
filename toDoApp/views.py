from django.shortcuts import render, redirect
import pymongo

# Connect with Local Server
client = pymongo.MongoClient("mongodb://localhost:27017")
print("Welcome To PyMongo")

# Create a Database for ToDo
db = client["ToDo_DB"]

# create Collection for To-Do List
collection = db["TodoList"]

# count_id for assigning number
num = collection.count_documents({})


# View for Create ,Read, Update and Delete Operation In DataBase, To-Do APP
def homepage(request):
    global num
    
    # if request is POST
    if request.method == "POST":
        
        # to check whether to insert or perform action (Edit and Delete)
        e_data = request.POST.values()         # store data into e_data variable
        e_data = list(e_data)				   # convert it into list
        id = e_data[1]                         # store id into varaible
        
        # if id is empty then insert to-do record
        if id == "":
            # all values in POST Request
            e_data = request.POST.items()
            # make it dictionary
            toDo_data = dict(e_data)
            # add count_id as hidden value of every data list
            toDo_data['id'] = num
            # increment count id by 1
            num = num + 1
            
            # CREATE => Insert Into To-Do Data into Collection
            collection.insert_one(toDo_data)    
            # READ => Fetch To Do Data from DataBase
            toDo_data = collection.find({})
            toDo_data = list(toDo_data)
            context = {
                "toDo_data": toDo_data
            }
            return render(request, 'homepage.html', context)
        
         # if id has value then perform action => Edit or Delete
        else:
            # to check whether to delete or update
            e_data = request.POST.values()       # store data into e_data
            e_data = list(e_data)                # convert it into list
            # store value of e_data at 2nd Postion
            toDo = e_data[2]   

             # if toDo ==> del then To-Do will be deleted
            if toDo == "del":
                e_data = request.POST.values()   # store data into e_data
                e_data = list(e_data)            # convert it into list
                # store value of e_data at 1st Position in id to target
                id = int(e_data[1])
                # remove the Data at (id) index from DataBase
                collection.delete_one({'id': id})
                # READ => Fetch To-Do's from DataBase
                toDo_data = collection.find({})
                # Make it list
                toDo_data = list(toDo_data)
                context = {
                    "toDo_data": toDo_data
                }                
                return render(request, 'homepage.html', context)
            else:
                e_data = request.POST.items()    # store data into e_data
                e_data = dict(e_data)             # convert it into list
                # store value of e_data at 8th Postion into id to target
                id = int(e_data['edit-id'])
                # store new data
                naya_data = e_data
                # Update Values
                collection.update_one({'id': id},
                    {"$set":{'title': naya_data['title'], 
                            'description':naya_data['description'],
                }})

                # READ => Fetch To-do List Data from DataBase
                toDo_data = collection.find({})
                # Make it list
                toDo_data = list(toDo_data)
                context = {
                    "toDo_data": toDo_data
                }
                return render(request, 'homepage.html', context)

    # IF request is GET
    
    # READ => Fetch To-Do Data from DataBase
    toDo_data = collection.find({})
    # Make it list
    toDo_data = list(toDo_data)
    context = {
        "toDo_data": toDo_data
    }

    return render(request, "homepage.html", context)