Metamorphosis: Eric, Yuki, Maya
Softdev
2022 10 17
Time spent: 0.6 hr

DISCO:
* when using ```request.form``` with a post request, sensitive information such as passwords and usernames inputted into the query string is hidden. Just the route is shown. 
* to initiate a post request, you have to edit the front end of the code.
    ```
    <form action="/auth", method = "POST">
      <input type="text" name="username">
      <input type="submit" name="sub1">
    </form>
    ```
* ```request.args``` and ```request.form``` are mutually exclusive.

QCC:
