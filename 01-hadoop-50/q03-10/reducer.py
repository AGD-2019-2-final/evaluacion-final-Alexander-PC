import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
    for line in sys.stdin:
      line = line.strip()
      key_columna = line.split(',')[1]
      valor_columna = line.split(',')[0]
      sys.stdout.write("{},{}\n".format(key_columna,valor_columna))