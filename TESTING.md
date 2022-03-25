# TESTING
<!-- The program was tested at each step of the development within the development environment as well as on Heroku after the deployment. The testing processes included:
1. [User Stories testing](#user-stories-testing)
2. [Validator testing](#validator-testing)
2. [Programmatic testing](#programmatic-testing)
3. [Performance testing](#performance-testing)
4. [Development testing](#bugs-and-fixes)

## <a name="user-stories-testing"></a>User Story testing
Functionality was tested at each stage of development and as each of the stories in the Git Project was completed. Refer [here](https://github.com/Koko-66/teaze/projects/1) for details of the stories.
The testing entailed going through each feature of the app and ensuring that the application runs as expected and yields expected results, without causing any errors.

## <a name="validator-testing"></a>Validator testing 
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
Each feature was tested while being developed to ensure correct and error-free functionality. Each of the bugs encountered was resolved by using a combination of error message analysis, print statements, and research for possible causes and solutions.

1. The testing on serving static files was done at the start of the project to avoid issues at later stages, which seems to be a common issue. To carry out the test, added coloured background to the css file and an image from Cloudinary and changed the DEBUG setting to `False` for the time of testing.

<!-- ### Issues pending fixing -->
