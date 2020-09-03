Among many other use cases, selenium is helpful for scraping "hard to scrape" websites. It allows you to open a web browser instance and automate actions to be performed on that browser. Some websites require "clicks" to get to data vs simply going through the URL, so in these cases Selenium is critical. 

## Getting Started
- To run selenium you need to download a web driver. Instructions & links to drivers can be found [here](https://selenium-python.readthedocs.io/installation.html#drivers). Note that you need to move the driver to your `usr/local/bin` or add the `executable_path=path/to/driver.exe` argument to the call to the driver's constructor (here, `webdriver.Chrome()`.)

## Website Authentication
If you're scraping from a website that requires authentication, it's useful to store your cookies so that you don't have to enter the auth information every time that you start a new driver instance. There are two easy ways to store credentials. The first option is to manually begin a new session, enter the credentials, and save the cookies to a file. To complete this process, follow these instructions: 

- Open a terminal python session by entering `python3` into the terminal.
- Copy and paste all the imports from the `scrape.py` file.
- Execute `driver = webdriver.Chrome()` and then `driver.get("DESIRED URL")`.
- Login.
- Execute `pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))`
- Execute `driver.close()`. 

If you'd rather the process be fully automated you can store the credentials locally in a file named `.env` (in the format seen in `envtemplate` in this repo.) Then, include a call to `utils.setup()` in your main. You'll have to add the arguments (which will require some sleuthing of the HTML to select the username & password elements correctly.)

## Tips
- To debug when using selenium it's often easiest to open a python session in the terminal (just type python3 and copy/paste all the imports), and then enter the commands or the functions you're dubugging chunk by chunk. You can watch them execute and see where the issues are.
- You'll need to use the "inspect page" function of your web browser in order to extract the specific bits of information you want from a given webpage. IMO chrome has much better interface for this than safari.
- For pages with super messy HTML, a more intensive parser such as BeautifulSoup might be necessary. They can be used together easily just by calling `html = BeautifulSoup(driver.page_source, "html.parser")`.

## Beyond
This guide should help you get up and running with selenium and easily authenticate into a website. Now, the scraping should (hopefully!) be the easy part. Seleniumn is great for things like clicking on links or buttons, navigating a website, and utimately finding the information. The documentation can be found [here](https://www.selenium.dev/selenium/docs/api/py/api.html) and a really helpful walkthrouhg that includes details about navigating pages, locating elements, and using waits is [here](https://selenium-python.readthedocs.io/navigating.html). 