

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for tea
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify product in cart is correct