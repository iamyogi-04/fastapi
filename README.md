# fastapi

1. If app is not running then create a environment using {pip install virtualenv}then write this command {python -m venv (name of your choice)}

2.After creating the environment install following :
=> pip install fastapi[all]
=> pip install sqlalchemy
=> pip install geopy

3.After installing dependencies we have to activate the environment using command activate

4 For that activation we have to get inside the file we created using step-1 (name) folder to go inside it use cd/name/Scripts
and type command {act} then press tab button and then enter button

5.Then go to the root directory then for running the server use command {uvicorn crud:app --reload} then press enter 

6. Now your server is running on port (http://127.0.0.1:8000) add /docs to perform CRUD OPERATIONS

7. After creating  address check latitude and longitude and copy paste that inside google maps search bar and then your location is visible or u can check mapurl and directly click on it and it will show the location


