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

