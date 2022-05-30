# TABLE OF CONTENTS
1. [Introduction](#intro)
2. [UX](#ux)<br>
  2.1 [User Stories](#user-stories)
3. [Features and design](#features-design)<br>
  3.1. [Models and functional design](#models-and-flow)<br>
  3.2. [Existing features](#existing-features)<br>
    3.2.1. [Sign up and Login](#sign-up)<br>
    3.2.2. [Landing page](#landing-page)<br>
    3.2.3. [Navigation](#navigation)<br>
    3.2.4. [Footer](#footer)<br>
    3.2.5. [Browsing products](#browsing)<br>
    3.2.6. [Product details and selection](#product-details-selection)<br>
    3.2.7. [Making a pruchase](#purchase)<br>
    3.2.8. [Product reviews](#rating)<br>
    3.2.9. [Products management](#products-management)<br>
    3.2.10. [Custom error pages](#error-pages)<br>
  3.3. [Features left to implement](#left-to-implement)<br>
4. [Management via Django admin](#django-admin)<br>
5. [Marketing strategy](#marketing-strategy)<br>
6. [Technologies](#technologies)<br>
  6.1. [Languages used](#languages)<br>
  6.2. [Frameworks, libraries and programs used](#libraries-and-programs)<br>
7. [Testing](#errors-testing)<br>
8. [Deployment](#deployment)<br>
9. [Credits](#credits)<br><br>

# <a name="intro"></a>Green Bean e-shop

Green Bean is a __slow fashion__ brand where a responsible attitude to the environment meets great design. Green Bean products are made with sustainability in mind using high-quality, recycled and responsibly sourced materials and designs that are truly unique. The brand targets young adults and adults located in the UK to avoid international shipping, who are interested in the environment, slow fashion and ecology.
The brand's page and e-commerce store is available here: https://green-bean-shop.herokuapp.com/

# <a name="ux"></a>UX

The design of the site aims to follow best User Experience practices, focusing on easy browsing and a pleasant shopping experience. Considering the website is an e-commerce one, it is important it is visually appealing and that functionality and aesthetics are balanced correctly. The planning of the site involved creating [wireframes](https://github.com/Koko-66/green_bean_shop/blob/main/static/assets/data/GreenBean_wireframes.pdf) to visualise the final look of the site.

The Colour scheme is kept simple with a mostly white or light background to emphasise products and their images while the typology reflects the artistic side of the brand.

## <a name="user-stories"></a>User Stories 

The e-shop was developed using Agile methodology, with User Stories managed within a Github Project. All completed and outstanding User Stories can be viewed [here](https://github.com/Koko-66/green_bean_shop/projects/1).

# <a name="features-design"></a>Features and Design

## <a name="models-and-flow"></a>Models and functional design

The website data about the user, products, orders and all other relevant data are stored in a Postgres relationship database. The database model comprises of the following main tables:

  ### Product:
  `Product` model stores all the main information about the product and relates to the following supporting models: `Type` (type of product), `Size`, `Color` and `Category`. `Type` is required for each product and is used for their top level categorisation as well as in the generated SKU. All other supporting models are optional and can be left blank. This way the site owner has greater flexibility when adding new products and allows to easily scale up the product range, i.e. add new products that do not have different sizes or colours. Each of these supporting models also includes a `slug` for use in references within the code to prevent errors.

  ### Rating: 
  The rating model stores users' ratings and reviews for individual products. The user can choose a product rating between Poor (1) and Excellent (5) and leave a comment to help other shoppers make their decision about the purchase. The model links to `User` and `Product` models and the ratings are displayed along with the product information on the site (average and individual ratings).

  Average rating on product pages
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/average-ratings.png" width="500">
 

  ### Order and OrderLineItem:
  `Order` model stores information about an order placed by the users and the delivery address provided for the order. This way a purchase can be completed by shoppers who do not wish to sign up for an account, which significantly decreases the chance of the shoppers abandoning the purchase at this final stage.
  `OrderLineItem` model on the other hand stores information about the purchased product and its details - ordered quantity, size, colour, and total price for that line item (product price x quantity). OrderLineItem also has a method that generates an SKU at the time of the order to be used to monitor stock levels and the demand for specific kinds of products.

  ### UserProfile: 
  `UserProfile` model stores information about the user and their default delivery address. The UserProfile gets created when the user registers to the website and the address is saved at the time of placing an order when the __Save information__ box is ticked. 

  The components of each model and the relationships between them are represented in a graphic model representation available [here](https://github.com/Koko-66/green-bean-shop).

## <a name="existing-features"></a>Existing Features

  ### <a name="#sign-up"></a>__Sign up and Log in__

  The website offers an option for the users to create an account where they can view their previous orders and review history. They can register by clicking the account icon in the top right corner of the page and selecting _Register_. They are also prompted to register at the checkout and if they indicate a wish to leave a review for a product.

  Clicking on _Register_ redirects the site user to a sign-up page. _Resgistration_, just as _Log in_ form, is delivered by __Allauth__ Django app. The forms are fully validated for correct data input, and the _Registration_ form asks to confirm the inserted password and email address for validation purposes.
  For security purposes, the registration process requires the provided e-mail to be verified by the user - on submission of the _Registration_ form, the user receives an email with a link to verify their e-mail address. 
  The site also allows users to reset their forgotten passwords. 

  Log in form<br>
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/login.png" width="500">

  Registration form<br>
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/signup.png" width="500">

  All users are managed via the backend Django admin site by _superadmin_. 

  ### <a name="#landing-page"></a>__Landing page__

  The landing page contains a blurb with information about the brand that sets out its purpose. The content was composed with the SEO in mind and features some of the keywords identified as valuable for the target audience. It also has a link to an outside source with information on slow fashion, which can be considered a source of authority.

  ### <a name="#navigation"></a>__Top banner and navigation__

  The header is composed of two bars, the top bar shows the links to the social media and a user profile button with links to the Registration / Login or User Profile if they are already logged in. The main navigation bar takes care of the navigation through products according to their type and high-level grouping. Three of the menu items, _T-shirts_, _Accessories_ and _Special Offers_ are dropdowns with links to further groupings. The navigation bar also features a search bar and a shopping bag and a link to _Manage Products_ functionality.
  The shopping bag has a badge showing the number of items that are currently in the shopping bag as well as the total price for all items added to the bag to allow the user to monitor how much they are about to spend.
  If the user is logged in, a bar showing their user name appears between the two elements described above.

  Navigation:
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/nav-bar-large.png" width="500">

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/nav-bar-large_with-dropdown.png" width="500">

  Navigation on smaller devices:
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/nav-bar-small.png" width="500">

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/nav-bar-small-with-dropdown.png" width="500">

  ### <a name="#footer"></a>__Footer__

  The page footer is visible on scrolling to the bottom of the page to allow the shoppers to focus on products and contains links to Privacy and Returns and Refund policies. 
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/footer.png" width="500">

  ### <a name="#browsing"></a>__Browsing products__

  The products page, showing all products, can be accessed by clicking _Shop Now_ button on the landing page or _All Products_ in the menu bar. 
  
  On the left-hand side on the top of the page, the user sees the information about the number of products showing at a given time as well as whether any filters or sorting has been applied. On the right-hand side, they can access various filtering and sorting options.

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/all-products-top-with-filter.png" width="500">

  The products are shown as cards featuring the image if one is available or a default image if no image has been provided, product name, price and rating, as well as a list of available sizes and colours if applicable. The user can also add the product to their shopping bag directly from this page, by selecting the colour and size (if applicable) and then clicking _Add to bag_ button.

   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/product-cards.png" width="500">

  #### __*Searching*__

  The user can search products by keywords that can appear either in the product names or their descriptions directly from the search bar at the top of the page. The product titles and descriptions are composed with searchability in mind to help users find what they are looking for more easily.

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/search-box.png" width="500">

  #### __*Filtering and sorting*__

  When the user clicks on _Fitler/Sort_ on the main products page, a pop up comes up, where they can filter products by size, colour and category as well as sort alphabetically and by price. Once the shopper is happy with their selection they can apply the filters or clear the filters.

 <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/filters-large.png" width="500"><br>
 <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/filters-small.png" width="500">

  ### <a name="#product-details-selection"></a>__Product details and selection__

  Clicking on the product card takes the user to the product details page, where they view the product in more detail, read the product description, select the colour and size they wish to purchase and its quantity and add the item to the bag.
  The shoppers can then select a different size or colour and add this new selection to the bag as well as a separate item.

 <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/shopping-bag-same-items.png" width="500">

  When clicked, the image opens in a separate browser tab, so that the user can have a closer look at the product.

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/product-details-small.png" width="500">

  The product page also contains suggestions of other products in the same categories that might be of interest to the user and has a list of previous reviews.

  ### <a name="#purchase"></a>__Making a purchase__

  In order to make a purchase, the user needs to first select size and/or colour if these are options for the product they wish to purchase. To prevent errors, an option for each of these is already preselected (first option for colour and "M" for the size) and the user only needs to select another one if needed. Once these are selected, they can add the product to the bag. On adding the product to the bag, the user sees a pop up confirming that the item has been added to their shopping bag, and they can either close it and continue shopping or click on the button which directs them to the shopping cart.

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/added-to-bag-notification.png" width="500">

  The shopping bag can be accessed from the popup, by clicking _Go to secure checkout_ or, if the pop-up was dismissed, by clicking the shopping bag icon. 

  The shopping bag contains information about the items currently appearing in the bag and allows the shopper to adjust the product quantity or remove items from the bag entirely. It also shows the user the price per product, the total for the order line, as well as the total order value and the delivery costs. If the order falls below the free delivery rate, the page will also show information about the amount the shopper will still need to spend to get free delivery.

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/shopping-bag-view.png" width="500"><br>
  
  The shopper also receives feedback on the change made to the order line, product that was changed and the updated status of the bag.<br>
  'Item removed' confirmation
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/remove-item-from-bag-success.png" width="500">
  <br>
  'Quantity updated' confirmation
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/update-quantity-in-bag-success.png" width="500">
  Clicking on the product image in the list takes the shopper back to the product details page.

  When the shopper is happy to move on, they click on _Secure checkout_ and are taken to a _Checkout_ page to complete their purchase. 
  If the shopper is logged in and have a saved address the address in the checkout form is populated with the saved data. They can update it by clicking on Save info button. If the shopper is not logged in, he/she is prompted to log in or register for an account to save their information.
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/checkout-top.png" width="500">
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/save-info-and-gdpr.png" width="500">
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/create-login-prompt-in-checkout.png" width="500">

  The checkout also contains links to the Privacy and Return and Refunds policies and a consent box to receive the brand's newsletter. 

  Once an order is complete the user is redirected to a page with order confirmation details.

   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/order-complete.png" width="500">

  ### <a name="#rating"></a>__Product reviews__

  The website at present has a basic framework for product review, allowing the registered user to leave a review for any product. The review comprises of a star rating (from 1/Poor to 5/Excellent and comment, and is saved against the product as well as the user account. 

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/add-product-review.png" width="500"><br>

  At present, the user can access a review page from the product detail view. In the next feature update, the reviews will be restricted to products the shoppers purchased and they will receive an email with a request to leave a review. The reviews will also be monitored and will need to be approved by the site moderator before being published on the site.

  The average product rview is shown as part of product details while individual reviews for each product appear at the bottom of the _Product details_ page. By detault only 3 first reviews are shown and the rest can be expanded by clicking _Show more..._ button.

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/..." width="500"><br>

  
  ### <a name="#user-profile"></a>__User profile__

  Every registered user has a user profile, which can be accessed from the top banner menu, by clicking on the user account icon.<br>

  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/profile-menu.png" width="500"><br>

  The profile page comprises of of 3 sections:  
  1. The __Default delivery address__ section features a button with a link to update profile page<br>
    <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/profile-address-section.png" width="500"><br>
    Update address<br>
    <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/profile-update-address.png" width="500"><br>

  2. __Your orders__ section listing the user's order history shows the last 5 orders and the rest can be viewed by clicking the _View Older_ button.<br>
  
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/profile-order-section.png" width="500"><br>
  
  3. __Your review hisory__ section shows only 5 latest ratings, since access to these is not crucial to the user.<br>
  <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/profile-ratings-section.png" width="500"><br>


  ### <a name="#products-management"></a>__Products management__

  Products can be managed from the Django admin site as well as from the front end. If the user is logged in with superuser rights, an extra button _Manage products_ is available. The button takes the admin user to a page where they can edit, delete and add new products, product types categories, colours and sizes.

  Main view<br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/manage-products.png" width="500"><br>
  Expanded view<br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/manage-products-2.png" width="500"><br>

  Editing and adding new products are managed on a separate page while editing and adding types, categories, colours and sizes in modals, which is easier and quicker considering the number of fields for these models. These elements can also be added directly from Add new product page, which makes it easier for the shop owner to manage their product database. 
  One feature worth mentioning here is the presence of an image thumbnail in the Edit product form providing reference to the user of what they are editing.

  Next to the elements that can have more than one element selected (which can be done using Shift or Ctrl/Cmd and click) the user also has access to _Clear all_ button that clears all the selected product types, colours, categories and sizes. This button is also available in the _Edit product_ template.

  Add new product<br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/add-product.png" width="500"><br>
   Edit category - modal view<br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/edit-category-modal.png" width="500"><br>
   Add new category and clear all buttons within product add view.
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/add-product-with-add-category.png" width="500"><br>

  Products and all other models can be also of course managed via django admin site. For brevity, this will not be discussed in detail here. 

  ### <a name="#error-pages"></a>__Custom error pages__

  The site has custom 404 and 500 error pages with a button leading back to the Products page in case something goes wrong.
  404 page <br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/custom_404_page.png" width="500"><br>
  500 page <br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/custom_500_page.png" width="500"><br>

## <a name="left-to-implement"></a>Features Left to Implement

An e-commerce website is a complex application that requires constant development according to the users' needs. As such, there is still a lot of scope for improvement and additional features, some of which include: 

1. Allowing the users to filter products by more than just one colour, size or category.
2. Build on reviews functionality: 
  - restrict the users to comment only on the products they've purchased and add a possibility to add additional comments to a given review or update it.
  - add some sort of vetting process for reviews before they appear on the site
3. Add a pre-publish status on products after they are added, to allow for product posting QC.
4. Appropriate management for special offers and discounts and their presentation on the product pages. Discounts would be set up as a separate model and added to the product model as a foreign key. 
5. Add handling of registration for a newsletter on the Checkout page.
6. Change layout of policies to home branding.

# <a name="marketing-strategy"></a>Marketing strategy

Considering the type of business Green Bean is as well as its target audience, the marketing strategy focuses on SEO, social media marketing and email marketing. Implementation of these three elements will help the brand grow organically and build a community and a loyal client base.

## Search Engine Optimisation

Keyword research was carried out following the process below: 
1. Jotted down a list of topics related to the site: t-shirts, slow fashion, design and sustainability
2. Brainstormed to obtain a list of long and short-tail keywords related to the topics above. This exercise resulted in the following list: <br>
t-shirts, quality t-shirts, clothing, jewellery, design t-shirts, unique t-shirts, unique jewellery and accessories, slow fashion, sustainable fashion, recycled clothing, great t-shirts, cool t-shirts, buy sustainable clothing, t-shirts for a gift, custom t-shirts, unique t-shirts uk
3. Researched the list created in point 2 using Google Search to expand/refine it. This resulted in the addition of a couple of new terms and the following list: <br>
good quality t-shirts, high quality t-shirts, quality t-shirts, design t-shirts, unique jewellery and accessories, slow fashion, sustainable fashion, recycled clothing, unique graphic t-shirts, buy sustainable products, unique t-shirts uk, buy recycled t-shirts online, buy recycled clothes online, best ethical t-shirts uk<br>
4. Assessed whether the selected keywords are relevant and have authority using wordtracker.com, which resulted in the final list composed of: <br>
good quality t-shirts, high quality t-shirts, unique design t-shirts, unique graphic t-shirts, unique design jewellery and accessories, slow fashion, sustainable fashion, recycled clothing, cool sustainable t-shirts, buy sustainable clothing, sustainable clothing uk, ethical clothing, ethical fashion, eco-friendly clothing, sustainable brand,  buy sustainable products, buy eco-friendly t-shirts online, buy recycled clothes

### Implementation of SEO in HTML

Considering the type and purpose of the site the implementation of SEO focuses on the meta tag, where all the above keywords have been placed, the text on the landing page, the product descriptions which are construed keeping in mind the results of the keyword search and the use of html elements to make them more prominent to the search engines, and product images and their alt-elements, which are mostly automatically generated and match the product name. Keywords are also used in aria elements whenever possible. 
The links to the external sites (Good on You, social media sites) have been set as `noopeners` prioritising the site's security over SEO.

The site also includes sitemap.html and robot.txt files. 

## Social Media

Social media strategy sets out to create and manage social accounts on Instagram and Facebook, where the shoppers can engage with the brand, post reviews and share interesting information about 'Slow fashion.' 
The Facebook page has been set up for the brand where news will be posted regularly to keep the audience engage and informed about the brand's activities. There is a plan to run discussion groups around the topics of _slow fashion_, _environement_ and _sustainability_.

   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/facebook-page.png" width="500"><br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/facebook-page2.png" width="500"><br>
   <img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/facebook-page-post.png" width="500"><br>

## E-mail marketing 

Newsletters with the news on the brand's activities in the area of 'slow fashion' and its involvement with various organisations operating in the area of sustainability, as well as news about the new products launched are also an important part of marketing for the site. The newsletters and subscription lists are managed in Mailchimp via forms embedded in the site allowing users to easily register their interest in receiving the newsletter, irrespective of whether they have a Green Bean account. 
The subscriptions are managed in two ways. Firstly, after 5 seconds from entering the site, a _Subscribe to our newsletter appears_. <br>

<img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/mailchimp-signup_pop-up.png" width="500"><br>

Secondly, as a backup since once dismiss the pop up will not appear again until the browser data is cleared, the site also features an embeded sign up form which can be accessed by clicking a 'SUBSCRIBE' button placed on every page of the site.<br>
<img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/subscribe-button.png" width="500"><br>
<img src="https://github.com/Koko-66/green_bean_shop/blob/main/media/assets/data/mailchimp-signup.png" width="500"><br>

Another place where the shopper can register for the newsletter is the Checkout page, however, this feature is still under development.

## GDPR considerations

Green Bean abides by the GDPR and has a Privacy Policy that states the purposes for which the user's data will be used. The link to the Policy is placed in the footer of the page as well as 

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
- __[widget_tweaks](https://pypi.org/project/django-widget-tweaks/)__ and __[crispy froms](https://django-crispy-forms.readthedocs.io/en/latest/)__:  used to format forms
- __[django-bootstrap-modal-forms](https://pypi.org/project/django-bootstrap-modal-forms/)__: used to manage deletions, additions and edits to product and its supporting models
- __[Heroku](https://www.heroku.com/)__: used to deploy the live version of the project
- __Beautify__: VSCode extension to format code

# <a name="errors-testing"></a>Error handling and testing

The error handling is currently mostly handled by the inbuilt functionality of class-based views as well as some if-statement based checks within these. Going forward, the application will be using a more robust approach using a set of custom error classes.

Information about the application testing is available in a separate file [here](https://github.com/Koko-66/green-bean-shop/blob/main/TESTING.md).

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
 - selected GitHub as the deployment method,
 - selected Connect,
 - authorised Heroku to access the GitHub account,
 - searched for 'green-bean-shop' repository and confirmed the connection.
6. First time deployed the app using the manual Deploy Branch button, then enabled automatic deploys.
7. After the first deployment, added variables for email and set debug setting to FALSE in the deployed environment.
 
# Requirements
The website was built using Python3.8. All other requirements are contained in the requirements.txt file.

# <a name="credits"></a>Credits

The application was built following the Code Institute's Boutique Ado walkthrough project - thank you to CI for providing the basis! 

In addition, a great thank you to: 
- My mentor, Caleb Mbakwe, for invaluable advice on the best approach to the project, organisation of code, and support throughout and CI tutors.
- Stackoverflow community and those behind running it for making it possible to solve almost any problem.
- Creators of Django and Heroku documentation as well as authors of all the plugins and libraries used in this application.
- Artists posting their pictures on [Pexels](pexels.com) for the great pictures!
- Phillip for help with the images and sharing some of his designs.
