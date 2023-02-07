from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest


@pytest.fixture(autouse=True, scope="class")
def setup(browser, request):
    if browser == "edge":
        edge_options = EdgeOptions()
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
        edge_options.add_argument("--headless")
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        firefox_options.add_argument("--headless")
    else:
        chrome_options = ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        chrome_options.add_argument("--headless")
    request.cls.driver = driver

    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# Customization of the html report title
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Ebay Test Cases Report"


# Customization of the html report environment section
def pytest_configure(config):
    config._metadata['Project Name'] = 'Ebay automation in Python Selenium'
    config._metadata['Tester'] = 'Charline'
