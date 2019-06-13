*** Settings ***
Resource  Resources/PO/Bylocation.robot
Resource  Resources/PO/Bycompany.robot
Resource  Resources/PO/Byrole.robot


*** Keywords ***
Show all jobs by location
    Bylocation.Helsinki
    Bylocation.Espoo

Show all jobs by company
    Bycompany.Nokia

Show all jobs by role
    Byrole.Python jobs



