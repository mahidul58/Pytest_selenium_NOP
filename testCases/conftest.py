import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
   # browser == 'chrome':
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='edge':
        driver = webdriver.Edge()
    print("Launching firefox browser.........")


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
 return request.config.getoption("--browser")

########### pytest HTML Report ################
# It is hook for Adding Environment info to HTML Report
#def pytest_configure(config):
    #config._metadata['Project Name'] = 'nop Commerce'
    #config._metadata['Module Name'] = 'Customers'
   # config._metadata['Tester'] = 'Pavan'
 def pytest_configure(config):
     config._metadata = {
         "Project Name": "Pytest_selenium_NOP",
         "Module Name": "Customers",
         "Tester": "Mahidul Islam"
     }



# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




