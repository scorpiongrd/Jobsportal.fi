*** Settings ***
Documentation  Check major links
Resource  ../Resources/jpcommon.robot
Resource  ../Resources/jpapp.robot
Test Setup  Begin Web Test
Test Teardown  End Web Test

*** Variables ***



*** Test Cases ***
Show all jobs
    jpcommon.Load
    jpapp.Show all jobs by location
    jpapp.Show all jobs by company
    jpapp.Show all jobs by role



