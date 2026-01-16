 Feature: Adding to Target cart
 Scenario: Adding and verifying target cart
   Given Open Target main page
   When Search for Playstation 5
   Then Search results for Playstation 5 are shown
   When Click first result
   When Click Add to cart on sidebar
   When Close Sidebar
   When Click on cart icon
   Then Verify Playstation 5 is added to cart

