def redact_ex(ex_str, n = '', sep = '\n', end = '\n\n'):
    print('', 'EXERCISE {no}:'.format(
        no = int(n) if not isinstance(n, str) else n), ex_str,
        sep = sep, end = end)
    return None