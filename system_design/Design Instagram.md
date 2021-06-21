Design Instagram

Requirements:
1. Upload Images from a mobile client
2. Users follow other users
3. Generate a feed of images (newsfeed)
4. Scale: 10 million users

10 million users monthly basis
2 photos per month
5MB per photo

-> 10^7 * 2 (photos) * 5MB
-> 10^8 MB = 100,000,000 MB = 100 TB (month) -> 1.2PB (annually)

Users, Photos, Following DBs
Many-To-Many, One-To-Many...

User
|id|primary key, int, serial|                
|-----|----|
|name|string
|email|string|
|location|string


Photo
|id| primary key, int, serial|
|-----|----|
|user_id| foreign key, User.id|
|caption| string
|location| string
|path_url|string



Followers
|from_user| foreign keys referencing User.id|
|-----|----|
|to_user| foreign keys referencing User.id

* facebook friends are bi-directional