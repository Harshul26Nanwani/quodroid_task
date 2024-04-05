*** Settings ***
Documentation       Custom Script Started
Library             RPA.Browser.Selenium
*** Tasks ***
Open google.com
    Open Browser    browser=chrome
    Go To    url=https://google.com
