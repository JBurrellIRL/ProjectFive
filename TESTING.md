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

- *As a site user I can view a list of products so that I can select a product that I'm interested in, to view or purchase.*

The site user can browse a list of products for sale from the main navigation. By clicking into either the "genre" or "format" dropdown menus, they can click to view All Products. They can also click on the "Shop Now" action button in the middle of the homepage to reach the store.

![Site Content - Store](docs/testing_images/reach-store-page.png)

Once they reach the store page, they can view a list of products for sale. The page is paginated to show 8 products at a time. They can move between sub-pages using the pagination navigation option at the bottom of the page. They can also add a product to their shopping bag from this page.

![Site Content - Store](docs/testing_images/store-page.png)

- *As a site user I can click on a product on the main Store page so that I can view extra information about the product.

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