def textsum(tekst,letter):
    
    return tekst.count(letter)
    
    
tekst= "You never get a second chance to make a first impression"
letter="e"

print(f"Letter '{letter}' appears in text: {textsum(tekst,letter)} times")