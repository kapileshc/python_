import random

def get_file_extension(filename):
    return filename[filename.index('.')+1:]

def roll_dice(num):
    return random.randint(1,num)
