# [eSignAnyWhere](https://www.esignanywhere.net/) is a Namirial-owned company that provides electronic signature solutions

[Product's swagger](https://latam.esignanywhere.net/swagger/?urls.primaryName=v5#/User/User_Create)

## My script for batch user creation: user-create-batch.py

It could be a useful tool for clients and internals who want to create users in larger quantities. Checks which are required:

- Line 8: Determine if the eSAW instance is correct. In the example, I'm using "latam," but you can change it if you desire.

- Line 9: Fill in the {APITOKEN} placeholder with your ApiToken.

- Line 12: It's reading the "users.csv" archive. It's the name I gave the archive I received from the client that contained the data from the users they asked me to create. Put what else you want.

- Line 32: There is the JSON object. As you can see, the users.csv file has on the column[0] the users FirstName, column[1] LastName, column[2] Email, and column[3] the TRUE parameter. It was the configuration they asked, but you can change it if you want. I removed the "Authentications" settings for security reasons, but feel free to add whatever you want.

- Line 63: The sleep time of 2 seconds is the amount of time between each API requests. Feel free to change it, but inserting less than this might cause the API to break and overload.

## My script for batch user modification: user_authentication_update.py

It could be a useful tool for clients and internals who want to modify users in larger quantities. Checks which are required:

- Line 6: Determine if the eSAW instance is correct. In the example, I'm using "latam," but you can change it if you desire.

- Line 9: Fill in the {APITOKEN} placeholder with your ApiToken.

- Line 12: It's reading the "users.json" archive. It's the name I gave the archive I gather from the esaw endpoint "v5/user/find" that contained the data from all users from the organization I am inserted. Put what else you want.

- Line 35: The dict object is there. To be more specific, the users.json file contains the results of all users from the organization into which my user is inserted. So basically the Json contains the userId which is going to the URL for each request, and the email which is going to "UserIdentifierAttibuteValue" in "Authentications". The authentication method was the part I was asked to change on the users, but you can change any other detail from the users, just check the product's swagger and see what else you can change here: [Product's swagger](https://latam.esignanywhere.net/swagger/?urls.primaryName=v5#/User/User_Update)

- Line 55: The sleep time of 2 seconds is the amount of time between each API requests. Feel free to change it, but inserting less than this might cause the API to break and overload.
