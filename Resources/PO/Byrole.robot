*** Settings ***
Documentation    Show all jobs selected by role
Library  SeleniumLibrary
Resource  Resources/jpcommon.robot

*** Keywords ***
Python jobs
    click element  xpath=/html/body/footer/div/div[1]/div[3]/fieldset/ul/li[1]/a
    nap
