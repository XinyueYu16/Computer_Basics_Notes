*PEP8：https://www.python.org/dev/peps/pep-0008/#code-lay-out*

Things I learnt:

- **Names:** DONT PUT CAPTALIZED WORDS TOGETHER WITH UNDERSCORES!

- **Underscores:** The usage of **\_first_underscore**(for the unpublic), **\__double_underscore**(for the name mangling in a basic class, where you don't want a same-spelling variable overriding it. It turns foo.\_\_alias to foo.\_foo\_\_alias), **a\_tracing\_underscore\_**(where you don't want to override basic names in Python neither a spelling corruption).
- **Line-Length:**  **79** for codes; **72** for docstrings/comments.
- **Clean Indentation:** Except the case that your indentation would align with the opening delimiter, don't leave your parameters *hanging* in the first line.
- **Blank Lines:** **2 for top-level functions & classes**, 1 for method definitions inside a class or logical sections, 0 for one-liners.
- **Commas:** If you closing delimiter would be on its own in another line, keep the commas; otherwise leaving a trailing commas doesn't make sense.
- **Spacing:** No surrounding spacing for assigning parameters, but do have those when you create a default value for parameters...
- **Function Returns:** Pls return **None** if you want to leave a lonely return, there.
- **Except:** Always Except Exceptions or more specific (one of the sake is of your Keyboard Interruption), and you can put finally afterwards like **try...except..finally**. But don't have flow controllers like **return/break/continue** in finally.
- **WITH**: Use it when you want something to be crisply done without ashes. Like a transaction connection or reading a file.
- **Comparison:** 
  - **Don't** compare a boolean like True == True;
  - **Don't** compare a variable(undecided type) using if variable;
  - **Do** use if A is not None;
  - **Do** use if sequence_a to check if it's empty.

