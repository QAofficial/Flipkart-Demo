*** Settings ***
Library    BuiltIn
Library    SeleniumLibrary

*** Variables ***
${URL}    https://robotframework.org

*** Test Cases ***
Open Robot Framework Website
    [Documentation]    Open Robot Framework website and check title
    Open Browser    ${URL}    chrome
    Title Should Be    Robot Framework
    Close Browser

Hello World Test
    [Documentation]    Simple log message
    Log    Hello from Robot Framework!
