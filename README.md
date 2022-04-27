
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
  `Product` is the core model for the site, which has relationships with the following __supporting models__: `Type` (type of product), `Size`, `Color` and `Category`. All supporting models are optional, and can be left blank when creating a product for greater flexibility and to allow scaling product range.

  ### Order and OrderLineItem:
  `Order` stores information about an order placed by the users, and delivery address, to allow orders to be completed by shoppers who are not registered.
  `OrderLineItem` model stores information about the purchased product and its details - quantity, size and color. OrderLineItem also features a method for creating an SKU at time of the order for stock monitoring purposes.

  ### UserProfile: 
  `UserProfile` model stores information about the user, their default delivery address as well as their order history. 
  <!-- Based on their previous purchases, the site also provides suggestions of other products of same type/category to promote future purcahses. -->

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

  Landing page contains a blurb with information about the company, setting out vision and values. The top banner contains links to the social media, profile login, and information about the minimum order value to receive free delivery, while the main menu contains links to products search bar and shopping bag. The page itslef is aimed at visually attracting the user to enter the shop and explore the offer.
  <!-- Show shopping bag only when on products, not on main landing page? --> 

Admin user's home page<br>
<!--<img src="" width="500"> -->

  ### <a name="#navigation"></a>__Navigation__

  The header is composed of two bars, the top bar shows the links to the social media and a button taking the user to login or userprofile if they are already logged in. The main navigation bar takes care of the navigaton through products and offers links to products already sorted by different groups and categorisations. See image showing this below.
  The shopping bag icon in the navigation bar includes indiation of the number of items in the shopping bag as well as the total for the items added to the bag to allow the user monitor their spend.

  Top bar navigation:
  <!--<img src="" width="500"> -->

  Product navigation:
  <!--<img src="" width="500"> -->

  Shopping bag:
  <!--<img src="" width="500"> -->

  ### <a name="#browsing"></a>__Browsing products__

  The products page, showing all products, can be accessed by clicking _Shop Now_ button on the landing page, the logo on any page, or _All Products_ in the menu bar. 
  The products are shown as cards featuring image with the product if one is available or a default image if no image has been provided, list of avilable sizes and colors, if this is applicable for that product<!--, as well as Buy Now button allowing the user to add the item to their shopping bag directly from that page-->.

  On the left-nad side of the page, the user sees the information about the number of products showing, and what filters have been applied if that is the case. On the right-hand side they can access various filtering and sorting options. 

  #### __*Searching*__

  The user can search products by keywords that can appear either in the product names or their directly from the search bar at the top of the page. The product titles and descriptions are composed with searchability in mind.

  <!--<img src="" width="500"> -->

  #### __*Filtering and sorting*__

  When the user clicks on _Fitler / Sort_ on the main products page, a pop up comes up, where they can fitlter products by size, color and category as well as sort alphabetically and by price.

  <!--<img src="" width="500"> -->

  ### <a name="#product-details-selection"></a>__Product details and selection__

  Clicking on the product card takes the user to the product details page, where they view the product in more detail, read the product description, select the color and size they wish to purchase and add the item to the bag.

  <!-- When clicked, the image opens in a separate browser tab, so that the user can have a closer look at the product. -->

  ### <a name="#purchase"></a>__Making a purchase__

  In order to make a purchase the user needs to first select size and/or color if these are ooptions for the product they wish to purchase. Once these are selected, they can add the product to the bag. On adding the product to the bag, the user sees a pop up confirming that the item has been added to their shopping bag, and they can either close it and continue shopping or click on the button which directs them to the shopping cart.

  ### <a name="#products-management"></a>__Products management__

  #### __*Adding new product*__


## <a name="left-to-implement"></a>Features Left to Implement


# <a name="django-admin"></a>Management via Django admin site

The product

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