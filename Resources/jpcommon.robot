*** Settings ***
Documentation    Browser preparations and ending
Library  SeleniumLibrary

*** Keywords ***
Begin Web Test
    open browser  about:blank  chrome
    maximize browser window

Nap
    Sleep  2s

Load
    Go to  https://www.jobsportal.fi
    wait until page contains  Contact us
    click element  //div[@class='cc-compliance']  #cookie agreement
    nap


End Web Test
    Close Browser

