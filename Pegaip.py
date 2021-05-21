nom = str(input('digite seu link: '))
seg = int(input('selecione o tempo de redirecionamento: '))
tit = str(input('digite um titulo para o site: '))

print('-'*79)

print('<DOCTYPE html>\n<html>\n  <head>\n    <meta http-equiv="refresh" content="{}; url={}">\n    <meta name="" content="">\n    <title>{}</title>\n  </head>\n  <body>\n</body>\n</html>'.format(seg, nom, tit))
print('-'*79)
print('crie um arquivo.html salve e mande para a vitima')
print('-'*79)
