#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# **********************************************************************

def print_abacus(value):
  s = str(value)
  row = '|00000*****|'
  i = 0
  j = 0
  while i < 10 - len(s):# 10 - 8 = 2    
    print(row[:11] + "   " + row[11])# |00000*****   | 
    i = i + 1

  while j < len(s):
    n = int(s[j]) # 1
    output = row[:(11 - n)] + "   " + row[(11 - n):] # |00000****   *|
    print(output)
    j = j + 1


   
  


# ###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |

print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|

print "Abacus showing 1337:"
print_abacus(1337)
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000*****   |
# #>>>|00000****   *|
# #>>>|00000**   ***|
# #>>>|00000**   ***|
# #>>>|000   00*****|
