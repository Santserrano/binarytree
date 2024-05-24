from engine.arbol import Arbol
from engine.colors import colors
import timeit
import os
#a

start_time1 = timeit.default_timer()
arbol = Arbol('emma')
end_time1 = timeit.default_timer()

start_time2 = timeit.default_timer()
arbol.agregar("olivia")
arbol.agregar("isabella")
arbol.agregar("sofia")
arbol.agregar("emily")
arbol.agregar("talulah")
arbol.agregar("candela")
end_time2 = timeit.default_timer()

start_time3 = timeit.default_timer()
arbol.preorden()
end_time3 = timeit.default_timer()

start_time4 = timeit.default_timer()
arbol.inorden()
end_time4 = timeit.default_timer()

start_time5 = timeit.default_timer()
arbol.postorden()
end_time5 = timeit.default_timer()
os.system('cls')  
# Calcular la diferencia de tiempo
execution_time_1 = end_time1 - start_time1
execution_time_2 = end_time2 - start_time2
execution_time_pre = end_time3 - start_time3
execution_time_in = end_time4 - start_time4
execution_time_pos = end_time5 - start_time5

print(colors.MAGENTA + '*** Bechmarks ***')
print(colors.GREEN  + "***", colors.WHITE  + "[kernel 0] : [Clase] ",  colors.GREEN  + "  ***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_1),  colors.RED + "segundos"  + colors.RESET)
print(colors.GREEN  + "***", colors.WHITE  + "[kernel 1] : [Agregar] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_2),  colors.RED + " segundos"  + colors.RESET)
print(colors.GREEN  + "***", colors.WHITE  + "[kernel 2] : [pre]\t   ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_pre),  colors.RED + " segundos"  + colors.RESET)
print(colors.GREEN  + "***", colors.WHITE  + "[kernel 3] : [in]\t   ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_in),  colors.RED + " segundos"  + colors.RESET)
print(colors.GREEN  + "***", colors.WHITE  + "[kernel 4] : [pos]\t   ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_pos),  colors.RED + " segundos"  + colors.RESET)