from googleSheets import*
import pandas as pd
import math
if __name__ == "__main__":
  spreadsheet = sheets()  

  df = pd.DataFrame(spreadsheet)

  semestre = df[0][1]
  partes = semestre.split(':')
  qntAulas = int(partes[1])
  porcentagemFaltas = int(qntAulas * 0.25)
  alunosFaltas = []
  alunosP1 = []
  alunosP2 = []
  alunosP3 = []
  
  for i in range(3,27):
    linhas_selecionadas = df.loc[i]
    alunosFaltas.append(int(linhas_selecionadas[2]))
    alunosP1.append(int(linhas_selecionadas[3]))
    alunosP2.append(int(linhas_selecionadas[4]))
    alunosP3.append(int(linhas_selecionadas[5]))
  
  situacao = []
  notaFinal = []
  
  for i in range(0,24):
    m = math.ceil((alunosP1[i] + alunosP2[i] + alunosP3[i])/3)
    if alunosFaltas[i] > porcentagemFaltas:
      situacao.append(["Reprovado por falta"])
      notaFinal.append([0])
    elif m < 50:
      situacao.append(["Reprovado por Nota"])
      notaFinal.append([0])
    elif 50 <= m < 70:
      situacao.append(["Exame Final"])
      naf = (50 * 2) - m
      notaFinal.append([naf])
    elif m >= 70:
      situacao.append(["Aprovado"])
      notaFinal.append([0])

  upDateSheets(situacao,notaFinal)
  



