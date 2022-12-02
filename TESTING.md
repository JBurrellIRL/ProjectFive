# Testing Document

## User Story Testing

### EPIC 1 - Store Management & Administration

- *As a site admin I can create, update and delete products within the store so that I can manage the items currently for sale.*

The site administrator has full access to CRUD functionality for all products, both from within the site front-end and also within the site admin panel. 

When logged in, the site administrator can add products through an "Add Product" option that appears in the user drop-down menu:

![Store Management - Add Product](docs/testing_images/add-product.png)

When logged in, the site administrator can edit and delete products through both the main store page and also the product details page. Edit and Delete buttons appear, only for the site administrator:

![Store Management - Edit Product](docs/testing_images/edit-product.png)
![Store Management - Delete Product](docs/testing_images/delete-product.png)

- *As a site admin I can update and delete registered users so that I can manage the users that have registered on the site.*

The site admin can edit and delete users from the site admin panel. They can delete existing users, add new users, and edit and manually verify the email addresses of registered users.

![Store Management - Manage users](docs/testing_images/delete-users.png)
![Store Management - Manage users](docs/testing_images/update-email.png)

- *As a site administrator I can manage and respond to messages sent through the site contact form so that I can engage with my customers.*

The site admin can view all submissions sent through the Contact form from the site admin. They can mark each submission as "replied to" if they wish, to assist with contact management.

![Store Management - Manage messages](docs/testing_images/contact-form-manage.png)

- *As a site admin I can review and approve customer reviews within the admin panel so that I can add customer reviews to my site, to improve trust in me as a seller.*

The site admin can approve, review and delete customer reviews from the site admin panel. They can also delete approved reviews from the site front-end if they wish to. The functionality to edit approved reviews on the front-end is also built-in, but not currently added to the Reviews template.

![Store Management - Manage reviews](docs/testing_images/manage-reviews.png)
![Store Management - Manage reviews](docs/testing_images/managereviews-front.png)

### EPIC 2 - User Interaction

- *As a site user I can contact the store owner so that I can send through questions or enquiries to the store owner.*

The user can contact the store by going to the "Contact" page in the main navigation or footer navigation, and filling out the form. The form submission triggers an email to go to the site admin, as well as adding an entry to the database.

![User Interaction - Contact](docs/testing_images/contact-form.png)

- *As a site user I can add, edit and delete reviews of my experience on the site as a buyer so that I can express my views that inform future and existing users of the site.*

Site users can navigate to the "Customer Reviews" section in the footer navigation. They must log in to be able to leave a review. They can then add a review, where they can add their review title, write a description, and leave a rating 1 to 5, all of which appear on the site once their review has been approved.

![User Interaction - Reviews](docs/testing_images/add-review.png)

Once the review is approved, the user can either edit or delete their own review, based on their choice. Edit/Delete buttons are present, to the user that left that particular review.

![User Interaction - Reviews](docs/testing_images/edit-delete-review.png)

- *As a site user I can sign up to the store's newsletter so that I can receive updates on new products being added and/or promotions.*

The site visitor can sign up to a newsletter on the store homepage, to receive news relating to the store by email. The newsletter is set up via Mailchimp.

![User Interaction - marketing](docs/testing_images/mc-newsletter.png)

- *As a site user I can have the option to visit the store's social media accounts so that I can follow the store through these channels, to learn about current and future products for sale.*

The site user has access to the store's social media profiles in the site footer. There's links to Facebook, Twitter and Instagram along with a link to the store owner's personal Discogs profile.

![User Interaction - social](docs/testing_images/social-media.png)

### EPIC 3: Site Content & Navigation

- *As a Site User, I can navigate around the site so that I can find content that's relevant to what I am looking for.*

The site user has access to the main site navigation and footer navigation on all pages on the site. These are site-wide and appear no matter which page the visitor is viewing.

![Site Content - Main Nav](docs/readme_images/navigation.png)
![Site Content - Footer Nav](docs/readme_images/footer.png)

- *As a site user I can immediately understand the purpose of the site so that I can learn information about the website.*

This user story is covered by the general site content, which has been worked on throughout the project. The site is clearly structured, from the site title to the text and image content on the site, and its purpose is clear from all aspects. 

- *As a site user I can view a list of products so that I can select a product that I'm interested in, to view or purchase.*

The site user can browse a list of products for sale from the main navigation. By clicking into either the "genre" or "format" dropdown menus, they can click to view All Products. They can also click on the "Shop Now" action button in the middle of the homepage to reach the store.

![Site Content - Store](docs/testing_images/reach-store-page.png)

Once they reach the store page, they can view a list of products for sale. The page is paginated to show 8 products at a time. They can move between sub-pages using the pagination navigation option at the bottom of the page. They can also add a product to their shopping bag from this page.

![Site Content - Store](docs/testing_images/store-page.png)

- *As a site user I can click on a product on the main Store page so that I can view extra information about the product.*

The user can click on either the product thumbnail or the product title on the product page to be taken to the product detail page. Once there, they can view extra details not visible on the product page, including the item condition and a full description. The option to Add to Cart is also present here, as is a "Back to All Products" button. 

![Site Content - Store Detail](docs/testing_images/product-detail.png)

- *As a site user I can browse the store by product category so that I can find music that's part of the genre I'm interested in.*

The user can browse by either album format or music genre from the main site navigation.

![Site Content - Category Nav](docs/testing_images/category-nav.png)

- *As a Site User I can find the Terms & Conditions and Privacy Policy applicable to this store so that I can have a better understanding of how this store operates and handles my data.*

The site user has access to these pages from the site footer.

![Site Content - Footer Nav](docs/readme_images/terms-conditions.png)
![Site Content - Footer Nav](docs/readme_images/privacy-policy.png)

- *As a site user I can find out what the item condition grades mean so that I will know what to expect in terms of item quality when I receive it."

The FAQ page in the site has information on this, and gives a detailed breakdown of what each condition grade means. This page is accessible from both the main navigation and the footer navigation.

![Site Content - FAQ](docs/readme_images/faqs.png)

### EPIC 4: eCommerce Functionality

- *As a site user I can add products to my shopping bag so that I can purchase them when ready.*

The site user has the option to add a chosen product to their cart from both the main store page and the product detail page. Once they add an item to their cart, they receive a browser message to let them know that the product has been added successfully to their cart.

![eCommerce - add-to-cart](docs/testing_images/add-to-cart.png)

- *As a site user I can view the contents of the shopping bag at any stage so that I can see the contents along with the current total cost.*

The site user can click on the Cart icon in the site header at any time, which takes them to the Shopping Bag page. Here, they can view all the products within the shopping bag at that particular time. The page also gives them a running total of their order, including order total, applicable shipping costs and amount to pay.

![eCommerce - bag](docs/readme_images/shopping-cart.png)

- *As a site user I can enter my payment details at checkout so that I can purchase the items in my shopping bag.*

After proceeding from the bag to the checkout, the customer can enter their card details securely in order to complete their purchase. The payment widget is embedded from Stripe, and takes care of the site payments. While the payment is being processed, the user will see a spinning wheel, indicating that the transaction is being processed. This should also discourage them from navigating away before the order is confirmed.

![eCommerce - checkout](docs/testing_images/checkout-page.png)

- *As a Site User I can purchase without registering, so that I can buy something without having to register for an account.*

No registration is required for a buy to be able to make a purchase from the site. The buyer can proceed through the checkout process without needing an account - they do, however, receive an option to create an account on the checkout page. 

![eCommerce - guest-checkout](docs/testing_images/create-account.png)

- *As a Site User I can view a detailed order confirmation after checkout so that I can see all the details of the order I've placed.*

Once the order is completed, the shopper will see an order confirmation screen that details their order in full. They can also see this confirmation screen for previous orders from their user profile page.

![eCommerce - order-confirmation](docs/testing_images/order-confirmation.png)

- *As a site user I can receive an email to confirm my order so that I have a personal copy of the order that I've placed.*

An order confirmation is sent out from the store administrator email account to the email address added to the order at checkout.

![eCommerce - email-confirmation](docs/testing_images/email-confirmation.png)

### EPIC 5: User accounts & Profile

- *As a new site user I can create an account so that I can be a registered user.*

The visitor to the site can register for an account using the "Register" option in the main navigation bar. An option to create an account also exists at checkout.

![Accounts - register](docs/testing_images/register.png)

- *As a site user I can verify my site membership through an email confirmation so that I can provide extra approval for my site membership.*

After signing up with an email address, username and password, the user will receive an email to the email address they provided, asking them to click the link to confirm their membership. This decreases the likelihood of spam accounts being created on the site, and also increases the security of the user themselves, as they can lower the risk of being subscribed to a site that they didn't agree to.

![Accounts - confirm membership](docs/testing_images/confirm-account.png)

- *As a registered site user I can log in or log out of my account as appropriate so that I can access my user account as required.*

The user can log in and out of their account from the main navigation bar. If logged out, an option will exist to either register or log in. If already logged in, the registration option disappears and a "Logout" option appears the user account dropdown menu.

![Accounts - log in-out](docs/readme_images/nav-logged-out.png)
![Accounts - log in-out](docs/readme_images/nav-logged-in.png)

- *As a site user I can recover or reset my password so that I can gain access to the logged-in features if I have forgotten my login details.*

An option exists for the user to reset their password if they have forgotten it. This option is visible on the login screen, and also on the registration page. Clicking on this option will take them to the password recovery page.

![Accounts - password-recovery](docs/testing_images/password-reset.png)

- *As a Site User I can view and update my registered shipping address and view previous orders so that I can ensure that my shipping address is correct and view information relating to previous orders.*

The logged-in user can access their profile through the user account dropdown menu in the main navigation. Here, they can update their registered shipping address and view their previous orders. There's also an option to change their login password if they wish to do that.

![Accounts - password-recovery](docs/readme_images/)


