# DocsGen-py

A markdown template manager for writing API docs in python.

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