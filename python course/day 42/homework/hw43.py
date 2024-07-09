answer0 = "yes"
answer1 = "no"
answer2 = "კი"
answer3 = "არა"
language0 = "ქართული"
language1 = "english"
input0 = input("hello, whats your name?:  ")
input1 = input("whats your surname?: ")
input2 = input("how old are you?:  ")
print("ok" + input0)
input3 = input(" can i make you laught?: ")

if input3 == answer0:
    input4 = input("on what language?: ")
    if input4 == language0:
      print("მოკლედ მიდიოდა ცხვარი და შეჭამეს")
      input5 = input("კიდე გინდა?: ")
      if input5 == answer2:
            print("კახელი ყიდს ხორცს, რუსი მიდის და ამბობს: ეტა მიასა? კახელი პასუხობს: რა უნდა მიაფსა გამო აქეთ")
            input6 = input("კიდევ გინდა ხუმრობა?:  ")
            if input6 == answer2:
                print("მიდიოდა და ბოძს დაეჯახა, სამწუხაროდ გარდაიცვალა")
            elif input6 == answer3:
             print("კარგი, კარგად")
      elif input5 == answer3:
             print("კარგი, კარგად")
    elif input4 == language1:
          print("for short, sheep went to the walk and they ate it")
elif input3 == answer1:
          print("ok, bie")
