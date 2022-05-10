# DocsGen-py

A template engine for python with an API that helps make documentation

# Contents

 - [Usage](#usage)
 - [API Reference](/output/out.md)

# Usage

You can install the latest commit of this repo with:
```bash
$ python3 -m pip install git+https://github.com/ethanavatar/docsgen-py.git
```

This module's core functionality is that it interprets file contents as f-strings. This means you can use almost any arbitrary python expression in your input files by wrapping it in `{}`. This can be used with virtually any input format, but it is probably most useful for managing markdown templates.

Suppose a file called `example.md` that contains:
```markdown
# {name}
{summary}
```

Heres an example of how you can interact with this file.
```python
from docsgen import docsgen

with open('example.md', 'r') as f:
    template = f.read()

keywords = {
    'name': 'DocsGen',
    'summary': 'A markdown template manager for writing API docs in python.'
}

out = docsgen.format_doc(template_str=template, keywords=keywords)
print(out)
```

Running the code above will print:
```markdown
# DocsGen
A markdown template manager for writing API docs in python.
```

It doesnt end with keywords. You can put almost any valid python expression in the braces.

For example, you can execute a function that is local to the module you are using to generate the docs:

`example2.md`
```markdown
# {makeUpper(name)}
{summary}
```

```python
from docsgen import docsgen

def makeUpper(s):
    return s.upper()

with open('example2.md', 'r') as f:
    template = f.read()

keywords = {
    'name': 'DocsGen',
    'summary': 'A markdown template manager for writing API docs in python.'
}

out = docsgen.format_doc(template_str=template, keywords=keywords)
print(out)
```

The code above will print:
```markdown
# DOCSGEN
A markdown template manager for writing API docs in python.
```

The package comes with a few built-in functions that can be used in your templates to make things like tables and lists. See [API Reference](/output/out.md) for more details.
