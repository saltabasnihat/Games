def vowel_counter(input):
    vowels = ['a','e','u','i','o','E','A','U','O','I']
    num_vow = 0;

    for i in input:
        if i in vowels:
            num_vow += 1
    return num_vow

