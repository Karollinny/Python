def do_twice(f, numero):
    f() + numero
    f() + numero

def print_spam(numero):
    print_spam('spam' + numero)

do_twice(print_spam, 3)
