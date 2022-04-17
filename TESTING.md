# TESTING
The program was tested at each step of the development within the development environment as well as on Heroku after the deployment. The testing processes included:
1. [User Stories testing](#user-stories-testing)
2. [Validator testing](#validator-testing)
2. [Programmatic testing](#programmatic-testing)
3. [Performance testing](#performance-testing)
4. [Development testing](#bugs-and-fixes)

## <a name="user-stories-testing"></a>User Story testing
Functionality was tested at each stage of development and as each of the stories in the Git Project was completed.
The testing entailed going through each feature of the app and ensuring that the application runs as expected and yields expected results, without causing any errors.

### 1. As a shopper/site user I can read about the products and the company so that I know what products the site offers.

On entering the page, the user reads a brief message about the site's purpose and the company's misson and is invited to enter the shop. The top banner and the main menu is visible on this page as well, and the shopping cart icon is replaced with a t-shirt. 

### 2. As a site user/shopper I can easily access the company's social media from the website so that I see the company's reviews and events.

The links to social media sites are placed at the very top of the page in a banner that is visible at all times.

### 3. As a shopper I can view a list of products so that I can find what I want to buy.

The main product page lists all available items wiht images and information about the product. On clicking the item, the shopper can access a page with more product details.

### 4. As a shopper I can search for products and filter them by category so that I can easily find what I am looking for.

The site features a search bar, where the user can look for a product by keyword in product name and description.

### 5. As a shopper I can view product details so that I can check the price, description, color and size options.

The shopper can view product details by clicking o the product card in the main product view. The product detail page contains product name, price, description, lists of available colors and sizes, list of categories and rating, if available.

### 6. As a site user I can easily register for an account so that I can view my previous orders and store my delivery details.

The site user/shopper can register for an account in a secure way. Regisrtation process requires their email to be verified, to ensure correct information is stored for order confirmation and password reset functionalities.

### 7. As a site user I can easily log in and out of the site so that I can access my account and prevent access to it by others.

The login/logout options are readily available from the top banner and are visible at all times.

<!-- ## <a name="validator-testing"></a>Validator testing 
Each view file has been checked with [Pep 8 online check](http://pep8online.com/) validator. The development took place also in an environment  with enabled linters: pylint, flake8 and cornflakes-linter (VS Code extensions).
Some errors raised by Pep 8 refer to the length of links to code refernced in comments and have not been resolved.
HTML and CSS were checked in their relevant W3C validators and results with some notes on remaining errors and warnings are available [here](https://github.com/Koko-66/teaze/blob/main/static/data/CSS%20and%20HTML%20validation.pdf).
Lighthouse reports can be accessed [here]

## <a name="programmatic-testing"></a>Programmatic testing 
In addition to testing the code during the development using various print statments, the code was also tested programmatically using Unittest.
Each application has its own `tests` with test files divided according to the part they are testing - `models`, `views` and `forms`. 
The testing is done in an SQlite database separate from the production one, which uses its own `test_settings.py` file.
The decisions on which part of code needed testing were based on reports generated with the use of __Coverage__ plugin and at the most current report stands at 92%. -->

<!-- ## <a name="performance-testing"></a>Performance and responsiveness testing
Performance testing was done by running the application on various devices and browsers, including:
- Browsers: Firefox 9, Chrome, Safari, Samsung (mobile)
- Devices: Laptop 13', Samsung Note 8 and Samsung Note 10, iPad Pro 10 inch
In addition, the responsiveness of design was tested extensively in Firefox DevTools. -->

## <a name="bugs-and-fixes"></a>Development Testing
Each feature was tested while being developed to ensure correct and error-free functionality. The bugs encountered was resolved by using a combination of error message analysis, print statements, and research for possible causes and solutions.

### TEST 1 ###

#### _Serving static files_ ####
The testing on serving static files was done at the start of the project to avoid issues at later stages, which seems to be a common issue. The test involved adding coloured background to the base.css file and an image from Cloudinary to the index page and changing the DEBUG setting to `False` for the time of testing.
#### _Result_ ####
Static files and an image served on Heroku as expected, with orange background and the image visible in the corner of the page.

### TEST 2 ###

#### _Testing models in the admin_ ####
All models were tested in the admin to ensure everything works as expected before moving on with the development.
#### _Result_ ####
No issues found.

### TEST 3 ###

#### _Testing adding sizes to bag_ ####
Testing of the walkthrough method for adding sizes to bag 
revealed an issue in updating the product list in the bag. If the same product already existed in the bag and another was added, it would replace the previously listed product, rather than update its amount, or create a new listing with a different size.
#### _Result_ ####
Testing showed the issue to be the type of the `item_id` (`int`). Conversion of the `item_id` to a string and using this value in the function instead, solved the issue.

<!-- ### Issues pending fixing -->
