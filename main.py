from transliterate import translit


print(translit("Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.", 'ru'))   
print(translit("More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...", 'ru'))

from num2words import num2words


print(num2words(42))  
print(num2words(42, to='ordinal')) 
print(num2words(42, lang='fr'))    
