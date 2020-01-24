import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
      key_columna = line.split('   ')[0]
      valor1_columna = line.split('   ')[1]
      valor2_columna = line.split('   ')[2].strip()
      sys.stdout.write("{}\t{}\t{}\n".format(key_columna,valor1_columna,valor2_columna))