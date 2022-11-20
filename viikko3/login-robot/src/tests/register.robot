*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  heikki  heikki1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  h  heikki1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  heikki  h
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password # Containing Only Letters
    Input Credentials  heikki  heikkiheikkiheikki
    Output Should Contain  Only letters not allowed

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command