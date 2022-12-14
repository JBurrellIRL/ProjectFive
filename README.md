# JB's Record Store

JB's Record Store is a small-scale B2C e-commerce store selling physical music albums on LP, CD and Cassette. The site is targeted towards users who are interested in music and building their physical music collection, an industry that's experienced a major revival over the past number of years. 

Users can browse and purchase a range of music based on their interests. They can browse the store by either format (CD, LP or Cassete) or by musical genre - options for both are available from the main site navigation. They can also read reviews left by other users of the site, and can reach out to the site administrator if needed, either through the site Contact form or else via the store's social media accounts. 

The store uses Stripe to handle payments. As this site was built for educational purposes, please do not enter any live card details into the checkout page. For testing purposes, Stripe's test card details can be used - you can find a link to these details in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [JB's Record Store](https://jbs-record-store.herokuapp.com/)

![Responsive](docs/readme_images/ami-responsive.png)

## Table of Contents

- [User Stories](#user-stories)
- [Site Design](#site-design)
- [Agile Methodology](#agile-methodology)
- [Database Schema](#database-schema)
- [Security](#security)
- [Site Features](#site-features)
- [Business Model](#business-model)
- [Marketing](#marketing)
- [Deployment to Heroku](#deployment-to-heroku)
- [AWS Set Up](#aws-set-up)
- [Forking this repository](#forking-this-repository)
- [Cloning this repository](#cloning-this-repository)
- [Languages](#languages)
- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used-during-site-development)
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)

## User Stories

#### EPIC: Site Content & Navigation
- As a Site User, I can navigate around the site so that I can find content that's relevant to what I am looking for.
- As a site User I can immediately understand the purpose of the site so that I can learn information about the website.
- As a Site User I can view a list of products so that I can select a product that I'm interested in, to view or purchase.
- As a Site User I can click on a product on the main Store page so that I can view extra information about the product.
- As a Site User I can browse the store by product category so that I can find music that's part of the genre I'm interested in.
- As a Site User I can read reviews/testimonials left by other users.
- As a Site User I can have easy access to the Terms & Conditions under which the store operates, and also the store's Privacy Policy.

#### EPIC: User accounts & Profile
- As a new site user I can create an account so that I can be a registered user.
- As a site user I can verify my site membership through an email confirmation so that I can provide extra approval for my site membership.
- As a registered site user I can log in or log out of my account as appropriate so that I can access my user account as required.
- As a site user I can recover or reset my password so that I can gain access to the logged-in features if I have forgotten my login details.
- As a Site User I can view and update my registered shipping address and view previous orders so that I can ensure that my shipping address is correct and view information relating to previous orders.

#### EPIC: eCommerce Functionality
- As a site user I can add products to my shopping bag so that I can purchase them when ready.
- As a site user I can view the contents of the shopping bag at any stage so that I can see the contents along with the current total cost.
- As a Site User I can complete a purchase so that I can buy something without having to register for an account.
- As a Site User I can view a detailed order confirmation after checkout so that I can see all the details of the order I've placed.
- As a site user I can receive an email to confirm my order so that I have a personal copy of the order that I've placed.

#### EPIC: Store Management & Administration
- As a site administrator I can create, update and delete products within the store so that I can manage the items currently for sale.
- As a site administrator I can update and delete registered users so that I can manage the users that have registered on the site.
- As a site administrator I can review and approve customer reviews within the admin panel so that I can add customer reviews to my site, to improve trust in me as a seller.
- As a site administrator I can manage and respond to messages sent through the site contact form so that I can engage with my customers.

#### EPIC: User Interaction
- As a site user I can contact the store owner so that I can send through questions or enquiries to the store owner.
- As a site user I can sign up to the store's newsletter so that I can receive updates on new products being added and/or promotions.
- As a site user I can have the option to visit the store's social media accounts so that I can follow the store through these channels, to learn about current and future products for sale.
- As a site user I can leave reviews of my experience on the site as a buyer so that I can express my views that inform future and existing users of the site.

#### User Stories not yet implemented

The following user story was scoped out of the project at this stage, due to time constraints. It was marked as "Won't-have" within the project board in GitHub Projects, and is added under the "Future Features" heading. This functionality will be returned to at a later date.

- As a site administrator I can avail of automated stock management within the site so that the stock levels of items in the store can decrease automatically once a customer places an order, and I can be notified through email that stock levels of products are running low.

Due to the small size of the store, a search feature user story has also not been added at this time. If the store grows to include more products over time, this will be added to the site header:

- As a site user I can search the site for content so that I can find whether or not the store has an item that I'm looking for.

## Site Design

The site uses a simple and clean design which sticks to minimalistic colours and design thinking. There's a single static image on the site landing page, along with a grid-style Product page with an image thumbnail, product title and assorted information greeting the user. The site uses bright yet contrasting colours to make it easy for the user to navigate around the site. 

#### Fonts

The Oswald font is used within the site for heading areas, whereas the Roboto font is used for paragraph areas and buttons within the site. These fonts complement each other well. The fonts are imported from Google Fonts. As per best practice, Sans Serif is added as a backup font in case the main site fonts are not being imported for any reason.

#### Wireframes

<details>

 <summary>Homepage</summary>

![Landing Page](docs/wireframes/homepage-wf.png)
</details>

<details>

<summary>Store Page</summary>

![Browse Albums](docs/wireframes/products-wf.png)
</details>

<details>

<summary>Reviews page</summary>

![Contact Us](docs/wireframes/reviews-wf.png)
</details>

<details>

<summary>Contact page</summary>

![Contact Us](docs/wireframes/contact-wf.png)
</details>

## Agile Methodology

Github Projects was used to manage the development requirements and process. There's a link to the project board [here](https://github.com/users/JBurrellIRL/projects/3) .

The project comprises of 5 Epics, which are listed within the project as Milestones. A Github Issue was created for each User Story. The User Stories each contain Acceptance Criteria, to make it more clear as to when each User Story has been completed.

## Database Schema

During development, SQLite was used for the site database and for production, ElephantSQL was used in conjunction with Heroku to deploy the live site. Below is an image displaying how the database models relate to each other.

![Database Schema](docs/readme_images/database-structure.png)

## Security

- The database URL and secret key needed to access the database are stored as environment variables in the env.py file, and as config variables in Heroku. I ensured not to push any sensitive information to GitHub on any initial commits, to ensure the integrity and security of my database.
- Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site, to ensure the integrity of the forms.
- Django's LoginRequiredMixin is used for the relevant class-based views in order to restrict access to authenticated users only. Non-authenticated users are redirected to the login page. The UserPassesTestMixin is used to ensure that only the customer that left a review (or the site admin) can edit the review through the front-end of the site.
- For Django function-based views, the login_required decorator is used to restrict access as required.
- I created custom 404 and 403 error pages, to inform the user of the applicable error. These pages also include buttons to return the user to the site homepage.

![404-error](docs/readme_images/404-error.png)

## Site Features

### Header

**Site Title**

- The user is greeted with a site title, positioned to the left, which is clearly defined in the site header. The site title returns the user to the homepage if clicked.

![header](docs/readme_images/navigation.png)

**Navigation**

- The navigation bar is positioned at the top of each page in the site, and includes links to the most popular pages within the site.
- The navigation bar items display differently depending on whether or not the site visitor is logged in. 
- If the visitor is logged out, they'll see an option to either register for an account or to log into an existing account:

![header](docs/readme_images/nav-logged-out.png)

- If the visitor has logged in, the options to register and log in are replaced by a user icon (from Font Awesome) and their username, to show them that they are logged in under that username. Clicking on the username opens a dropdown menu, where the user has an option to go to their profile, add a new product (if logged in as the superuser) or to Logout.

![header](docs/readme_images/nav-logged-in.png)

- The navigation bar also includes a shopping bag, which can be clicked on to reach the shopping bag page. Beside this is a field that shows the running total of the contents of the shopper's bag. This updates dynamically as the shopper adds items to their bag.

![header](docs/readme_images/shopping-bag.png)

- The navigation bar uses Bootstrap classes and is fully responsive to screens of different sizes. It switches to a "hamburger" menu at 992px.

![header](docs/readme_images/hamburger.png)

- The dropdown menus within the hamburger menu retain a white background, so that they're easy for the user to navigate on a mobile device:

![header](docs/readme_images/dropdown-burger.png)

### Footer

![footer](docs/readme_images/footer.png)

- The site footer navigation includes links to Terms & Conditions, Privacy Policy. Customer Reviews and other important pages within the site.
- There's also links to Facebook, Twitter and Instagram along with a link to my personal Discogs record collection catalogue. 
- The external links are coded to open in a new browser tab, so that the visitor is not taken away from the website. The internal links open in the same tab.
- There's also a reference to me as the site designer, along with a link to my personal website.

### Home Page

**Welcome section**

-The home page includes a welcome image and a "Shop Now" button to encourage the user to go to the Product Page. It also includes a brief welcoming paragraph to educate the user on the purpose of this store. Some important keywords are added in `<strong></strong>` tags for the benefit of search engine indexing.

![home](docs/readme_images/banner-area.png)

**General Information section**

-This part of the homepage includes general information about the store, positioned in responsive cards. The cards contain information useful to the user, and directs them to other areas of the site for further information:

![home](docs/readme_images/homepage-cards.png)

**Marketing & About Me section**

-The next section includes a newsletter block that allows the site visitor to sign up to my mailing list. The mailing list is set up via the Mailchimp marketing platform. The text blurb to the right of this includes some brief information about me.

![home](docs/readme_images/marketing-section.png)

### User Account Pages

**Sign Up**

![sign-up](docs/readme_images/authentication/register.png)

**Log In**

![log-in](docs/readme_images/authentication/login.png)

**Log Out**

![log-out](docs/readme_images/authentication/logout.png)

- I used the django-allauth package to create the Sign up, Log in and Log out functionality.
- The user receives messages in their browser to confirm whether or not their login attempt has been successful. They also receive notifications if they've made an error in one of the sign-up or login fields.
- When a user signs up for an account they must verify their membership by clicking on the authentication link emailed to the address they provided.
- If a user forgets their password they can reset it by clicking the 'Forgot Password' on the log in and registration pages.

### User Profile

**Shipping information**

![profile](docs/readme_images/shipping-info.png)

- The shipping address section stores the user's shipping address and phone number.
- The information provided here can be used to autofill the address fields at checkout, to save the customer time.
- There's also an option here for the customer to change their login password, if they wish to.

**Previous Orders**

![profile](docs/readme_images/previous-orders.png)

- The order history section displays a list of all previous orders placed by the customer.
- The display includes the order number, date the order was placed and order total.
- Clicking the order number will take the user to a summary page of that order, with a note stating that the confirmnation shown is of a previous order, not a new one.

### Store Page

**Store Landing Page**

![store](docs/readme_images/store-landing.png)

- The user can reach the products page by either clicking on the "Shop Now" button on the homepage, or via the site navigation. The user has an option to browse by either music genre or physical format from the site navigation. In both the Genre and Format dropdown menus, the user sees an option to browse either by "All Products", which returns all products (paginated to 8 products per page) or by the category filter that they choose.
- The landing page is responsive, and changes the number of products per row based on the width of the user's browser window.
- The user will see a product thumbnail image, artist, format, genre, price and an excerpt description.
- The user has an option to add an item to their shopping cart on the Store landing page. 
- If the user is logged in as a store administrator, they'll also see buttons for Editing and Deleting products under the Add to Cart button.

**Product Detail Page**

![store](docs/readme_images/product-detail.png)

- After clicking on an individual product on the Products page, the user will be taken to the full product details. 
- The product details page displays the product image, artist, format, genre, item condition, Discogs album rating and price, as well as an Add to Cart button. Under everything, the user will see a detailed product description.
- If the user is logged in as a store administrator, they'll also see buttons for Editing and Deleting products above the Add to Cart button.

### Store Management

**Add Product**

![store-management](docs/readme_images/add-product.png)

- A product can be added to the store by a superuser by clicking on the "Add Product" option in the navigation bar user dropdown menu, or via the site back-end. The option in the navigation bar is only visible to superusers.
- If a user that isn't logged in tries to add a product by using the direct URL to the Add Product page, they'll be redirected to the Sign In page.
- If a user then logs into a non-superuser account, they'll receive a message to say that only store administrators can add products, and be redirected to the homepage.
- The user must fill out the fields marked with asterisks. Otherwise, the user won't be allowed to submit the new product and the browser will activate the next compulsory field.
- The 'description' field is the Summernote WYSIWYG editor, added as an extra Django package. It renders in both the back-end and front-end. It's responsive and can be used on mobile and desktop devices.
- The SKU field requires a unique value. If a previously-used SKU is entered into this field, the user receives an error to say that this SKU has already been used. 
- The user can upload an image to the product. If they do not, a default image is used. 
- The user will only be able to submit the form if the form does not return any errors. If there's no errors found, they'll receive a success message after submitting the form.

**Edit Product**

![store-management](docs/readme_images/edit-product.png)

- A superuser can choose to edit a product through the front-end on both the main Store page and also the Product Detail page. 
- If a non-superuser tries to edit the product using the direct editing URL, they're redirected to the login page.
- If the user then logs in as a regular user, they receive an error stating that "only store administrators can modify products", and are redirected to the homepage.
- The form opens with the original content rendered.
- The 'description" field is the Summernote WYSIWYG field, as with the Add Product form.
- The image field displays a thumbnail of the existing image, and a checkbox option exists to allow the superuser to clear the existing image. 
- Once the product has been adjusted, the superuser receives a success message to notify them that the product has been successfully updated.

**Delete Product**

![store-management](docs/readme_images/delete-product.png)

- A superuser has the option to delete products through the site back-end, and also through the front-end on both the Store page and the Product Detail page.
- Clicking on the "Delete" button opens a Bootstrap modal, asking the user if they want to confirm deletion of the product.
- Clicking "Delete" returns a "Product Deleted" message and the product is removed from the database.

**Order management in admin panel**

![store-management](docs/readme_images/order-notes.png)

- Once an order is received, it will appear in the site admin area for the site administrator to view. 
- To help with order management, the site admin also has access to an Order Notes section in the admin panel. Here, the administrator can add a new note and associate it directly with a received order as a foreign key. The administrator can add notes such as the date the order was shipped, tracking numbers etc, and set the order to Fulfilled: Yes or No. This information is stored in the database to help the site administrator with order management.


### Shopping Bag

![shopping-bag](docs/readme_images/shopping-cart.png)

- When the user clicks on the shopping bag icon in the nav bar they are taken to the Shopping Bag page, which shows the products added to the cart, order total, applicable charge for shipping and overall total to be charged.
- The user also sees a notification about how much extra they need to spend to get free shipping, if they are below the free shipping threshold. If they are above that threshold, this message does not appear.
- The user has an option to return to the Store page by clicking on the "Keep Shopping" button.
- The user can remove items from their shopping bag by clicking on the "Remove" button under the product thumbnail. Upon clicking on this, the shopping bag is updated, as are the order totals.
- If the user removes everything from their shopping bag, they receive a message stating that their shopping bag is empty. The order total fields and the "Go To Checkout" button disappear if this takes place.
- Once ready, the user can then proceed to the checkout page by clicking on the "Go To Checkout" button, as long as there is items in their shopping bag at this stage.

### Checkout area

![checkout](docs/readme_images/checkout-page.png)

**Personal Details**

- Within the details section the user can fill out their personal details, shipping address and payment information.
- If the user is a guest, an option to either create a new account or log into an existing account is visible.
- If the user is logged in, a checkbox to save the shipping information to their profile can be selected.
- If the user is signed in and has shipping information saved, the shipping details and email address will auto-populate from the already-saved user profile.
- If a user leaves a required field empty or inputs invalid or empty data, an error will appear to prompt the user to check their inputs.

**Order Summary**

- The Order Summary section lists the items about to be purchased, along with the item subtotal and an order total.
- The order totals give a breakdown of the order total, the cost of shipping and also the grand total to be charged from the customer card.
- The image thumbnail links back to that product's detail page.

**Payment**

- The site payments are handled by the Stripe payment processor. This is a secure payment platform, documentation for it can be found here: https://stripe.com/docs/ .
- Invalid card details will trigger a red warning message stating that the card details entered are invalid.
- After the user clicks to complete payment, a loading screen will be triggered, to let the user know that their transaction is being processed and to discourage them from navigating away before this takes place.
- If the payment form fails or the user closes the browser window before the loading screen disappears, the transaction should still succeed through the inbuilt webhook.
- The payment webhook is designed to search through the database to see if the customer's order exists. If it does not, the webhook will create the order using the customer's details and payment information.

**Order Confirmation**

![checkout](docs/readme_images/checkout-success.png)

- Completing the order takes the user to the checkout success page. Here, the user will see a summary of their completed order, including the shipping address, items purchased and order total. The order also receives a randomly-generated order number. This information will also be visible to a registered user under their "Profile" section described earlier.
- The customer will also receive an email to confirm their order.

### Customer Reviews section

![reviews](docs/readme_images/reviews-page.png)

- The Customer Reviews page can be reached by clicking on the link to the page in the footer of the site.
- When a user navigates to this page, they can see reviews left by previous users. Each review includes the review itself, the username of the reviewer, the rating given by the user, the date the review was left and an image optionally uploaded by the reviewer. If the user chooses not to upload an image, a placeholder image is used instead. 
- The user must be logged in to be able to leave a review. If the person is logged out, a message will appear to let them know they must be logged in to be able to leave a review.
- Once the review is submitted, it must be approved by the site administrator before it can be viewed on the site.
- After the review is approved and is appearing on the site, a logged-in user will have the option to either edit or delete any reviews left by themselves, through buttons that appear under the "Rating" section.
 
**Add Review page**

![reviews](docs/readme_images/add-review.png)

- The user can give their review a title, give it a rating and write a paragraph to describe their experience. They can also optionally upload an image to go alongside their review, once it's been approved by the site administrator.
- Once the review is submitted, the customer receives a message to confirm that the review has been received, and is awaiting approval.

**Edit Review page**

![reviews](docs/readme_images/edit-review.png)

- The user can edit reviews left by themselves only. On the main Reviews page, an option to Edit the existing review will appear under the Rating.
- If someone attempts to edit a review attributed to another user through the direct URL to the editing page, they're redirected to the login screen.
- If they log into an account that did not leave the review they're attempting to edit, they see a custom 403 "forbidden" page, with a link back to the site homepage.

**Delete Review**

![reviews](docs/readme_images/delete-review.png)

- A logged-in user will have access to a Delete button on reviews that they've previously left. This button appears under the "Rating" field on the main reviews page.
- Clicking on the "Delete" button triggers a Bootstrap modal, asking the user to provide confirmation for the deletion of the review.
- Clicking "Delete" returns a "Review Deleted" message and the review is permanently removed from the database.

### Contact Form

![contact](docs/readme_images/contact-us.png)

- A user can open the Contact Us page from either the main top navigation or the footer navigation. 
- The user can submit a query through the form by filling out each field with valid input. 
- If the user inputs a non-email address into the email field, an error is returned to ask the user to check their input.
- If a field is left blank, an error is returned to inform the user that they must fill out that field.
- The site administrator will receive an email with the contents of each submission through the form. The submissions are also logged in the site database and can be managed from within the admin panel.
- The site administrator also has a "Contact Notes" section built into the admin panel, that is associated with each submission. They can log their reply in this area, and mark each message as "replied to" or "awaiting reply".

### FAQs page

![terms](docs/readme_images/faqs.png)

- The user can reach the FAQs page through the link in the footer navigation.
- This page contains information on the condition grading of the items available in the store. The user is given a list of condition grades, along with a detailed description of what each grade means.

### Terms & Conditions page

![terms](docs/readme_images/terms-conditions.png)

- The user can reach the Terms & Conditions page through the link in the footer navigation.
- Here, the user can read the terms and conditions under which the store operates.
- The content was generated using the Free Terms and Conditions Generator [here](https://www.termsandconditionsgenerator.com/).

### Privacy Policy page

![privacy](docs/readme_images/privacy-policy.png)

- The user can reach the Privacy Policy page through the link in the footer navigation.
- Here, the user can find details on the store's privacy policy and how it uses the customer's data.
- The content was generated using the Privacy Policy Generator [here](https://www.privacypolicygenerator.info/).

## Business Model

JB's Record Store's Business Model is Business to Consumer (B2C). The products for sale in the store are sold directly by the store owner to consumers. A customer of JB's Record Store would most likely be someone who is interested in growing their own record collection, or is interested in browsing rare and hard-to-find items and finding their current market value.

## Marketing

### SEO

For this store, keyword research was performed by analysing Google search results, checking competitor's keywords and by utilising wordtracker.com. The keywords most relevant to the store have been added to the site's meta-keywords and meta description. I also used recommended keywords in headings, site content, <strong></strong> tags and image alt-text across the site. 

### Building Trust

I included a Reviews section in the site, which a user can reach through the link provided in the site footer. Including a reviews/testimonials section helps to build trust with my audience. I also included both a Terms & Conditions page and a Privacy Policy page, which will help to reassure any potential customers that they're dealing with a reputable store that takes their privacy and user experience seriously.

### Social Media Marketing

A Facebook business page has been created for organic social media marketing. The branding on the social media page is similar to the branding on the website, and the page can be used to share new content from the site so that people following the business through Facebook can be kept up-to-date on the current content for sale. It also includes a "Shop Now" button to make it easy for visitors to reach the store itself.

![facebook](docs/readme_images/facebook.png)

### Email Newsletter Marketing

Site visitors can sign up to a newsletter when visiting the site. Registering for an account is not needed for this. A signup box is visible in the lower section of the site homepage. The idea of the newsletter is to allow the site administrator to share store news and/or special offers with existing and potential customers via email. The newsletter function was created via Mailchimp.

## Testing

A dedicated testing document can be found [here](https://github.com/JBurrellIRL/ProjectFive/blob/main/TESTING.md).

## Deployment to Heroku

This app was deployed to Heroku using the following steps:

### Create the Heroku App:

- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- Click the button labelled New in the top right-hand corner and from the drop-down menu select "Create New App".
- Enter a unique app name that fits your project.
- Select your region.
- Click on the Create App button.

### Attach the ElephantSQL database:
- Sign up for an [ElephantSQL](https://customer.elephantsql.com/signup) account.
- Click on the "Create New Instance" option to the top right of the page.
- Give your new instance a meaningful name, and select the "Tiny Turtle" plan option for a free database. Then, click on Select Region.
- Choose a data centre that's nearest to your own location. Click on Review, followed by Create Instance.
- Once your instance has been created, copy the database URL and add it to your Heroku project in the Settings tab, in the "Config Vars" section.

### Connect the ElephantSQL database to your project project
- Create an env.py file in the main directory of the project.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Import the env.py file to the settings.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- In settings.py file import dj_database_url, remove the default configuration within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

### Create files / directories
- Create three folders in the main directory; media, static and templates.
- Create a "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in the Heroku Settings tab:
| Variable Name         | Value (Where to find this info)                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| AWS_ACCESS_KEY_ID     | AWS CSV                                                                         |
| AWS_SECRET_ACCESS_KEY | AWS CSV                                                                         |
| DATABASE_URL          | ElephantSQL                                                                     |
| EMAIL_HOST_PASS       | Password from email account                                                     |
| EMAIL_HOST_USER       | Your site email address                                                         |
| SECRET_KEY            | Random key generated using https://miniwebtool.com/django-secret-key-generator/ |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                  |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                       |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret   |
| USE_AWS               | True (When AWS setup is created)                                                |

### Deploy
- IMPORTANT: Ensure in Django settings, DEBUG is False.
- Go to the Deploy tab on Heroku and connect to GitHub - make sure you select the correct repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually.
- Click Open App to view the deployed site.

The site is now live and operational.

## AWS Set Up
### AWS S3 Bucket
- Create an AWS account [here](https://portal.aws.amazon.com/billing/signup).
- In the 'Services' tab on the AWS Management Console, search 'S3' and select it.
- Click 'Create a new bucket', give it a name (it's good to match this to your Heroku app name), and choose the region closest to you.
- Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket Owner Preferred.
- Uncheck Block All Public Access and tick to acknowledge that the bucket will be public.
- Click 'Create Bucket'.
- Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'Edit' and change the Static website hosting option to 'Enabled'. Copy the default values for the index and error documents and click 'Save Changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the Type dropdown menu.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears.
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.


### IAM
- From the 'Services' menu, search IAM and select it when it's returned.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create Group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions'  .
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "Your ARN goes here/",
    "Your ARN goes here/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You must create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Aaa a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you just created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables (as noted in the chart above) as per above list and also in your env.py.


### Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add Django Storages to your installed apps.
- Create an if statement in settings.py, and add the following:

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` so that Django knows where our static files will be coming from in production.

- Create a file called custom_storages.py in your root directory,  and import both our settings from django.conf as well as the s3boto3 storage class from Django Storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

- Also, add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Finally, under 'Permissions', select the option 'Grant public-read access' and click Upload.
- Job done! Your static files and media files should now be linked from Django to your S3 bucket.

## Forking this repository
- Locate the repository at this link [JB's Record Store](https://github.com/JBurrellIRL/ProjectFive).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [JB's Record Store](https://github.com/JBurrellIRL/ProjectFive). 
2. Under the **'Code'** heading, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Languages

- Python
- HTML5
- CSS3
- Javascript

## Frameworks - Libraries - Programs Used during site development
- [Django 3.2](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [JQuery](https://jquery.com/)
- [ElephantSQL](https://www.elephantsql.com/) was used as the database for this project.
- [SQLite](https://www.sqlite.org/index.html) - was used as the database during production.
- [Stripe](https://stripe.com/ie) - the platform used to handle payments.
- [Django Summernote](https://summernote.org/) - WYSIWYG text editor for product descriptions.
- [AWS](https://aws.amazon.com/?nc2=h_lg) - used for file storage.
- [Heroku](https://dashboard.heroku.com/login) - Cloud-based platform used for deployment of project.
- [Google's Mobile Responsiveness Test](https://search.google.com/test/mobile-friendly) - Used to verify mobile responsivenenss of website.
- [Am I Responsive](https://ui.dev/amiresponsive) - Mobile responsive test.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons across the site.
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Used for icons on product page.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [Jshint](https://jshint.com/) - used to validate JavaScript.
- [Coolors](https://coolors.co/) - Used for colour palette tests.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design.
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used with Django Forms.
- [Bootstrap 5](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for responsiveness and site styling.
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert Excel CSV tables to markdown.
- [Sitemap Generator](www.xml-sitemaps.com): used to create sitemap.xml file.
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/): Used to create the site's privacy policy.
- [Terms & Conditions Generator](https://www.termsandconditionsgenerator.com/)): Used to create the site's terms & conditions.
- [Mailchimp](https://mailchimp.com/?currency=EUR): Used to create the newsletter signup functionality.
- [RegExr](https://regexr.com/): Used this to learn about and reference regular expressions.

## Credits

- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [Bootstrap 5.0 Docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Discogs](https://discogs.com) - A selection of the album information text for this site plus images were sourced from Discogs. JB's Record Store is not a live site, is for educational purposes only and no copyright infringement whatsoever is intended.
- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

## Acknowledgement

Thanks to my mentor, Jack Wachira, for his truly invaluable feedback and advice. 