September 14th, 2019 
* setting up environment
* creating skeleton web application

September 15th, 2019
* trouble shooting "flask_cors not recognized in pycharm"
* installing bootstrap
* setting up github & first commit to taen_dev then merge from command line


With a brand new computer (Windows Surface Laptop, replaced), I started to set up the environment for a web application that uses Python-flask and VueJs. I decided to use these frameworks, because I worked with them in my summer internship position.

That being said, I was provided with Mac at my internship, and I have never set up a web application from scratch, so this experience was new for me. During the process, I encountered many problems and obstacles, which I solved mainly by researching the problems online.

The process of setting up the environment helped me to gain knowledge and understanding of the basis of web application, but also taught me probem solving skills. I found that by actually researching and solving these problems myself, I was able to learn and understand substantially.

NOTE: This is going to be a long, unedited file, and is only for documenting/reflecting purposes.

## Setting up environment

Software used for this project:
* Windows Command Prompt -> I am more familiar with Linux, but Ubundo seemed complicated
* Pycharm -> for actually coding the web application, allow for readable codes
* Github -> it's only me, but it's a very good opportunity to learn git commands!
* Google Chrome -> I mainly use this to run the localhost and check developer's tool.
I am going to skip the process of software installation. I think it is pretty straight forward.

### Installing python (pip) and NodeJs (npm)
From the official websites, install and run each packages.
Install pip by downloading pip.py file and running it.

Problem:
* command prompt did not recognize python or npm commands

Cause:
* command prompt could not identify the paths to the installed packages.

Solution:
* From advanced system setting, add paths of the packages (python and nodeJs) to the environmental path.

Testing:
* in command line, python --version, node --version, npm --version

Outcome:
* understood what is meant by 'path not found', and how to resolve this problem.

### Installing flask and vue and connecting the server to client
On client side, install vueJs, which creates a package-lock json that lists all package dependencies. 
Install vue by npm install. There are some default files created in the client directory.

Install Vue-router and add router.js file. The initial problem with this was a new package-lock file was created in other directory, and I had to merge between the two. 

On server side, create an environment folder, using virtualenv. Install flask and flask-cors using pip. 
The problem I had here is again Pycharm not recognizing flask and flask-cors. This was because of:

1. pip installed flask and flask-cors (CORS needed for server responses) outside of the project directory.
2. source root was not identified.

Resolving the above problems allowed flask and vue to send requests via axios. 

Outcome:
* understood the paths within Pycharm, identifying source roots and template folders for Pycharm to refer to.
* understanding CORS

### Installing bootstrap
Pretty straight forward - installed Bootstrap from official website, and included import statement in main js.

### Installing Git and commiting from command prompt
Installed Git for windows. Pulled from remote repository, commited, pushed, and merged.

Mistakes made:
* tried pushing before pulling, resulting in error
* did not checkout to my development repository, and commited to master branch directly

Git Rules for myself
* Always commit in taen_dev
* Then merge to master
* If working on side project create a new branch or stash (less preferred?)


## Takeaway
* Know the commands on command prompt (searching up is acceptable, in my opinion)
* Always think about the pathes of packages; are applications given the paths? DO NOT TAKE FOR GRANTED
* For client-side packages, look at package-json, for server-side packages, look at venv site-packages
* Stay organized, commit and push to development branch first

I have learned a lot setting up the environment of this application. I have to admit, it took quite some time. 
I have experience working with flask-vue application, but when I started my internship, all the environment was set up for me. 
The only set-ups I had to do were installing software, obtaining ssh files from AWS server, cloning projects, and setting up database, which I did following a Wiki document that the company had made.

It was a worthwhile process! Frustrating at times, but pretty fun. 


NOTE * I still need to set up my database!! I will need to do research on free database... and sqlalchemy probably. 


## Primary Sources
https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
https://kittagon.hateblo.jp/entry/2018/08/27/011354
https://flaviocopes.com/vue-router/
https://wpism.com/publish-local-project-github-command-line/

and others such as stackoverflow, official websites, etc.