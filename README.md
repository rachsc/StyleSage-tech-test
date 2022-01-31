# EXERCISES 1 AND 2

## Requirements
- Python 3.8
- Django 4.0
- CSV
- Coverage (Optional for testing)

## Installation
After you cloned the respository, you want to create a virtual environment, so you have a clean python installation. 
```
python -m venv env
```
Once you´ve created a virtual environment, you may activate it.
```
(On Windows): env\Scripts\activate.bat
(On Unix or MacOS): source env/bien/activate
```
You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Endpoints
In this REST API, you can find some endpoints that define its structure and how you can access data from the application using HTTP methods - GET, POST

Endpoint | HTTP Method | CRUD Method | Result
---|---|---|---
upload| POST | CREATE | Upload artists images to django database
register | POST | CREATE | Create new user and lets you already logged in
download-artists | GET | READ | Download csv file of the artists database
 | GET | READ | Home page
artists | GET | READ | Get list of Artists
artists/<str:ID> | GET | READ | Get one artist with a list of their albums
albums | GET | READ | Get a list of all the albums with artist name, track count, total album duration, longest track duration and shortest track duration.
albums/<str:ID> | GET | READ | Get one album with its information.
accounts/login | POST | CREATE | Log in 
accounts/logout/?next=/ | POST | CREATE | Log out and redirects to home page
passphrase/basic | POST | CREATE | Tells how many of the passphrases you entered does not contain duplicate words
passphrase/advanced| POST | CREATE | Tells how many of the passphrases you entered does not contain words that are anagrams of others


## Use
You can test the API using cURL, httpie, Postman or a web browser (among other things). In this documentation I am going to show you how to test it with the web browser for and easier understanding as these are the most visual options and the ones I used.

First, you have to start up Django´s development server.
```
python manage.py runserver
```

### Exercise 1
Using chiknoob.db provided by https://www.sqlitetutorial.net/sqlite-sample-database, this app has a database of songs, albums and artists.

The home page will be in https://127.0.0.1:8000. From here, we can access the access points by clicking at the elements in the top bar of the web page:

1. Click on **Artists** or go to https://127.0.0.1:8000/artists to see the list of artists. Authentication is NOT required.
   

2. Now you can click on any artist of the list. You will be redirected to http://127.0.0.1:8000/artists/<id:pk> where you can see the albums of the artist and an image of the artist if you uploaded one to the database (this is explained in the repository for Exercise 3: https://github.com/rachsc/StyleSage-tech-tes-Exercise3).
   Authentication it IS required.
   

3. Click on **Albums** or go to https://127.0.0.1:8000/albums to see the list of albums. Below each album you´ll find its artist, number of tracks, album duration, the longest track duration and shortest track duration.
Authentication it IS required.
  
 
4. Now you can click on any album of the list. You will be redirected to http://127.0.0.1:8000/albums/<id:pk> where you can find the list of songs of that album.
Authentication it IS required.
   

#### Authentication:
- Register: You can sign up by clicking on **Register** or going to http://127.0.0.1:8000/register/. Once you are registered you will be logged in.
  

- Login: You can log in by clicking on **Login** or going to http://127.0.0.1:8000/accounts/login/.


- Logout: You can log out by clicking on **Logout**.


#### Download artists names
You can download the artists table from the database that will be later used in Exercise 3.

You only need to go to (GET request): http://127.0.0.1:8000/download-artists/ and a csv would be downloaded to your local machine.

#### Upload artists images
You can upload the artists images that you will obtain in exercise 3.

You only need to go to (GET request): http://127.0.0.1:8000/upload/ and you´ll be able to select the image you want and tell the artist.

With this, the image will be uploaded to a new table of Django database and the artists with an image uploaded will have the image shown when you click on a specific artist.

### Exercise 2
#### Duplicate
1. Go to http://127.0.0.1:8000/passphrase/basic.


2. Write phrases (strings) and press ENTER to insert a new line. 


3. When you are done, click OK and the page will show the number of strings or passphrases that did not contain duplicated words.

#### Anagram
1. Go to http://127.0.0.1:8000/passphrase/advanced.


2. Write phrases (strings) and press ENTER to insert a new line. 


3. When you are done, click OK and the page will show the number of strings or passphrases that did not contain words that are anagrams of others.


# EXERCISE 3

## Requirements
- Python 3.8
- Scrapy 2.5.1 4.0
- Requests 2.27.1
- Pandas 1.4
- Pillow 9

## Installation
After you cloned the respository, you want to create a virtual environment, so you have a clean python installation. 
```
python -m venv env
```
Once you´ve created a virtual environment, you may activate it.
```
(On Windows): env\Scripts\activate.bat
(On Unix or MacOS): source env/bien/activate
```
You can install all the required dependencies by running
```
pip install -r requirements.txt
```
## Use
This is a Scrapy project. It needs to have a **artists.csv** file at the project´s root directory as it is the file downloaded from exercise 1 with the artists names.

The spider will use each name in that file to complete this url: https://www.allmusic.com/search/all/

That way, we can find the image of that artists in that web page. This web page does not have images for all the artists though.

To execute it, just run:
```
scrapy crawl image-search
```

This will download an image for each artist if there is one in the page selected. They will be stored in the folder **images**.

