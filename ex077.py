palavras = {'livro', 'caderno', 'python', 'acreditar', 'faculdade', 'amigos', 'familia', 'pai'}
print (palavras)
for p in palavras:
    print('\nNa palavras {} temos: '.format(p.upper()), end= ' ')
    for palavra in p:
        if palavra.lower() in 'aeiou':
            print(palavra, end=' ')

