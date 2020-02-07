directions = ('north', 'south', 'east', 'west')
verbs = ('go',  'kill', 'eat')
stops = ('the', 'in', 'of')
nouns = ('bear', 'princess')
def scan(inputs):
    words = inputs.split()
    result = []
    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        else:
            try:
                result.append(('number', int(word)))
            except ValueError:
                result.append(('error', word))
    return result
