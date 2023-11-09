import random
from static.EncodingChart import EncodingChart


def makePromptText(length=1):
    prompt = ""
    for _ in range(0, length):
        prompt += chr(int(random.random()*26)+65)
    return prompt


def makePromptMorse(chars=1):
    promptText = makePromptText(chars)
    prompt = []
    for c in promptText:
        prompt.extend(EncodingChart[c])
    return prompt
