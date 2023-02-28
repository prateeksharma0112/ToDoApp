Project Title : ToDo App

Project Description : A Simple To-Do App, In which User Can Create, Read, Edit and Delete To-Do.

1. We have HomePage, In which we have Add To-Do Button, by clicking on it, POP up will appear, in which Two Input Fields are Availabe, 
we have to Fill Title and Description and Click On Save, And To Do Will be added to Database also it will appear on the Screen.

2. On Each To-do we have Edit and Delete Button, where if we have to Edit the To-Do we have to click on Edit, a pop will appear
where we have the previous Value OF To-Do in Input Columns, we can Edit the Previous Data and click on Update then it will update 
the Values in Database also it will appear on Screen.

3. If the To-do is Completed we can Simply Delete that Particular To-Do, by clicking on DELETE button, a pop will appear for confirming to 
Delete that Particular To-Do, and if we click On Delete the To-Do will Be Deleted From Database.

4. We are Reading The To-Do's Directly From Database.

5. We are Performing the CRUD operations in Database.

6. we are Sending POST request From Frontend and Handling them in views.py

TechStack :
Backend - Python (Programming Language), Django (Framework), MongoDb (NoSQL Database)
Frontend - HTML, CSS, JavaScript, BootStrap

Structure For Our MongoDB Database

DB Name - ToDo_DB
Collection Name - TodoList
Document - {
    csrfmiddlewaretoken : "rnhewKoAOYamEMN2ENDtPscPtugxvij7iFnh215ACIQ671L3in2I7a3qE2DXGM9X"
    id : integer_value (To Identify Unique To-DO, assigning id Number -> 1,2,3,...) 
    title : "Title For TO-DO"
    description : "Description For TO-DO"
}

Installation and Run In Your Local System

System Reqirements - MongoDB, Python 3.10.6, Ubuntu 22.04.1 LTS
Tools - MongoDB Compass (For Visualization), VS Code Editor 

1. Create a virtual Environment and activate
     >>>  python -m venv toDoApp_venv
     >>>  cd toDoApp_venv
     >>>  source bin/activate

2. Download the requirements.txt File and install it.
     >>> pip install -r requirements.txt

3. Create toDoAppProject Folder and Clone the Project
     >>> mkdir toDoAppProject
     >>> cd toDoAppProject
     >>> git clone https://github.com/prateeksharma0112/ToDoApp.git

4. Start MongoDb server at local Host
     >>> sudo systemctl start MongoDB

     Check the status whether it is running or not
     >>> sudo systemctl status MongoDB --> it should be Active 

5.  Start the Application
    >>> python3 manage.py runserver



