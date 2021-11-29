### `{type}` {obj.__name__}({", ".join([f'{param["name"]} : `{param["type"]}`' for param in params])})

{summary}

#### Returns

{return_summary}

#### Parameters

{get_md_list_from_params_list(params, load_template_file('templates/list.md'))}


#### Example

{example}