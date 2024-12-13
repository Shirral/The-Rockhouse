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

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8) extensions have been used.

### Manual testing: Features

| Feature       | Expected behaviour | Action  | Result |
| ------------- |--------------------| --------|--------|
| *Responsive design* | When the project is viewed on different kinds of devices with different screen sizes, the design should remain clear and functional. The elements of all the pages should resize to match the window size. The layout of newlist.html and index.html should be different for small screens and bigger screens.  | The project is opened and tested on several different devices: a laptop (Acer Nitro 5), an Android phone (Ulephone Power Armor 14), and an iOS tablet (iPad Air 4th Generation). | The elements of the project respond to the different screen sizes correctly, changing their proportions to preserve the design and functionality of the game. |
| *Flash messages* | The flash messages should be displayed on the top part of the main section of the page, above all the main elements, but below the navbar. They should not cover any other page elements. | Log in, log out, account creation and deletion, creating/editing/deliting a list and a category are all performed on all of the deviced used for testing. | The flash mesages are displaying correcly on all devices. |
| *Navbar* | The navbar should show the app logo, the profile icon, and the three standard links or the burger button in the usual positions. The burger buton should trigger a side menu to show. Clicking on all the links should lead to being taken to ther respective destinations. | The navbar is inspected on different devices. All the elements are clicked/tapped. | The navbar behaves correcly. All of the navbar elements are displayed correctly. All links work as intended, the side menu navigation works as intended. |
| *Homepage* | The homepage should display text on the left, an image on the right on the bigger screens, and text separated by the project logo in the middle of the screen on the smaller devices. The log in and register links should lead to the login page and the register page. | The homepage is loaded. Both links are clicked. | The elements behave correctly on all devices. |
| *Login/Register pages* | The user should be able to fill in the text input fields on the login/register pages and log in/register a new account upon clicking on the submit button. After that, the now logged in user should be taken to the Lists page. The links to the login/register pages should take the user to the right page upon clicking. | A registration attempt is made. A login attempt is made. The links on both pages are clicked. | The new account is registered successfully. The user is logged in successfully. The user is brought to the Lists page after clicking on the submit button in both cases. Both links work as intended. |
| *Not logged in page* | The page should appear each time the user tries to access one of the pages based on the base.html template - the inner app pages with the actual app content. The user should be taken to the login page upon clicking on the login button. | An attempt to access each page while logged out is made. The login button is clicked. | The redirects work as intended. The login button takes the user to the login page. |
| *Error pages* | An error 404 page should be displayed if the user tries to access a nonexisting page. An error 500 page should appear in case of an internal server error. The buttons on both error pages should take the user to the right place: the Lists page for the error 404 and the last page the user tried to access for the error 500. | A random string of characters is put in the address bar after the base address of the app. The link on the error 404 page is clicked. The route for the error 500 page is temporarily changed to allow to purposefully access the error page; the page is accessed. The link is clicked. |  Error 404 page works correctly. The link work correctly. The error 505 page was accessed purposefully, without a redirection from a page the user was trying to access, so it was not possible to test the actual behaviour of the page. The link takes the user to the homepage. |
| *New list button* | The 'new list' button should be displayed at the top. It should lead the user to the New list page upon being clicked. | The page is loaded. The button is clicked. | The button displays correctly. The user is led to the New list page. |
| *List display section* | The lists made by the user - if there are any - should be displayed on the page in the form of cards, grouped by the type of die they belong to. Empty groups should not be displayed. Each card should have the name on the list displayed on it on the left and the name of the assigned category, if the user decided to set one. If the assigned category had a colour, the card should be of that colour. The card should take the user to the List view screen upon being clicked. An animation moving the card slightly upwards should be triggered on hover. The card should return to the normal position when the user stops hovering cursos over it. | Cards are inspected. The user hovers the cursor over the cards. The cards are clicked. | The cards are displayed correctly. The on:hover animation works correctly. The user is taken to the List view page of the correct list after clicking on the card. |
| *New list page* | The six dice should be displayed in a grid: 2x3 on bigger screens, 3x2 on mobile devices. The entire container divs including the text and the picture for each die should be clickable. The user should be led to the Add list page of the right type after clicking on the dice container div. | The page is viewed on different devices. Each of the dice is clicked - both on the text and on the image. | The grid displays the dice correctly on different devices. The links work as intended. |
| *List name* | The name of the correct list should be displayed. | The page is loaded. | The name of the list is displayed correctly. The name displayed belongs to the correct list. |
| *List item cards* | There should be as many list items as the dice category indicated. Each item should have a fixed number assigned to it. The list items that have been given notes will be clickable, and have a notes icon displayed on the far right of their cards. Upon clicking on such card, the notes will be shown. They will be hidden again if the user clicks on the card again. | The page is loaded. The list item cards are clicked on. | The list items display correctly. The notes icon is displayed correctly. Only the cards with the notes icon are clickable and expand to show the notes section upon being clicked. |
| *Roll die functionality* | The Roll Die section should show the right kind of die for the list it represents. The entire section - both text and the die image - should be clickable. Upon being clicked, a div with the roll result should appear below the section and the card with the corresponding number should be highlighted in deep orange. Multiple clicks should bring varied results. | The page is loaded. The Roll Die section is hovered over. The section is clicked several times. | The right die image is loaded correcly. The entire section is clickable. The result div appears after the roll and the correct item list card is highlighted with the right colour. |
| *Task mode functionality* | The Task mode toggle should be shown below the list. The help icon should fire a tooltip message explaining the way task mode works when hovered over. The task mode should be activated upon clicking on the toggle. The toggle should stay toggled after the user refreshes the page. Rolling the die should now remember each die roll and only roll the next rolls from among the items that have not been rolled before. The items that have been rolled before should have their text greyed out after the card is no longer highlighted with deep orange. The list should be reset after the last list item has been rolled and the user tried to roll again. It should also reset when the user turns off the task mode. | The toggle is clicked on. The Roll Die button section is clicked on several times. The page is refreshed. The Roll Die section is clicked on some more, until the list resets. Then it is clicked on some more, and then the toggle is clicked on again. | The toggle behaves correctly. Its value is saved and only changes if the user toggles it. The task mode behaves correctly: it only rolls each item once and grays out the previously rolled items. It resets correctly. |
| *Back, edit list, delete list buttons* | The buttons should do what they say: bring the user back to the Lists page, to the Edit List page, and to the list deletion modal, respectively. | Each of the buttons is clicked. | The buttons do what they should do. |
| *List delete modal* | The List delete modal should appear on the screen and darken the rest of it when the delete list button is clicked. It should give the users an option to proceed and to go back. The modal should be hidden if the user chooses to cancel the operation; if they coose to proceed, the modal should disappear, the list should be deleted, and the user should be brought back to the Lists page. Clicking outside of the modal should close it. | The delete list button is clicked. Each link in the modal window is clicked. Clicking outside of the modal is performed, too. | The modal appears and disappears as it should. Both links work and do what they should do. |
| *List name - add/edit list pages* | The text field should accept text between 3-30 characters long. It should have a placeholder text saying "Name your list...". The name should be saved when the form is submitted. On the list edit page, the input field should be pre-populated with the current name. | Text that only has 2 characters is put in. Text that has 10 characters is put in. Text that has 31 characters is put in. The filled form is submitted. | The placeholder text is shown correctly. The field validation asks the user to make the text longer in case of 2 characters. It does not allow the user to put in more than 30 charaters. The name is saved and displays on the other pages properly. The input field is pre-populated with the current name on the list edit page. |
| *Add/change category* | Clicking on the paragraph should bring up the Materialize select dropdown menu. Another click on the paragraph should hide it. It should have the categories created by the user ready for the user to choose from. Picking one of the categories should set it when the form is submitted. On the edit page, the select element should show the current category as selected. | The paragraph is clicked on. An existing category is chosen. The list is saved. | The dropdown appears and disappears correctly. The category can be chosen on all the deviced except for the iPad, where the category before/after the tapped one gets selected. The issue persists in both Safari and Chrome. The selected category is saved and displays on the other pages correctly. The select element shows the current category as selected on the list edit page. |
| *List item input fields* | The right amount of fields, corresponding to the die number, should be generated. The fields should accept text up to 100 characters long. Leaving blank fields should prompt the form to ask the user to fill the missing ones. The list items should be saved and displayed successfully on the List view page. On the edit list page, the fields should be pre-populated with existing list items. | The fields are filled; an attempts is made to put in more than 100 characters. The form is submitted. | The fields stop the user from putting in more than 100 characters. The input fields are pre-populated on the list edit page. The list items are saved and displayed successfully. |
| *List note button* | The button should show an "Add notes..." tooltip message on hover. It should display a notes section directly underneath the corresponding list item input field when it is clicked, and hide the notes section if it is clicked again. The textarea should accept no more than 500 characters. The notes should be saved and ready to be viewed on the list view page when the form is submitted. Existing notes should be displayed and available to edit on the edit list page. | The button is hovered over, then clicked. The textarea id filled. An attempt is made to put in more than 500 characters. The button is clicked again. And again. The form is submitted. | The tooltip message displays properly. The notes section appears and disappears on click properly, keeping the contents put in by the user. The textarea does not allow the user to put in more than 500 characters. The notes are saved and can be viewed. The existing notes are available for editing. |
| *Cancel and save list/save changes buttons* | The cancel button should bring the user back to the Lists page (add list page) or the view list page (edit list page). The save list/changes button should write the information to the database and bring the user back to Lists page (add list page) or the view list page (edit list page). | Both buttons are clicked on both pages. | The buttons work as they should. |
| *Categories page* | The page should display the "add category" button on the top and a list of existing categories below it. The button should lead the user to the Add category page on click. The category cards should display the category name and the category colour, if it's been assigned. Each category card should lead the user to their edit page on click. | The "add category" button is clicked. The category cards are clicked. | The button and the cards display correctly. They lead the user where they're supposed to when clicked. |
| *Category name iput* | Should accept text between 3-30 characters long. Should show a placeholder text "Name the new category..." when creating a new category or the existing category name if editing caegory. Should be saved and ready to be viewed on other pages when the form is submited. | Text that only has 2 characters is put in. Text that has 10 characters is put in. Text that has 31 characters is put in. The filled form is submitted. | The placeholder text is shown correctly. The field validation asks the user to make the text longer in case of 2 characters. It does not allow the user to put in more than 30 charaters. The name is saved and displays on the other pages properly. The input field is pre-populated with the current name on the list edit page. |
| *Colour picker* | Should only allow user one selection at the time. The selected colour should be marked with a thicker, more intense border. The selection should be saved and the colour should still be picked with the thick border when the category is edited. | The colour is picked. The form is saved. The category is then edited. | The colour picker works properly. The state of the selection is saved for the future. |
| *Cancel, add category/save changes, and delete category buttons* | The Cancel button should bring the user back to the Categories page. The add category/save changes buttons should the same, plus - mainly - save the information to the database. The delete category button should trigger the category delete modal. | All of the buttons are clicked. | The buttons are working as they should. |
| *Category delete modal* | The category delete modal should appear on the screen and darken the rest of it when the delete category button is clicked. It should give the users an option to proceed and to go back. The modal should be hidden if the user chooses to cancel the operation; if they coose to proceed, the modal should disappear, the category should be deleted, and the user should be brought back to the Categories page. Clicking outside of the modal should close it. | The delete category button is clicked. Each link in the modal window is clicked. Clicking outside of the modal is performed, too. | The modal appears and disappears as it should. Both links work and do what they should do. |
| *User greeting* | The heading should display the user's name in a welcoming message. | The page is loaded. | The corrct name is correctly retrieved from the database and displayed. |
| *Dark mode toggle* | The toggle should immediately swap the colour scheme of the app once it's clicked. It should then stay in its new position until it is toggled to the "off" position again. The colour scheme should then change back to light. | The switch element is toggled. Then, the page is refreshed. Various pages are accessed. Then, the toggle is clicked once more. | The colour scheme changes correctly. The state of the toggle is retrieved and displayed correctly. |
| *Account deletion* | The paragraph should bring up the account deletion modal upon being clicked. The modal should give the users an option to proceed and to go back. It should be hidden if the user chooses to cancel the operation; if they coose to proceed, the modal should disappear, the account should be deleted, and the user should be brought to the login page. Clicking outside of the modal should close it. | The paragraph is clicked. | The modal appears and disappears as it should. Both links work and do what they should do. |

### Manual Testing: Testing User Stories from the UX/UI section of README.md

**1. First Time Visitor Goals**

* *As a first time visitor, I want to learn what the app is about.*

    * Accessing the app for the first time, the user is brought to the Homepage. The Homepage briefly describes the app and what it's useful for and invites the user to give it a go.

* *As a first time visitor, I want to create an account.*

    * The Homepage features a link to the Register page. The user can click on the link and easily create an account.

* *As a first time visitor, I want to create my first list.*

    * After a successful registration the user is brought to the Lists page. There aren't any lists there yet - just a big button encouraging the user to create one. The user clicks on the button, picks their die, fills in the necessary fields, and they save the list. They can now access it easily.

* *As a first time visitor, I want to create some categories for my lists.*

    * Seeing the navbar, the user notices the "Your categories" link. They click on it and they see a large "New category..." button. They click on the button, choose a name and a colour for their category, and create it.

**2. Returning Visitor Goals**

* *As a returning visitor, I want to log in to my account.*

    * The Homepage features a login link. After the user logs out, they get automatically redirected to the login page. If the user tried to access one of the pages that requires them to be logged in to see, they will get redirected to the Not Logged In page, which also has a link to the login page. Whichever way the user uses to access the login page, it will be easily found. The user can then log in to their account.

* *As a returning visitor, I want to use my lists.*

    * When the user logs in, they are brought to the Lists page where their lists can be viewed. The user clicks on the list they want to use and either uses it in combination with a physical die they roll in the real world, or - more likely - they use the Die Roll functionality of the app.

* *As a returning visitor, I want to edit and/or delete my lists.*

    * Already at the List view page, the user sees the list edit/delete buttons. The user clicks on the one they want and proceeds to edit/delete the list.

* *As a returning visitor, I want to edit and/or delete my categories.*

    * Wanting to edit and/or delete categories, the user goes to the Categories page. There, they can see their existing categories. They are clickable, so the user clicks on them. The user proceeds to edit or delete the category.

* *As a returning visitor, I want to try the Task Mode to use my list for one-off tasks that should be completed once and for all.*

    * Interacting with their list, the user notices the Task Mode toggle. They hover over or tap the help icon to learn about it, then switch the toggle on. They roll the die several times, ticking their tasks off the list, rolling a different result each time and seeing the past results being grayed out.

### Further Testing

The website has been tested on a variety of screen sizes (resizing the browser window on desktop, tablet, smartphones), browsers (Chrome, Safari Edge, Firefox), and devices. The results were pleasing; small adjustments have been made throughout the process. The only major problem found was the iOS issue wih the Materialize select element.

## Bugs fixed & problems overcome

| Problem description   |  Fix  |
| --------------------- | ----- |
| Materialize grid elements would sometimes fall out of order completely during working on the layout of the pages. While copying and pasting blocks of code, VS Code would sometimes add an unnecessary closing tag after the opening div tag of the copied block, which would close the div immediately and cause display issues. | The redundant closing </div> tags were found and deleted. |
| Materialize select element wouldn't work correctly on the iPad. Searching the internet revealed it's a common issue in iOS. | Downloaded an external script that solves the issue. |

Due to the nature of working with Python, any other issues were being corrected on the go the moment they arised - the application would throw an error and refuse to work whenever something was wrong - so they never got a chance to become bugs.