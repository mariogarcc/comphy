def ask_continue():
    response = input("Continue? (y/n)\n")
    if response.lower() not in ('y', 'n'):
        return ask_continue()
    if response.lower() == 'n':
        return quit()
