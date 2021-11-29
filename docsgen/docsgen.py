import re

match_summary = re.compile(r'<summary>(.*)</summary>', re.DOTALL)
match_param = re.compile(r'<param name="(.*)" type="(.*)">(.*)</param>')
match_return = re.compile(r'<returns value="(.*)">(.*)</returns>')
match_example = re.compile(r'<example>(.*)</example>', re.DOTALL)

def load_template_file(template_file_path : str) -> str:
    '''
    <summary> Loads a template file and returns the contents as a string. </summary>

    <param name="template_file_path" type="str"> The relative path to the template file. </param>

    <returns value="str"> The contents of the template file. </returns>

    <example>
    ```python
    >>> print(load_template_file('templates/class.md'))
    # `class` {obj.__name__}

    {obj.__doc__.strip()}

    ## Methods

    {get_md_table_from_methods_list(methods_list, load_template_file('templates/table.md'))}
    ```
    </example>
    '''
    with open(template_file_path, 'r') as template_file:
        return template_file.read()

def get_methods_list(obj : object = None) -> list:
    '''
    <summary> Returns a list of methods of a class or module. </summary>

    <param name="obj" type="object"> The class to get the methods from. </param>
    <returns value="list"> A list of methods. </returns>

    <example>
    ```python
    >>> import module_interfacing
    >>> [method.__name__ for method in get_methods_list(module_interfacing)]
    ['format_doc', 'get_method_doc_values', 'get_methods_list', 'md_list_from_params_list', 'md_table_from_methods_list']
    ```
    </example>
    '''
    return [getattr(obj, x) for x in dir(obj) if callable(getattr(obj, x)) and not x.startswith("_")]


def get_method_doc_values(method) -> dict:
    '''
    <summary> Parse a method docstring for tags and return a dict of the corresponding values. </summary>

    <param name="method" type="function"> The method to retrieve the values from. </param>

    <returns value="dict"> A dictionary of the values. </returns>

    <example>
    ```python
    >>> method = get_methods_doc_values
    >>> get_method_doc_values(method)
    {
    \t'summary': 'parse a method docstring for tags and return a dict of the corresponding values.',
    \t'params': [('method', 'function', 'The method to retrieve the values from.')],
    \t'returns': [('dict', 'A dictionary of the values.')],
    \t'example': ...
    }
    ```
    </example>
    '''
    method_doc = method.__doc__
    summary = match_summary.search(method_doc)
    params = match_param.findall(method_doc)
    returns = match_return.search(method_doc)
    example = match_example.search(method_doc)

    summary = summary.group(1) if summary else ''
    return_type, return_summary = returns.group(1, 2) if returns else ('None', '')
    example = re.sub(' +', ' ', example.group(1)) if example else ''

    params_list = []
    for name, type, param_summary in params:
        params_list.append({
            'name': name,
            'type': type,
            'summary': param_summary
        })

    return {
        'name' : method.__name__, 
        'summary': summary,
        'params': params_list,
        'type': return_type,
        'return_summary': return_summary,
        'example': example
    }


def get_md_list_from_params_list(lst : list, template_str : str) -> str:
    '''
    <summary> Returns a markdown list from a list of parameters. </summary>

    <param name="lst" type="list"> The list of objects to convert to a markdown list. </param>
    <param name="template_file_path" type="str"> The relative path to the template file. </param>

    <returns value="str"> The markdown list as a string. </returns>

    <example>
    ```python
    # TODO
    ```
    </example>
    '''
    ret = ''
    for obj in lst:
        locals().update(obj)
        ret += eval(f'f"""{template_str}\n"""')
    return ret


def get_md_table_from_methods_list(methods_list : list, template_str : str) -> str:
    '''
    <summary> Returns a markdown table from a list of methods. </summary>

    <param name="methods_list" type="list"> The list of methods to convert to a markdown table. </param>
    <param name="template_file_path" type="str"> The relative path to the template file. </param>

    <returns value="str"> The markdown table as a string. </returns>

    <example>
    ```python
    # TODO
    ```
    </example>
    '''
    template_lines = template_str.split('\n')
    ret = '\n'.join(template_lines[:2]) + '\n'
    for obj in methods_list:
        locals().update(get_method_doc_values(obj))
        ret += eval(f'f"""{template_lines[2]}\n"""')
    return ret


def format_doc(obj, template_str, keywords : dict) -> str:
    '''
    <summary> Formats a docstring for a class or method by evaluating the template with the input keywords. </summary>

    <param name="obj" type="object"> The class or method to format the docstring for. </param>
    <param name="template_file" type="str"> The relative path to the template file. </param>
    <param name="keywords" type="dict"> The keywords to give to the scope of the template. </param>

    <returns value="str"> The formatted docstring. </returns>

    <example>
    ```python
    # TODO
    ```
    </example>
    '''
    locals().update(keywords)
    template = eval(f'f"""{template_str}"""')
    return template

if __name__ == '__main__':
    import sys, os

    sys.path.append(os.path.abspath('../'))

    module = sys.modules[__name__]
    module.__doc__ = 'A markdown template manager for writing python API docs'

    module_template = load_template_file('templates/module.md')
    method_template = load_template_file('templates/method.md')

    methods_list = get_methods_list(module)
    out = format_doc(module, module_template, {'methods_list': methods_list})
    for obj in methods_list:
        out += format_doc(obj, method_template, get_method_doc_values(obj))

    with open('output/out.md', 'w') as f:
        f.write(out)