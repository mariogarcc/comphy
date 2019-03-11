def redact_ex(ex_str, n, sep = '\n', end = '\n\n'):
    print('', 'EXERCISE {no:d}:'.format(no = int(n)), ex_str,
        sep = sep, end = end)
    return None