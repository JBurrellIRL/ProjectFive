# JB's Record Store

JB's Record Store is a small-scale B2C e-commerce store selling physical music albums on LP, CD and Cassette. The site is targeted towards users who are interested in music and building their physical music collection, an industry that's experienced a major revival over the past number of years. 

Users can browse and purchase a range of music based on their interests. They can browse the store by either format (CD, LP or Cassete) or by musical genre - options for both are available from the main site navigation. They can also read reviews left by other users of the site, and can reach out to the site administrator if needed, either through the site Contact form or else via the store's social media accounts.

The store uses Stripe to handle payments. As this site was built for educational purposes, please do not enter any live card details into the checkout page. For testing purposes, Stripe's test card details can be used - you can find a link to these details in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [JB's Record Store](https://jbs-record-store.herokuapp.com/)

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

The following user story was scoped out of the project at this stage, due to time constraints. It was marked as "Won't-have" within the project board in GitHub Projects. This functionality will be returned to at a later date.

- As a site administrator I can avail of automated stock management within the site so that the stock levels of items in the store can decrease automatically once a customer places an order, and I can be notified through email that stock levels of products are running low.

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
