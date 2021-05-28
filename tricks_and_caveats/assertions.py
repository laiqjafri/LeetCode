counter = 1

# The following assert will never fail unless we remove the parenthesis. The parenthesis make the compiler think that
# the argument is a tuple
# When you pass a tuple as a first argument in an assert statement, the assertion always evaluates to true and
# therefore never fails
assert (
    counter == 10,
    'It should have counted all the time'
)

assert (1 == 2, 'This should fail')

assert False, 'This will be raised as an error'
