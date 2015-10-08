
def Cesar(texto, despl):
    i = 0
    z = 124
    text = list(texto)
    while i<len(text):
        ascii= ord(text[i])
        if (ascii >= 97) and (ascii<123):
            num_max = ascii+despl
            if num_max >= 123:
                ascii = ascii+despl-26
            else:
                ascii = ascii+despl
            text[i] = chr(ascii)
        i=i+1
    print "".join(text)
    
        


   



