"-----------day 8 challenge--------------------------------"
print("Welcome to the daily affirmation generator")
print("------------------------------------------\n")
name = input("enter your name ")
week = input("enter the day of the week ")
song = input("enter your favourite song ")
place = input("enter you favourite place ")
if week == "sunday" or week == "Sunday":  ########################################
  print()
  print(f"ok so today is {name}'s home alone.")
  print("enjoy the song", song, "at his favourite place", place)
  weight = int(input("what's your weight?🤔🤔 "))
  if weight >= 50 and weight <= 100:
    print("\033[33m", "hey be carefull with the food you eating.🫡👍", "\033[0m")
  elif weight > 100:
    print(
        "\033[31m",
        "today is holiday let's focus on how we can get you to that dam two degits",
        "\033[0m")
  else:
    print("\033[32m", "you can enjoy the food 😎😎", "\033[0m")
elif week == "monday" or week == "Monday":  #######################################
  print()
  print("ok so today is", name, " at workplace")
  print("enjoy the song", song, "at his workplace")
  print("but he always wish in breaktimes he will visit", place)
  job = input("do you really love your job?🤔🤔 (answer must be yes or no)\n")
  if job == "yes" or job == "Yes":
    print("\033[32m", "hey that's great i wish you do well there ❤️",
          "\033[0m")
  else:
    print(
        "\033[34m",
        "No worry i hope you are doing hard work and i hope some day you shall get you favourite workplace",
        "\033[0m")
elif week == "tuesday" or week == "Tuesday":  #######################################
  print()
  print("ok so today is", name, " at workplace")
  print("today you must manage the time to go at", place)
  print("make sure to hear", song, "while travelling")
  status = input("are you single? 🤔🤔(answer must be yes or no)\n")
  if status == "yes" or status == "Yes":
    print("\033[32m", "ok so the dude is focusing on big money 😎😎👌", "\033[0m")
  else:
    print("\033[31m", "i am jelous of you 😒😢👍👍👍", "\033[0m")
elif week == "wednesday" or week == "Wednesday":  #######################################
  print()
  print("ok so today is", name, " at workplace")
  print("today you must manage the time to go at", place)
  print("make sure to hear", song, "while travelling")
  money = input(
      "do you received this month saliry? 🤔🤔(answer must be yes or no)\n")
  if money == "yes" or money == "Yes":
    print("\033[32m", "congrats let's have a party 🥳🥳🥳🥳", "\033[0m")
  else:
    print("\033[31m", "no worry money is on it's way 👍👍🫡", "\033[0m")
elif week == "thursday" or week == "Thursday":  #######################################
  print()
  print("ok so today is", name, " at workplace")
  print("today you must manage the time to go at", place)
  print("make sure to hear", song, "while travelling")
  season = input("which season is going on? 🤔🤔")
  if season == "summer" or season == "Summer":
    print(
        "\033[32m",
        "bro please do not where tight cloths\nmost important have cold drinks per 1 hour👍",
        "\033[0m")
  elif season == "winter" or season == "Winter":
    print("\033[32m",
          "bro where 2 or 3 cloths at one time\nhave hot tea per 1 hour👍",
          "\033[0m")
  elif season == "rainy":
    print("\033[32m", "good seasson, make sure to wear raincoat👍", "\033[0m")
  else:
    print("\033[32m", "good season, make sure to have outdoor party👍",
          "\033[0m")
elif week == "friday" or week == "Friday":  #######################################
  print()
  print("ok so today is", name, " at workplace")
  print("today you must manage the time to go at", place)
  print("make sure to hear", song, "while travelling")
  game = input(
      "which types of games you like to play?\ni mean indoor or outdoor? 🤔🤔")
  if game == "indoor" or game == "Indoor":
    print(
        "\033[32m",
        "hey buddy i also like indoor game. let's play together. getting my xbox at your home🥳🥳😍😍",
        "\033[0m")
  else:
    print(
        "\033[32m",
        "hey buddy i also like outdoor game. let's play together. getting my bike at your home🥳🥳😍😍",
        "\033[0m")
  print("have a good day👍👍")
elif week == "saturday" or week == "Saturday":  #######################################
  print()
  print("ok so today is", name, " at workplace")
  print("today you must manage the time to go at", place)
  print("make sure to hear", song, "while travelling")
  status = input("are you single? 🤔🤔(answer must be yes or no)\n")
  if status == "yes" or status == "Yes":
    print("\033[32m", "ok so the dude is focusing on big money🤑🤑🤑", "\033[0m")
  else:
    print("\033[31m", "i am jelous of you😒👍👍", "\033[0m")
  print("\n👍👍have a good day")
else:
  print()
  print(
      "\033[031m",
      "you haven't entered the correct day of the week\nIN ORDER TO GET affirmation MESSAGES (make sure your input must be name of day in weeks 😥😥",
      "\033[0m")
