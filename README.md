# eSignAnyWhere is a Namirial-owned company that provides electronic signature solutions: https://www.esignanywhere.net/
## My script for batch user creation

It could be a useful tool for clients and internals who want to create users in larger quantities. Checks which are required:

- Line 8: Determine if the eSAW instance is correct. In the example, I'm using "latam," but you can change it if you desire.

- Line 9: Fill in the {APITOKEN} placeholder with your ApiToken.

- Line 12: It's reading the "users.csv" archive. It's the name I gave the archive I received from the client that contained the data from the users they asked me to create. Put what else you want.

- Line 32: There is the JSON object. As you can see, the users.csv file has on the column[0] the users FirstName, column[1] LastName, column[2] Email, and column[3] the TRUE parameter. It was the configuration they asked, but you can change it if you want. I removed the "Authentications" settings for security reasons, but feel free to add whatever you want.

- Line 63: The sleep time of 2 seconds is the amount of time between each API requests. Feel free to change it, but inserting less than this might cause the API to break and overload.

Product's swagger: https://latam.esignanywhere.net/swagger/?urls.primaryName=v5#/User/User_Create
