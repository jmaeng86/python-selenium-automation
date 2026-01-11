# Created by maeng at 1/8/2026
Feature: Verify Messages


  Scenario: User can see cart is empty
    Given Open target.com
    When Click on Cart icon
    Then Verify Your cart is empty message is shown



  Scenario: logged out user can sign in
    Given Open target.com
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened