def umciresi():
    question0 = int(input("please enter number: "))
    question1 = int(input("please enter number: "))
    if question0 < question1:
        return(question0)
    elif question1 < question0:
        return(question1)