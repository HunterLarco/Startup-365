# Error Codes

*api_description*

***

## Format

Any API request may result in an error. Each error follows the format

    {
      "code": error_code,
      "stat": "fail",
      "message": error_description
    }

***

## Codes and Messages

### Reserved API Codes

<table id="reserved_codes">
  <tr>
    <th>code</th>
    <th>message</th>
  </tr>
  <tr><td>-5</td><td>POST/GET Method Not Supported</td></tr>
  <tr><td>-4</td><td>Incorrect JSON Formatting</td></tr>
  <tr><td>-3</td><td>Parameter(s) Missing</td></tr>
  <tr><td>-2</td><td>Method Does Not Exist</td></tr>
  <tr><td>-1</td><td>Unspecified Method</td></tr>
  <tr><td> 0</td><td>Unknown Error</td></tr>
</table>