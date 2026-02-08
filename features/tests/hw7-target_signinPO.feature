# Created by maeng at 2/3/2026
Feature: Verify Logged out user can access sign in


  Scenario: User can see cart is empty
    Given Open target.com
    When Click Sign in
    And Click Sidebar sign in
    Then Verify Your cart is empty message is shown