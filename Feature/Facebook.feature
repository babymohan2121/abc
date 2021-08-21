Feature:validating the facebook login page with valid data,invalid data

  Scenario Outline:validate login page with valid data
    Given open browser as "<BROWSER>"
    When enter facebook url as "<URL>"
    When enter username as "<USERNAME>"
    When enter password as "<PASSWORD>"
    When click login button
    Then verify the user logged successfully

    Examples:
      | BROWSER |           URL             |         USERNAME               |  PASSWORD  |
      | chrome  | https://www.facebook.com/ | mohanjayavelmasc2016@gmail.com | 7010134741 |