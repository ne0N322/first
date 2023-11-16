from colorama import*
print(Fore.RED + 'Red')
# Fore - отвечает за цвет текста
print(Back.GREEN + '1')
# Back - отвечает за цвет фона сзади текста 
print (Style.BRIGHT + 'Python')
# Style - отвечает за стиль текста
print(Fore.BLUE,Back.YELLOW,Style.BRIGHT + 'Ukraine')
deinit()
# deinit - отвечает за сброс настроек и возврата к стандартным цветам. его можно использовать например при условии, если False то deinit() 
# и сброс к обычным цветам

