 import emoji

  # Using CLDR short names (replace spaces with underscores)
  print(emoji.emojize(":grinning_face_with_big_eyes:"))
  print(emoji.emojize("I love Python :green_heart:"))

  # Converting emojis back to short names
  print(emoji.demojize("I love Python ❤️"))