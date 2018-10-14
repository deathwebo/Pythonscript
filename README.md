# Pythonscript
A Python-to-Javascript focused on using JS in Python.

This transpiler NEVER can run Python code. It directly
transpiles into Javascript code. So basically you're
writing Javascript in Python. For example, you have
Python(script) code like this:

```python
a = [1, 'hi', 'pythonscript']
```

When you transpile it using Pythonscript it will generate
code like this:

```js
var a = [1, 'hi', 'pythonscript'];
```

So technically you can't use Python code in it. Pythonscript
makes you able to create JS bindings in Python. It's still
work-in-progress (WIP). So help me to devolop it faster
with sending pull requests!
