with open('../../my_file.txt', mode='w') as file:
    file.write('I am trying to teach myself Python')

with (open('../../my_file.txt', mode='r')) as file:
    contents = file.read()
    print(contents)

with open('new_file.txt', mode='w') as file:
    file.write('I\'ve created this file using Python')

