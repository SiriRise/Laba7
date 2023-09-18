class LexemeFinder:
    def __init__(self, s):
        self.s = s
        self.vowels = set('аеёиоуыэюя')
        self.max_consonants = -1
        self.max_lexemes = []

    def is_vowel(self, c):
        return c in self.vowels

    def has_consecutive_vowels(self, seq):
        for i in range(len(seq) - 1):
            if self.is_vowel(seq[i]) and self.is_vowel(seq[i + 1]):
                return True
        return False

    def count_odd_positioned_consonants(self, seq):
        count = 0
        for i in range(0, len(seq), 2):
            if not self.is_vowel(seq[i]):
                count += 1
        return count

    def lexico_permute_string(self):
        a = sorted(self.s)
        n = len(a) - 1

        while True:
            if not self.has_consecutive_vowels(a):
                lexeme = ''.join(a)
                odd_positioned_consonants = self.count_odd_positioned_consonants(lexeme)
                if odd_positioned_consonants > self.max_consonants:
                    self.max_consonants = odd_positioned_consonants
                    self.max_lexemes = [lexeme]
                elif odd_positioned_consonants == self.max_consonants:
                    self.max_lexemes.append(lexeme)

            for j in range(n - 1, -1, -1):
                if a[j] < a[j + 1]:
                    break
            else:
                break

            v = a[j]
            for k in range(n, j, -1):
                if v < a[k]:
                    break

            a[j], a[k] = a[k], a[j]
            a[j + 1:] = a[j + 1:][::-1]

        return self.max_lexemes


finder = LexemeFinder('институт')
lexemes = finder.lexico_permute_string()
if finder.max_consonants == 0:
    print("Лексем с согласными на нечетных местах не существуют")
else:
    print("Лексемы с наибольшим числом согласных на нечетных местах:")
    for i, lexeme in enumerate(lexemes, start=1):
        print(i, "", lexeme)
