import random


def random_integer(request):
    data = {
        'integer': random.randint(0, 10),
    }

    return data

def crypto_random(request):
    r = random.SystemRandom()
    
    data = {
        'integer': r.randint(0, 10),
    }

    return data

def random_slice(request):
    if "string" not in request.session:
        request.session['string'] = ''.join(random.choice('01') for _ in range(1024))

    sample = random.sample(request.session['string'], 50)

    data = {
        'string_count_0': request.session['string'].count('0'),
        'string_count_1': request.session['string'].count('1'),
        'string': request.session['string'],
        'sample': sample,
        'sample_count_0': sample.count('0'),
        'sample_count_1': sample.count('1'),
    }

    return data

def nonrandom_slice(request):
    string = '0' * 750 + '1' * 250 # String of 750 zeroes and 250 ones.

    sample = random.sample(string, 50)

    data = {
        'string_count_0': 750,
        'string_count_1': 250,
        'string': string,
        'sample': sample,
        'sample_count_0': sample.count('0'),
        'sample_count_1': sample.count('1'),
    }

    return data
