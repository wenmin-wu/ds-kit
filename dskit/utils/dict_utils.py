def deep_get(data: dict, path: str, default=None) -> object:
    path_parts = path.split('.')

    current = data
    if isinstance(current, dict) is False:
        return default

    for path_part in path_parts:
        if path_part in current:
            current = current[path_part]
        elif path_part.lstrip('-').isdigit() and int(path_part) in current:
            current = current[int(path_part)]
        else:
            return default
    return current


def deep_set(data: dict, path: str, value: object) -> None:
    path_parts = path.split('.')
    if isinstance(data, dict) is False:
        return
    current = data

    for idx, part in enumerate(path_parts):
        if idx == len(path_parts) - 1:
            current[part] = value
        elif part in current:
            current = current[part]
        elif part.lstrip('-').isdigit() and int(part) in current:
            current = current[int(part)]
        else:
            return