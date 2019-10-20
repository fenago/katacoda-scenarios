The WebElement that is obtained can be accessed for the following properties and general methods, as well as many more:

- **get_attribute():** This returns the attribute value for the key argument provided, such as value, id, name, and class.
- **tag_name: This returns the HTML tag name of a particular WebElement.
- **text:** This returns the text of the WebElement.
- **clear():** This clears the text of HTML form elements.
- **send_keys():** This is used to fill with text and provide the key effect, such as pressing ENTER, BACKSPACE, and  DELETE, available from the selenium.webdriver.common.keys module in selenium.webdriver.common to the HTML form elements.
- **click():** This performs the clicking action to the WebElement. This is used for HTML elements such as Submit Button.

In the following code, we will be using the functions and properties listed previously in searchBox:

```
print("Type :",type(searchBox))
<class 'selenium.webdriver.remote.webelement.WebElement'>

print("Attribute Value :",searchBox.get_attribute("value")) #is empty
Attribute Value : 

print("Attribute Class :",searchBox.get_attribute("class"))
Attribute Class : search_query form-control ac_input

print("Tag Name :",searchBox.tag_name)
```

