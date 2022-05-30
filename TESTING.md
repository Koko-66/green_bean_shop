# TESTING
The website was tested at each step of the development within the development environment as well as on Heroku after the deployment. The testing plan included elements explained below.

1. [User Stories and functionality testing](#user-stories-testing)
. [Validator testing](#validator-testing)
2. [Programmatic testing](#programmatic-testing)
4. [Development testing](#bugs-and-fixes)

[BACK to README](https://github.com/Koko-66/green_bean_shop/blob/main/README.md)

## <a name="user-stories-testing"></a>User stories and functionality testing
Functionality was tested at each stage of development and as each of the stories in the Git Project was completed. 
The testing entailed going through each feature of the app and ensuring that the application runs as expected and yields expected results, without causing any errors. In addition, main user stories were also tested at the very end of the project to ensure correct functioning after the final deployment.  

User story testing
### Home and account management 
- _As a shopper/site user I can read about the products and the company so that I know what products the site offers._
The site's landing page includes the brand's mission statement outlining what the brand does and what they stand for.
- _As a site user I can easily register for an account so that I can access my profile page_ 
- _As a site user I can easily log in and out of the site so that I can access my account and prevent access to it by others_: 
the user has easy access to sign up and login forms accessible from the navbar. The process is straightforward. 
- _As a shopper/site user I can view my profile so that I can view and amend my saved details._
- _As a shopper/site user I can view my profile so that I can view my order history._ 
In their profile, the user can view their full order history as well as 5 most product reviews.
_As a user/shopper I can see my logged-in status._ 
Once the user logs in a new banner with the information 'Logged in as USERNAME' appears in the navbar.
### Browsing products
_As a shopper I can view a list of products so that I can find what I want to buy._
_As a shopper I can view product details so that I can check the price, description, colour and size options._
The products are listed on the products page in the form of cards featuring the product image, name, price colour and size options if these are available. Upon clicking the card image, the users are taken to the product details page with a bigger image and more information about the product. 
- _As a shopper, I can search for products and filter them by category so that I can easily find what I am looking for._
- _As a shopper I can sort and filter products using more than one criterion so that I can find what I am looking for quicker._
The site provides a search bar, filtering and sorting functionality to help users navigate through the available products. 
- _As a shop owner I can suggest other relevant products to the users so that they purchase more products and remain engaged with the site._
- _As a shopper I receive suggestions of other products that might be of interest to me so that I find what I might need easier._
Below the product details on the _Product details_ page there is a list of products labelled with the same category presented as suggestions of other products the shopper might like.
- _As a site user/shopper I can see a custom 404 and 500 pages so that I have a uniform user experience and have greater trust in the quality of the site._
The site features custom 404 and 500 pages with a button taking the users back to the main shopping page in case an error occurs or the user tries to access a page that doesn't exist.

### Purchasing process 
_As a shopper, I can easily add products to the shopping cart so that I can make the purchase when I am ready._
_As a shopper I can add the product to my shopping bag directly from the page with a list of products so that I save time and don't need to go via the product details page if I don't wish to_
The user can add the product to the bag directly from the _All products_ page or _Product details_ page, whichever is more convenient.
_As a shopper, I can easily view and adjust what is in my cart so that I can make sure my selection is correct._
The user can access the shopping bag at any point of their journey by clicking its icon in the navbar. The shopping bag page allows the users to adjust the number of items in their bag and remove them if needed.
_As a shopper, I can see the total for items I added to the shopping cart at all times so that I can track how much I will spend._
As soon as the product is added to the shopping bag the number of items and the total amount in the shopping bag area in the navigation is updated.
_As a site user/admin I can see pop-up messages with feedback so that I know whether the action I completed was successful or not._
The code implements messages to the users confirming the successful completion of various actions which are then displayed in toasts with varying colours noting their seriousness.
_As a shopper, I can access checkout and make a payment so that I can complete my purchase._
The user can access secure checkout from the shopping bag where they can complete the purchase.
_As a shopper, I receive confirmation of my order so that I can be sure that my purchase was successful._
Upon the completion of the purchase, the application triggers an email confirmation that is sent to the email address provided at the checkout.
_As a shopper/site user I can view the company's Privacy Policy and have a GDPR opt-in option so that I understand how my data will be used._
_As a shopper I can read the store's refund and returns policy so that I have a clear understanding of what they are._
Green Bean's Privacy policy for compliance with GDPR as well as the Return and refund policy are both available in the site footer.

### Product rating/review
_As a user, I can rate a product and/or leave a review so that I can share my opinion with others._
_As a shopper, I can view and read other shoppers' opinions so that I can make an informed decision about my purchase._
_As a shop admin, I can restrict users to one review so that I keep the rating system accurate and valid._
The site allows the users to leave a review for each product (a star rating and/or a comment). Average ratings are then counted for each product and displayed along with other information in the product listings. In addition, the _Product details_ page includes a section with the reviews left by the users. If the user rated the product once, the application checks for existing reviews and replaces the link to the product review page with information that the product has been already reviewed by this user.

### Keeping in touch - newsletters and socials
_As a site user/shopper I can easily access the company's social media from the website so that I see the company's reviews and events._
Links to social media are visible at all times at the very top of the page.
_As a site user/shopper I can sign up for the company's newsletter so that I receive information about the company and the newest offers._
_As a shopper, I can access the newsletter signup form from any page so that I can sign up for the newsletter at any time._
A _Sign up to the newsletter_ popup appears 5 seconds after entering the site. Once dismissed it does not appear again until all session cookies are removed therefore the site also features an embedded form that is available upon clicking the 'SUBMIT' button available towards the bottom of all pages.

### Shop management and admin
_As an admin I can add, update and delete products so that the offer is always up to date and remains interesting._
_As an admin user, I can add product type, size, colour and category in frontend so that I can easily add new products and view them._
The site admin user can manage products, product types, categories, colours and sizes directly from the site as well as via the Django admin site. 
_As a shop owner, I want my site to appear in the top search results so that I can reach as many shoppers as possible._
The site follows an SEO and marketing plan as described in the [README](https://github.com/Koko-66/green_bean_shop/blob/main/README.md) file

## <a name="bugs-and-fixes"></a>Development Testing - Bugs and Fixes
Each feature was tested while being developed and before the final deployment to ensure correct and error-free functionality. The bugs encountered were resolved by using a combination of error message analysis, print statements, and research for possible causes and solutions.
The tests carried out and their results are listed below.

### TEST 1
<u>_Serving static files and visual aspects_</u><br>
The testing on serving static files was done at the start of the project to avoid issues at later stages, which seems to be a common issue. The test involved adding a coloured background to the base.css file and an image from Cloudinary to the index page and changing the DEBUG setting to `False` for the time of testing.<br>

***Result***<br>
Static files and an image served on Heroku as expected, with orange background and the image visible in the corner of the page.

### TEST 2
<u>_Testing models in the admin_</u><br>
All models were tested in the admin to ensure everything works as expected before moving on with the development.

***Result***<br>
No issues found.

### TEST 3 
<u>_Testing browsing products_</u><br>
The search bar and Filter/Sorting functionality were tested empirically. All issues were resolved at the time of development apart from sorting by rating which requires a special approach and was for now removed from the site due to time constraints.

***Result***<br>
No issues were found at the time of final testing.

### TEST 4 
<u>_Testing adding sizes to bag_</u><br>
Testing of the walkthrough method for adding sizes to the bag revealed an issue in updating the product list in the bag. If the same product already existed in the bag and another was added, it would replace the previously listed product, rather than update its amount, or create a new listing with a different size.

***Fix and Result***<br>
Testing showed the issue to be the type of the `item_id` (`int`). Conversion of the `item_id` to a string and using this value in the function instead, solved the issue.

### TEST 5
<u>_Testing adjusting and removing items from bag_</u><br>
Testing this functionality revealed an issue whereby sometimes all sizes and colours for the same items get deleted all at once rather than only a particular variant of a product.<br>

***Fix and Result***<br>
Considering the chaining of sizes and then colours, the view function needed an additional step to first delete the size if no colour already exists for that size in the dictionary, rather than deleting the whole item right away.<br>
In the adjust view, the part of the function handling the deletion of an item that has a size and a colour needed to be adjusted as well so that first the selected colour is deleted, and then checks for any other colour performed.

### TEST 6 
<u>_Test purchase proces_</u><br>
The shopper can view product details by clicking o the product card in the main product view. The product detail page contains the product name, price, description, lists of available colours and sizes, and a list of categories and ratings, if available.

The testing of purchasing process revealed a couple of issues:<br>
1. Statements calculcating `grand_total` and `free_delivery_delta` throws an error, caused by the difference in data types between `total` (decimal) and `free_delivery_threshhold` (float).<br>
    ***Fix and Result***<br>
    Converted `total` to float in the statements performing the calculations.
2. The toast showing the success message still contains information about the costs, because the grand_total still contains the value of delivery costs.
    <br>
    ***Fix and Result***<br>
    Added an if statement to the context view determining the delivery costs to set grand_total to Null if total is equal to 0.<br>
3. The `free_delivery_delta` value is not rounded.<br>
    ***Fix and Result***<br>
    Added formatting to all cost values in the bag and checkout templates as well as rounded the value in the bag view.
4. There is an issue with the emails that are not sent out when completing the purchase nor when creating a new account throwing the Errno 101 network is unreachable.

### TEST 7 
<u>_Test product sorting and filters_</u><br>
Issues found:<br>

1. JavaScript checking the pre-determined size did not work after the update to the filters.<br>
***Fix and Result***<br>
The issue was caused by the change of the value in the templates to pull in size.slug, which results in the size being in lower case. Updated function in the script to look for "m" instead of "M", which resolved the issue.

2. Sorting by rating does not work as expected, putting 4.5 before the rating of 5.
**Not fixed***<br>
Sorting by rating requires consideration of None values and their conversion to 0 (probably) for the sorting to work correctly since all other ratings are integers. Not fixed due to time constraints.

3. Filtering pop up on smaller devices does not scroll - the dropdowns need to be collapsed to show the bottom of the filters in the offcanvas.
**Fix and Result***<br>
CSS issue - adjusted styling of the `#filters` element and offcanvas classes to allow scrolling.

### TEST 8
<u>_Test access to views that require logging by typing urls_</u><br>
The test exposed that the profile page could be accessed by typing up the URL.<br>

***Fix and Result***<br>
Added `LoginRequiredMixin` to _ProfileDetails_, _UpdateProfile_ and _PastOrderDetail_ class views to prevent unauthorised access. When an attempt is made to access these pages, the user is automatically redirected to the login page instead.
This still left `profile` open to not logged-in access because the class overrode the `get` method without calling the `super()`. Changed `get` to `get_context_data` which is more appropriate for this usage anyway.
 
### TEST 9
<u>_Test product management functions_</u><br>
Tests carried out on adding and editing product types, categories, colours and sizes indicated an issue caused by the use of BS modal forms mixins:<br>

The lack of CreateUpdateAjaxMixin in the form caused an issue with the form saving twice, which led to Integrity errors because the slug was created twice. Adding an `if` statement in the model's `save` method did not solve the issue. On the other hand, the presence of CreateUpdateAjaxMixin caused an error (`AttributeError: 'NoneType' object has no attribute 'is_ajax'`) when updating the instances of models.<br>

***Fix and Result***<br>
Created two separate forms for creating and updating instances of the four models working in `bs-Django-modals` as a workaround. A more elegant solution might need to be looked at in the future time permitting.

### TEST 10
<u>_Test 404 and 500 pages_</u><br>
The pages were tested in the deployed Heroku site by trying to access a page that does not exist and by trying to send an email after the creation of the user, which currently results in a 500 error. 
No issues found - both pages work as expected.

### TEST 11
<u>_Testing registering for the account and logging in_</u><br>
User stories tested:

The site user/shopper can securely register for an account. The registration process requires their email to be verified, to ensure correct information is stored for order confirmation and password reset functionalities. This is not working correctly at present due to an issue with linking to the Gmail account - the connection results in [ERRNO 101]: Network is unreachable.

***Fix and Result***<br>


### TEST 12
<u>_User profile pages with ratings and order history_</u><br>
Creating and testing the profile page with order history unveiled an issue with the way product `color` and `size` are stored in the OrderLine model. The initial `OrderLine` model structure followed the BoutiqueAdo walkthrough project, which assumed colour and size are stored as strings. Considering these are separate models in this project, the `OrderLine` model needed an update to store these as references to the instances of `Color` and `Size` models. 

1. Order history is not rendering information about the products contained in the orders and the generation of SKUs is not working as expected.
***Fix and Result***<br>
The initial template called on properties within the instance of `product` attached to the `orderline` rather than properties of the `orderline` itself.

2. Tested whether the button to show older orders is working as expected and splitting is done correctly by adding a few orders and adjusting the split value to 1 rather than 5.
No issues found.

### TEST 13
<u>_Test ratings - rating process and rendering_</u><br>

1. Testing of the rating on _All Products_ page exposed an issue with the average rating showing as the same for all products, due to the variable storing only the value for the last product with ratings in the loop.
***Fix and Result***<br>
Updated the function in the products.contexts to store stars in a dictionary with `product` as key and looped through this in the template rather than the `avg_ratings` dictionary to display the stars.

### TEST 14
<u>_Test subscribe to newsletter functionality</u><br>
The offcanvas does not come up on _All products_ and _Product detail_ pages
 
***Fix and Result***<br>
After some investigation using DevTools it transpired that this is caused by the sizing of the `page-wrapper` on these pages. Fixed by adding a special CSS class for the Mailchimp form overriding the bootstrap offcanvas `bottom` rule and changing it from `auto` to `0`.

## <a name="performance-testing"></a>Testing the performance and responsiveness
Performance testing was done by running the application on various devices and browsers, including:
- Browsers: Firefox 9, Chrome, Safari, Samsung (mobile)
- Devices: Laptop 13', Samsung Note 8 and Samsung Note 10, iPad Pro 10 inch
In addition, the responsiveness of design was tested extensively in Chrome and Firefox DevTools. 

The testing showed some differences in the way the site appears on different browsers, this is however inevitable and does not dramatically change the users' experience of the site.

## <a name="validator-testing"></a>Validator testing 
Each view file has been checked with [Pep 8 online check](http://pep8online.com/) validator. The development took place also in an environment with enabled linters: pylint, flake8 and cornflakes-linter (VS Code extensions).
Some errors raised by Pep 8 refer to the length of links to code referenced in comments and have not been resolved.
HTML and CSS were checked in their relevant W3C validators and results with some notes on the remaining errors and warnings are available [here]().
Lighthouse reports can be accessed [here]

## <a name="programmatic-testing"></a>Programmatic testing 
In addition to testing the code during the development using various print statments, parts of the code was also tested programmatically using Unittest.
Each application has its own `tests` with test files divided according to the part they are testing - `models`, `views` and `forms`. 
The testing is done in an SQlite database separate from the production one, which uses its own `test_settings.py` file.
These tests in this application are not extensive due to time constraints.