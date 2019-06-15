*** Settings ***
Library  SeleniumLibrary
Documentation  Check major links
Library  ../Library/WebLibrary.py
Library  ../Library/Common.py

*** Variables ***



*** Test Cases ***
Show jobs by clicking links in footer
    open browser and load homepage
    accept cookie
    verify user can access jobs by all locations in footer  #jobs by location
    verify user can access jobs by all companies in footer  #jobs by company
    verify user can access jobs by all keywords in footer  #jobs by keywords
    end web test

