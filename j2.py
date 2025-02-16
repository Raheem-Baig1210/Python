def mood_to_emoji(a):
    if a=="happy":
        return ":D"
    elif a=='sad':
        return ':('
    elif a=="surprised":
        return ':O'
    elif a=="excited":
        return '^_^'
    elif a=='frustrated':
        return ">_<"
    elif a=="crying":
        return "T_T"
    else:
        return "please give me a correct mood"
a=input("Enter your mood: ")
print(mood_to_emoji(a))
