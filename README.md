# Greedy word wrap

```
wordwrap.py
```
Most text formatters pull in heavy dependencies or require a wall of config just to break a line. This one doesn't. It wraps text to a strict column width. It refuses to split words. Zero external packages.

Check the test suite next to the implementation. It shows exactly how the algorithm handles edge cases without hiding the logic.

We built this using strictly the Python standard library. No pip installs. No background services. No hidden network calls. You import it, call it, and move on. Time-to-first-wrap is basically zero.