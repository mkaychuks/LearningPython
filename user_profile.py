# Using Arbitrary Keyword Arguments

'''Sometimes you’ll want to accept an arbitrary number of arguments,
but you won’t know ahead of time what kind of information
will be passed to the function.'''


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Odogwu', 'Umunya',
                             location='princeton', field='physics')

print(user_profile)
