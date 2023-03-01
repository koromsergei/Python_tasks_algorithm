from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

print(Fore.BLUE + 'some red text')
print(Back.WHITE + 'and with a green background')
print(Style.BRIGHT + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')