
<!-- ![](my logo?)  -->
# TABLE OF CONTENTS
1. [Introduction](#intro)
2. [UX](#ux)<br>
  2.1 [User Stories](#user-stories)
3. [Features and design](#features-design)<br>
  3.1. [Models and functional design](#models-and-flow)
  3.2. [Existing features](#existing-features)<br>
    3.2.1. [Sign up and Login](#sign-up)<br>
    3.2.2. [Landing page](#landing-page)<br>
    3.2.3. [Navigation](#navigation)<br>
    3.2.4. [Browsing products](#browsing)<br>
    3.2.5. [Product details and selection](#product-details-selection)<br>
    3.2.6. [Making a pruchase](#purchase)<br>
    3.2.7. [Products management](#products-management)<br>
    <!-- 3.2.8. [](#)<br> -->
  3.3. [Features left to implement](#left-to-implement)<br>
4. [Management via Django admin](#django-admin)
5. [Technologies](#technologies)<br>
  5.1. [Languages used](#languages)<br>
  5.2. [Frameworks, libraries and programs used](#libraries-and-programs)
6. [Testing](#errors-testing)
7. [Deployment](#deployment)
8. [Credits](#credits)


# <a name="intro"></a>Green Bean e-shop

Green Bean is an e-commerce store where responsible attitude to the environment meets great design. All our products are made using recycled and responsibly sourced materials with sustainability in mind. Our designs are truely unique and varied, to suit every taste.
The site has been deployed to https://gren-bean-shop.herokuapp.com/

# <a name="ux"></a>UX

The design of the site aims to follow best User Experience practices, focusing on easy browsing and pleasant shopping experience. Condsidering the website is an e-commerce one, it is important it is visually appealing and that functionality and aesthetics is balanced correctly. 

## <a name="user-stories"></a>User Stories 

The application was developed using Agile methodology, with User Stories managed within a Github Project. All completed and outstanding User Stories can be viewed [here](https://github.com/Koko-66/green_bean_shop/projects/1).


# <a name="features-design"></a>Features and Design

## <a name="models-and-flow"></a>Models and functional design

The database underlying the website is a Postgres relationship database, where the product, user and all other relevant data are stored. 
The database model comprises of the following main tables:

  ### Product:
  `Product` is the core model for the site, which has relationships with the following supporting models: `Type` (type of product), `Size`, `Color` and `Category`.

  ### Order and OrderLineItem:
  `Order` stores information about an order placed by the users, and delivery address, to allow orders to be completed by shoppers who are not registered.
  `OrderLineItem` model stores information about the purchased product and its details - quantity, size and color.

  ### UserProfile: 
  `UserProfile` model stores information about the user, their default delivery address, linking with their order history.

  The components of each model and the relationships between them are represented in a graphic model representation available [here](https://github.com/Koko-66/green-bean-shop).

## <a name="existing-features"></a>Existing Features

  ### <a name="#sign-up"></a>__Sign up and Log in__

  When first accessing the application, the user is directed to a _Log in_ page. The page includes a link to a _Registration_ form, should the visitor not yet have an account. _Resgistration_ and _Log in_ forms are delivered by __Allauth__ Django app. The forms are fully validated for correct data input, and the _Registration_ form asks to confirm the inserted password and email address for validation purposes.
  For security purposes, the registration prococess requires the provided e-mail to be verified by the user - on submission of the _Registration_ form, the user receives and email with a link to verify their e-mail address. 
  The site also allows the users to reset their their forgotten passwords. 

  Log in form<br>
  <img src="" width="500">

  Registration form<br>
  <img src="" width="500">

  All users are managed via backend Django admin site by _superadmin_. 

  ### <a name="#landing-page"></a>__Landing page__

<!-- After logging in, a standard User is redirected to their homepage, where they can see a list of quizzes that have been published (i.e. set to `Approved`. If the quiz has been completed it is marked as such, and the button for taking the quiz is replaced with __Results__ that take the user to a page showing their results for that particular quiz.

Standard user's home page<br>
<img src='https://github.com/Koko-66/teaze/blob/main/static/data/Standard_user_home_page.png' width="500">

Admin users, on the other hand, are redirected to a dashboard with an overview of quizzes, questions and categories existing in the application. From here, via an extended menu, they can manage (create, edit and delete) all of these elements.

Admin user's home page<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Admin_user_home_page.png" width="500"> -->

  ### <a name="#navigation"></a>__Navigation__


  ### <a name="#browsing"></a>__Browsing products__

  #### __*Searching*__

  #### __*Filtering and sorting*__


  ### <a name="#product-details-selection"></a>__Product details and selection__

  #### __**__


  ### <a name="#purchase"></a>__Making a purchase__


  ### <a name="#products-management"></a>__Products management__

  #### __*Adding new product*__


## <a name="left-to-implement"></a>Features Left to Implement


# <a name="django-admin"></a>Management via Django admin site


# <a name="technologies"></a>Technologies used

## <a name="languages"></a>Languages

Programming languages used in the project: 

- HTML and CSS3
- Python
- JavaScript and JQuery

## <a name="libraries-and-programs"></a>Frameworks, Libraries, Plugins and other services used

- __Django__: main application framework
- __Bootstrap__: CSS styling
- __GitPod__: primary code editor
- __Git__:  for version control
- __[Git Hub](https://github.com/)__: to store project files
- __[Python Tutor](https://pythontutor.com/)__: used to help with debugging
- __darw.io__: to create the data model and program logic flow chart
- __Balsamiq__: for wireframes
- __Cloudinary__: to store image files uploaded by the user
- __PostgreSQL Database__: serving as main database
- __Coverage__: create reporting on level of tests
- __[AllAuth](https://django-allauth.readthedocs.io/en/latest/)__: user management
- __[widget_tweaks](https://pypi.org/project/django-widget-tweaks/)__:  used to format forms
<!-- - __[django-filter](https://django-filter.readthedocs.io/en/stable/)__: used on the Manage questions page to filter the content -->
- __[Heroku](https://www.heroku.com/)__: used to deploy the live version of the project
<!-- - __[whitenoise](http://whitenoise.evans.io/en/stable/django.html)__: to serve static files correctly in production -->
- __Beautify__: VSCode extension to format code
- 


# <a name="errors-testing"></a>Error handling and testing

The error handling is currently mostly handled by the inbuilt functionality of class-based views as well as some if-statement based checks within these. Going forward, the application will be using a more robust approach using a set of custom error classes.

Information about the application testing is available in a separate file [here](https://github.com/Koko-66/teaze/blob/main/TESTING.md).


# <a name="deployment"></a>Deployment
The program was deployed to Heroku at the start of the project to ensure its correct functioning and is accessible here: 

The steps taken to deploy the app: 

1. Updated the contents of the requirements file using the `pip3 freeze > requirements.txt` command in VS Code.
2. Checked the project structure and run the program to ensure everything is working as expected.
3. Created the Green Bean project on Heroku, giving it the name 'green-bean-shop'.
4. Added a new Postgres database:
  - In the Resources tab, searched for Heroku Postgres add-in and selected the free Hobby Dev option.
5. In the Config Vars section of the Settings tab, added the environment variables to set up: 
  - Link to Postgres database 
  - Link to Cloudinary
  - Disabled static files for the time of development
  - App secret key
5. In the Deployment tab:
 - selected GitHub as deployment method,
 - selected Connect,
 - authorised Heroku to access the GitHub account,
 - searched for 'green-bean-shop' repository and confirmed the connection.
6. First time deployed the app using the manual Deploy Branch button, then enabled automatic deploys.
7. After the first deployment, added variables for email and set debug setting to FALSE in the deployed environment.
 
# Requirements
Application was build using Python3.8. All other requirements are contained in the requirements.txt file.

# <a name="credits"></a>Credits

The application was built basing on the Code Institute's Boutique Ado walkthrough project - thank you to CI for providing the basis! 

In addition, a great thank you to: 
- My mentor, Caleb Mbakwe, for invaluable advice on the best approach to the project, organisation of code, and support throughout.
- As always, Stackoverflow community and those behind running it.
- Creators of Django and Heroku documentation as well as authors of all the plugins and libraries used in this application.