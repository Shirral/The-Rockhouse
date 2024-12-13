## Testing

### Validator Testing

* **HTML:**

The validator was not happy about the duplicate IDs of some elements on my website - particularly these that exist in the DOM twice, but only one version is shown to the user, depending on their screen size.

I have changed my duplicate IDs to classes with the exception of two unique IDs in the customisation.html template. That solved the problem. The validator found no more issues.

[W3C validator](https://validator.w3.org/) was used.

* **CSS:**

The validator has found no errors. The only warnings were about the vendor extensions - nearly exclusively all from the Bootstrap css.

[W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/) was used.

* **JS:**

The validator has found two missing semicolons in the customisation.js file. The semicolons have been fixed.

[JQuery Validator](https://www.utilities-online.info/jquery-validator) was used.

* **Python:**

I have been working with Python and Flake8 extensions for VS Code as I've been working on the project. All of the errors would be caught and resolved instantly. I have only left the "line too long" problems to solve last as I wasn't sure how to correctly and safely split my lines of Python code into shorter bits without breaking anything.

The Flake8 errors have been fixed except for a few lines which couldn't be split easily, mostly in the settings.py file.

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8) extensions have been used.

### Manual testing: Features

| Feature       | Expected behaviour | Action  | Result |
| ------------- |--------------------| --------|--------|
| *Responsive design* | When the project is viewed on different kinds of devices with different screen sizes, the design should remain clear and functional. The elements of all the pages should resize to match the window size. The rock grids and the layout of the About page should be different for small screens and bigger screens.  | The project is opened and tested on several different devices: a laptop (Acer Nitro 5), an Android phone (Ulephone Power Armor 14), and an iOS tablet (iPad Air 4th Generation). | The elements of the project respond to the different screen sizes correctly, changing their proportions to preserve the design and functionality of the website. |
| *Messages - alerts* | The messages should be displayed on the top part of the main section of the page, above all the main elements, but below the navbar. They should not cover any other page elements. | Log in, log out, adopting a rock and customising it, submitting an accessory request form and trying to submit a faulty form are all performed on all of the devices used for testing. | The mesages are displaying correcly on all devices. |
| *Navbars* | Both navbars should show the app logo, the profile icon, and the three standard links or the burger button in the usual positions. The burger button should trigger a menu to show. Clicking on all the links should lead to being taken to ther respective destinations. | The navbars are inspected on different devices. All the elements are clicked/tapped. | The navbars behave correcly. All of the navbar elements are displayed correctly. All links work as intended, the side menu navigation works as intended. |
| *Footer* | The footer should always stay at the bottom of the screen. The external social media links should open in new tabs. | All of the pages of the website are loaded. The social media links are clicked/tapped. | The footer and its links behave as expected. |
| *Homepage - Available Adoptions* | The homepage should display a grid of cards featuring rocks available for adoption. There should be no adopted rocks among them. The page should use the main navbar and the name 'Available Adoptions' should be underlined. Clicking on a picture of the rock or 'see more' link should lead to the rock profile page. Admind should see an [edit] link on the cards that should take them to the edit page for a given rock. | The homepage is loaded and inspected. The active elements are clicked. | The elements behave correctly on all devices. |
| *Gallery page* | The gellry page should display a grid of rocks that have been adopted. There should be no rocks available for adoption among them. All the rocks should have an owner displayed on them. The rocks with accessories should have the accessories displaying correctly on the rock image. Clicking on the rock image should take the user ot the rock profile page. | The page is loaded and inspected. The rock images are clicked/tapped. | The gallery behaves as expected. |
| *About page* | The page should display three sections of information about The Rockhouse using a Bootstrap grid. The layout should be different for bigger and smaller screens. The cards showing core crew members should be evenly spaced across the screen, no matter the screen size. | The page is inspected on different devices. | The page displays the information correctly. |
| *Account management* | All of the allauth templates used in the project should have custom styling to fit with the rest of the website. Every functionality of allauth should work - users should be able to register, login, change their password, add and remove emails. The form validation should prevent users from submitting invalid information. | A test user is registered, confirms their email, then logs in, changes password, adds a new email address, confirms it, removes the previous email address, then logs out, then uses the "forgot password?" link to reset their password. A login attempt is made with random credentials and with empty fields. A register attempt is made using a username that's already taken, and using empty fields. | Allauth templates are all styles and work correctly. The form errors are displayed to the user, preventing them from submitting invalid information. |
| *Rock profile page* | The page should display intormation about the rock: its image, name, material, texture, personality, and a description for all the rocks, as well as whether it's available for adoption and its cost and a button to proceed with the adoption for the rocks that don't yet have owners. For the rocks owned by the users, the name of the owner should be shown instead, along with the user's notes about the rock, if they've added any, and any accessories they might have added to their rock. The admin should see the edit link only on the available rocks. Clicking on the proceed/back/edit links should take the user to the right pages. | One of the available rock's profile page is opened; one of the adopted rock's profile page is also opened. | The latter has accessories and user notes. Everything is displayed as it should. |
| *Rock edit page* | The page should only be available to admins; normal users should be redirected away if they try to access it. The page should have layout similar to the rock profile page. The admin should be able to edit rock's name, material, texture, personality, and a description. They should also be able to delete a rock. A warning confirmation modal should appear if they click on the delete link. The modal should inform the admin if the rock is owned by a user. | The page is accessed by an admin user and a non-admin user. They try to make changes and delete rocks. | The page is displayed and behaves correctly, but it was initially accessibile to everyone with the link. This has now been fixed - normal users are redirected to the rock profile page. |
| *Adoption confirm page* | The page should offer the users a link to go back and a button to proceed with the adoption. | The elements are clicked/tapped. | The links work as intended. |
| *Adoption form page* | The user should be able to fill in the form, card information, and finalise the adoption. The form validation should not allow the user to submit a faulty form and should tell the user what they need to change. Stripe's widget should only accept valid cards. The user should be directed to the Adoption success page upon a successful adoption. | The form is filled incorrectly and submission is attempted - fields are left blank, invalid card data is used. Then, form is filled correctly and submission is attempted. | The form displays errors if any fields are invalid. The form is processed successfully. Stripe widget validates the card successfully. The user is brought to Adoption success page after a successful adoption.|
| *Adoption success page* | The form should give the user two links: one to their profile and one to the customisation tool. They should work. | The links are clicked/tapped. | The links lead the user where they should. |
| *User profile page* | The page should display user's name, date of joining, and the number of rocks they own as well as a grid of cards displaying their rocks. The cards should show the rock image with any customisations, rock's name, short description, date of adoption, and a see more link, plus a [customise] link only available to the rock owners. | The page is loaded and inspected. The links are clicked. | Everything works as it should. |
| *Customisation page* | The customisation page should show changes made to the rock in real time, right after a customisation option is chosen. The options should be separated into accessories and frames and displayed in their own sections in the accordion menu. The user should be able to save the changes and see them afterwards. The user should be able to add notes. The user should be able to access accessory request page through he link. | The page is loaded. Three accesories and one frame are chosen. Notes are added. The changes are saved. The link to the accessory request page is clicked. | Everything is working as expected. |
| *Accessory request page* | The page should display a form which users should be able to fill. The form should be validated and not accept invalid input. It should tell the users what needs fixing. Upon a successful submission, an AccessoryRequest object should be created in the database, available for the admins to view in the admin panel. | The form is filled incorrectly; a submission attempt is made. The form is filled correcly; a submission attempt is made. The AccessoryRequest objects are viewed in the admin panel. | The form validates correctly. The form submits correctly. The object is created in teh database correctly. |
| *List delete modal* | The List delete modal should appear on the screen and darken the rest of it when the delete list button is clicked. It should give the users an option to proceed and to go back. The modal should be hidden if the user chooses to cancel the operation; if they coose to proceed, the modal should disappear, the list should be deleted, and the user should be brought back to the Lists page. Clicking outside of the modal should close it. | The delete list button is clicked. Each link in the modal window is clicked. Clicking outside of the modal is performed, too. | The modal appears and disappears as it should. Both links work and do what they should do. |
| *Django admin* | The admin panel should only be accessible to superusers. The superusers should be able to perform any kind of operations on the objects in the databases from there - they should be able to add rocks and accessories, edit and delete them, to manage user's account information, and to read the new AccessoryRequest and new RockAdoptions. | A superuser navigates to the admin panel. A non-superuser navigates to the admin panel. The admin tries to add a rock and an accessory, edit a rock and an accessory, delete a rock and an accessory. The admin tries to change a user's email and password. The admin tries to read the information from the AccessoryRequest objects and RockAdoption objects. | The admin is let in the admin panel. The ordinary user is stopped and told to log in as an admin. The admin can perform every kind of operations on the objects in the database. |

### Manual Testing: Testing User Stories from the UX/UI section of README.md

**1. First Time Visitor Goals**

* *As a first time visitor, I want to learn what The Rockhouse is and why would anyone want to adopt a virtual rock.*

    * The user navigates to the About page which is showcased among the main links on the homepage and easily accessible. There, they get to learn about the idea behind the Rockhouse and about the perks of being an owner of a virtual pet rock.

* *As a first time visitor, I want to have a look at the rocks available at the website.*

    * The user is brought to the homepage, on which the available adoptions are shown. The user scrolls the page and beholds the rocks. They might click on rocks that appeal to them and learn more about them.

* *As a first time visitor, I want to see what's in the gallery.*

    * The user navigates to the gallery page which they can locate easily as it's highlighted among the main 3 links showed on the homepage. They see the adopted rocks in all their accessorised glory.

* *As a first time visitor, I want to create an account.*

    * The user spots a reasonably sized LOGIN/REGISTER button in the top right corner of the homepage. They click on it. They choose to create an account, as they don't have one yet, and they fill in the sign up form. They confirm their email address and their account is ready.

**2. Returning Visitor Goals**

* *As a returning visitor, I want to log in to my account.*

    * The user either clicks on the big LOGIN/REGISTER button in the main navbar, or spots the profile icon associated with user functionalities. They click on it. They are either led directly to the login page or they see a menu that gives them an option to navigate there. The user fills in the login form and they click on the log in button.

* *As a returning visitor, I want to change my email or password.*

    * The user, associating the profile icon with user functionalities, clicks on it. They see the password change and email management option there. They pick the one they want and follow the instructions shown on the screen to change their email/password.

* *As a returning visitor, I want to adopt a rock.*

    * The user scrolls available rocks on the homepage and picks the one they like. They click on it, go to its profile, and click on the PROCEED button after being informed that the rock is indeed available for adoption. They confirm their intention on the next page and they fill in the adoption form - their billing information and their payment card information. Upon a confirmation from Stripe, the user is brought to the success page - they now own the rock.

* *As a returning visitor, I want to customise my rock.*

    * Freshly after adopting the rock, the user spots a link to the customisation page on the success page. They click on it. Later on, they see a [customise] option on the rocks in their profile. They click on it. The user chooses the accessories they want and clicks the SAVE CHANGES button.

* *As a returning visitor, I want to add a note about my rock.*

    * Freshly after adopting the rock, the user spots a link to the customisation page on the success page. They click on it. Later on, they see a [customise] option on the rocks in their profile. They click on it. They see a text field encouraging them to tell the world about their rock and they fill it with their notes. They click on the SAVE CHANGES button.

* *As a returning visitor, I want to see other people's rocks.*

    * The user navigates to the gallery again. They compare their rocks with oher users' rocks, perhaps click on other users' names to see their profiles.

* *As a returning visitor, I want to request an accessory that is not available in the customisation app to be added to it.*

    * The user either sees an option to request an accessory on the customisation page, or in their profile menu. They click on it. The accessory request page explains how it works, and the user fills the form with the idea for a cool accessory they have. They submit the form.

**3. Website administrator goals**

* *As the website administrator, I want to add new rocks and accessories.*

    * The administrator navigates to the admin panel through the link in their profile menu. There, they see Rocks and Accessories. They choose the one they want and click on the "Add" button.

* *As the website administrator, I want to make quick changes to rocks available for adoption without having to go to the admin panel.*

    * The administrator finds the rock they want to make a quick change to on the Available Adoptions page and clicks the [edit] link. They make the changes they want and save them.

* *As the website administrator, I want to see the accessory requests from the users.*

    * The administrator navigates to the admin panel through the link in their profile menu. There, they see AccessoryRequest category. They click on it and see all of the requests that came from the users. They can now click on any of them to see exactly what each user requested.

* *As the website administrator, I want to see the information on the new adoptions.*
    
    * The administrator navigates to the admin panel through the link in their profile menu. There, they see RockAdoption category. They click on it and see all of the adoptions made so far. They can now click on any of them to see the details.

* *As the website administrator, I want to change any user's profile information like email or password in case they have lost access to their email and cannot access their account.*
    
    * The administrator navigates to the admin panel through the link in their profile menu. There, they see Users category. They click on it and see all of the users. They can now click on any of them to see and edit their details. They also see the Email addresses category which they can elso edit.

### Further Testing

The website has been tested on a variety of screen sizes (resizing the browser window on desktop, tablet, smartphones), browsers (Chrome, Safari Edge, Firefox), and devices, by several different people who were asked to check if it works as expected. A few design elements like the two top sections or the email management screen buttons could look better on medium-sized screens, but the overall results were good.

## Bugs fixed & problems overcome

| Problem description   |  Fix  |
| --------------------- | ----- |
| The input elements on the rock edit page, when prepopulated with the rock object's properties' current values, would only display the first word of multi-word strings.  | It turned out I forgot to encase the {{rock.something}} tags in quotes when putting them as the value of the 'value' property of the input elements. Adding the quotes solved the issue. |
| Many, many problems with custom CSS styles not being applied, or templates not being seen by Django. | Refreshing cache and restarting the server would often solve the problem. |
| Textares's 'rows' property wouldn't work. | Bootstrap's styles were giving the textarea a fixed height, overriding the effects of the 'rows' property. Overriding Bootstraps's style and setting a desired height solved the problem. |
| Textarea would produce unnecessary whiespace at the beginning of the text in it when I populated it with the value of {{rock.description}}. | Putting the entire textarea on one line of the html file solved the problem. |

Due to the nature of working with Python, any other issues were being corrected on the go the moment they arised - the application would throw an error and refuse to work whenever something was wrong - so they never got a chance to become bugs.