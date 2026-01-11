# Created by maeng at 1/11/2026
Feature: Help page

  Scenario: Identify elements on help page
    Given Open Target help page
    Then Verify Help text appears at header
    Then Verify Have a question
    Then Verify Browse all help
    Then Verify Help Search Bar
    Then Verify What would you like help with
    Then Verify all elements within grid
    Then Verify Popular title text
    Then Verify All popular pages
