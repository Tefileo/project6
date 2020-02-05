# Assignment 2 for post class
# define an empty dictionary
# name_dict = {}
# Prompt user for input for a story.
# it should have:
# hero, beginning, middle, end
# 2 other things you define to be part of the story.
# add each response to the dictionary under an appropriate key

dictionary = {}

beginning = input('Please input your story begining: ')
dictionary.update({'beginning':beginning})

middle = input('Please input your story middle: ')
dictionary.update({'middle':middle})

end = input('Please input your story end: ')
dictionary.update({'end':end})

story_Title = input('Please input story Title: ')
dictionary.update({'story_Title':story_Title})

dedicated = input('Please input a person to dedicate the story to: ')
dictionary.update({'dedicated':dedicated})

print(dictionary)