# Nyametizator 6000

# 📺Live Demo
## 🔗Link : [Small Heart💖](https://small-heart-demo.herokuapp.com/)


## ???

### Why?
This is just something I promised myself would do back in the day when I was learning python, now that I got a good flask template from an open source project I found, decided to make it reality

### What is this?

The original format/objective has changed since I couldn't find the code I made 8 months ago T.T.
I remmeber it was something about a normal string trasnformed into something a drunk person would say, please send a DM if you know it!!!

#### How to use Virtual enviroment?

**Add changes to the virtual enviroment**

$ pip freeze > requirements.txt

#### How to use heroku?

**don't use .gitignore I guess**

- $ touch Procfile
  - inside the new file write: web: gunicorn app:app
- $ heroku login 
- $ heroku create

**Push our code to heroku**
- $ git push heroku main|master

**Change the name of the page! o:**
- $ heroku rename