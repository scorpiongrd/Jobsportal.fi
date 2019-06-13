*** Settings ***
Documentation  This is some basic information
Library  SeleniumLibrary


*** Variables ***



*** Test Cases ***
[Documentation]
Open Browser  http://www.jobsportal.fi  chrome
Sleep  3s
Close Browser




*** Keywords ***
