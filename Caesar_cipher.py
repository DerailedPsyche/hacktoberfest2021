def encrypt(word, shift):
    word=word.lower()
    s=''
    l=list('abcdefghijklmnopqrstuvwxyz')
    for i in word:
        if i in l[:len(l)-shift]:
            s=s+l[l.index(i)+shift]
        elif i in l[len(l)-shift:]:
            s=s+l[l.index(i)+shift-26]
        elif i==' ':
            s=s+' '
    print(s)
word=input('Word to be encrypted:')
shift=int(input('Encryption shift:'))
encrypt(word,shift)
