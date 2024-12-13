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

