import random

from constants.EncodingChart import EncodingChart

def makePrompt(length=1):
    prompt=""
    for i in range(0,length):
        prompt+=chr(int(random.random()*26)+65)
    return prompt

def makePromptMorse(chars=1):
    return EncodingChart[makePrompt(chars)]



