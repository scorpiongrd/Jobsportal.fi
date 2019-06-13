*** Settings ***
Documentation    Show all jobs in selected location
Library  SeleniumLibrary
Resource  Resources/jpcommon.robot

*** Keywords ***
Helsinki
    click element  xpath=/html/body/footer/div/div[1]/div[1]/fieldset/ul/li[1]/a
    nap
Espoo
    click element  xpath=/html/body/footer/div/div[1]/div[1]/fieldset/ul/li[2]/a
    nap