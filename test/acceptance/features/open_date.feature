Feature: Conditional opening of slots by date
    When the user selects a year for an advent calendar only certain slots will be opened with the date's slot openable

Scenario: Opening an empty slot before its respective date
    Given: I have a slot without text or an image for date 12/01/2023
    And: The current date is 11/29/2023
    When: I try to open the slot
    Then: The slot should stay closed and present the failure popup

Scenario: Opening a filled slot before its respective date
    Given: I have a slot with text "too early" for date 12/01/2023
    And: The current date is 11/29/2023
    When: I try to open the slot
    Then: The slot should stay closed and present the failure popup

Scenario: Opening an empty slot on its respective date
    Given: I have a slot without text or an image for date 12/01/2023
    And: The current date is 12/01/2023
    When: I try to open the slot
    Then: The slot should open and display an empty tile

Scenario: Opening a filled slot on its respective date
    Given: I have a slot with text "on time" for date 12/01/2023
    And: The current date is 12/01/2023
    When: I try to open the slot
    Then: The slot should open and display text "on time"

Scenario: Empty slot after its respective date
    Given: I have a slot without text or an image for date 12/01/2023
    And: The current date is 01/01/2024
    Then: The slot should automatically be opened and display an empty tile

Scenario: Filled slot after its respective date
    Given: I have a slot with text "too late" for date 12/01/2023
    And: The current date is 01/01/2024
    Then: The slot should automatically be opened and display an empty tile
