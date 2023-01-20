#pierwsze rozwiazanie
'''
def response(hey_bob):
    if hey_bob == "":
        return "Fine. Be that way!"
    elif "?" in hey_bob and hey_bob.endswith(' ') or (hey_bob.endswith('?') and not hey_bob[1:5].isupper() or hey_bob.islower() and not "." in hey_bob):
        return "Sure."
    elif hey_bob[-1] == '?' and hey_bob[-2].isupper():
        return "Calm down, I know what I'm doing!"

    elif hey_bob.endswith('!') and hey_bob[0:2].isupper() or (hey_bob.endswith('!') and hey_bob[-3:-2].isupper()) or hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.endswith('.') or hey_bob.endswith('!') or (hey_bob[0:2].isalnum() and hey_bob.endswith(' ')) or hey_bob[0].isalnum():
        return "Whatever."
    else:
        return "Fine. Be that way!"
'''
def response(hey_bob):
    hey_bob = str(hey_bob.strip())
    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif not hey_bob:
        return "Fine. Be that way!"
    else:
        return "Whatever."


# Bob answers 'Sure.' if you ask him a question, such as "How are you?".
#
# He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
#
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
#
# He says 'Fine. Be that way!' if you address him without actually saying anything.
#
# He answers 'Whatever.' to anything else.