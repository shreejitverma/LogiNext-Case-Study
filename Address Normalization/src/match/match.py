import jellyfish #  jellyfish is a library for approximate & phonetic matching of strings.


def similarity(input_string_1, input_string_2):
    return jellyfish.jaro_winkler(input_string_1, input_string_2)

