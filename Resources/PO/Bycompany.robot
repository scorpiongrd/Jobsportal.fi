*** Settings ***
Documentation  Show all jobs in selected company
Library  SeleniumLibrary
Resource  Resources/jpcommon.robot

*** Keywords ***
Nokia
    Click element  xpath=/html/body/footer/div/div[1]/div[2]/fieldset/ul/li[1]/a
    nap
