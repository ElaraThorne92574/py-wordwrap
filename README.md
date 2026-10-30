# Greedy word wrap

```
wordwrap.py
```
Look at the tests next to the implementation. They show the exact edge cases.

Most wrapping tools pull in massive dependency trees. This one does not. It wraps text to a strict column width. It keeps words intact. Time to first call is basically zero.

We only use the standard library. Zero dependencies. Zero config files. Just import the module and call the function.