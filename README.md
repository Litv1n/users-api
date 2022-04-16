# users-api
User's API source code

# Run API
1. Build Docker and docker-compose files

In the app directory run the commands below

```
docker build .
docker-compose build
```

2. Run a server
To run the server and use the user's api run the command

```
docker-compose up
```

Then go to the ```localhost:8000/docs``` to see all available URLs and methods available at these URLs. Then you can execute each URL with its method and see how the app works.

# Usage
### Create a user
Create a user or users using URL ```/create-user```.
### Get user list
If you have a user you can check it going to the ```/get-user-list``` URL. If you do not have any user you will see empty list.
### Search user by id
You can find each user using the ```userId``` by going to the URL ```/search/{userID}```.
### Update user password
Update user instance password using the ```userId``` by going to the URL ```/update-password/{userId}```.
### Delete user
Delete user instance using the ```userId``` by going to the URL ```/delete-user/{userId}
