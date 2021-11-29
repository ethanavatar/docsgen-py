# `module` docsgen

A markdown template manager for writing python API docs

## Methods

| Name | Summary |
| ---- | ---- |
| format_doc -> `str` |  Formats a docstring for a class or method by evaluating the template with the input keywords.  |
| get_md_list_from_params_list -> `str` |  Returns a markdown list from a list of parameters.  |
| get_md_table_from_methods_list -> `str` |  Returns a markdown table from a list of methods.  |
| get_method_doc_values -> `dict` |  Parse a method docstring for tags and return a dict of the corresponding values.  |
| get_methods_list -> `list` |  Returns a list of methods of a class or module.  |
| load_template_file -> `str` |  Loads a template file and returns the contents as a string.  |
### `str` format_doc(obj : `object`, template_file : `str`, keywords : `dict`)

 Formats a docstring for a class or method by evaluating the template with the input keywords. 

#### Returns

 The formatted docstring. 

#### Parameters

 - obj : `object` -  The class or method to format the docstring for. 
 - template_file : `str` -  The relative path to the template file. 
 - keywords : `dict` -  The keywords to give to the scope of the template. 



#### Example


 ```python
 # TODO
 ```
 ### `str` get_md_list_from_params_list(lst : `list`, template_file_path : `str`)

 Returns a markdown list from a list of parameters. 

#### Returns

 The markdown list as a string. 

#### Parameters

 - lst : `list` -  The list of objects to convert to a markdown list. 
 - template_file_path : `str` -  The relative path to the template file. 



#### Example


 ```python
 # TODO
 ```
 ### `str` get_md_table_from_methods_list(methods_list : `list`, template_file_path : `str`)

 Returns a markdown table from a list of methods. 

#### Returns

 The markdown table as a string. 

#### Parameters

 - methods_list : `list` -  The list of methods to convert to a markdown table. 
 - template_file_path : `str` -  The relative path to the template file. 



#### Example


 ```python
 # TODO
 ```
 ### `dict` get_method_doc_values(method : `function`)

 Parse a method docstring for tags and return a dict of the corresponding values. 

#### Returns

 A dictionary of the values. 

#### Parameters

 - method : `function` -  The method to retrieve the values from. 



#### Example


 ```python
 >>> method = get_methods_doc_values
 >>> get_method_doc_values(method)
 {
 	'summary': 'parse a method docstring for tags and return a dict of the corresponding values.',
 	'params': [('method', 'function', 'The method to retrieve the values from.')],
 	'returns': [('dict', 'A dictionary of the values.')],
 	'example': ...
 }
 ```
 ### `list` get_methods_list(obj : `object`)

 Returns a list of methods of a class or module. 

#### Returns

 A list of methods. 

#### Parameters

 - obj : `object` -  The class to get the methods from. 



#### Example


 ```python
 >>> import module_interfacing
 >>> [method.__name__ for method in get_methods_list(module_interfacing)]
 ['format_doc', 'get_method_doc_values', 'get_methods_list', 'md_list_from_params_list', 'md_table_from_methods_list']
 ```
 ### `str` load_template_file(template_file_path : `str`)

 Loads a template file and returns the contents as a string. 

#### Returns

 The contents of the template file. 

#### Parameters

 - template_file_path : `str` -  The relative path to the template file. 



#### Example


 ```python
 >>> print(load_template_file('templates/class.md'))
 # `class` {obj.__name__}

 {obj.__doc__.strip()}

 ## Methods

 {get_md_table_from_methods_list(methods_list, load_template_file('templates/table.md'))}
 ```
 