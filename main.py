# Importing necessary modules
from googleSheets import*
import pandas as pd
import math
import logging

# Main function
if __name__ == "__main__":

  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
  # Initializing logger
  logger = logging.getLogger(__name__)
  logger.info("Operation started")
  # Loading spreadsheet data
  spreadsheet = sheets()  
  logger.info("Spreadsheet loaded")

  # Creating DataFrame from spreadsheet data
  df = pd.DataFrame(spreadsheet)
  # Extracting semester information
  semester = df[0][1]
  parts = semester.split(':')
  numClasses = int(parts[1])
  # Calculating maximum absence percentage
  absencePercentage = int(numClasses * 0.25)
  absentStudents = []
  gradesP1 = []
  gradesP2 = []
  gradesP3 = []
  
  # Looping through rows to extract relevant data
  for i in range(3,27):
    selected_rows = df.loc[i]
    absentStudents.append(int(selected_rows[2]))
    gradesP1.append(int(selected_rows[3]))
    gradesP2.append(int(selected_rows[4]))
    gradesP3.append(int(selected_rows[5]))
  
  # List to store student status
  status = []
  # List to store final grades
  finalGrade = []

  # Looping through students to determine their status and final grade
  for i in range(0,24):
    average = math.ceil((gradesP1[i] + gradesP2[i] + gradesP3[i])/3)
    if absentStudents[i] > absencePercentage:
      status.append(["Reprovado por falta"])
      finalGrade.append([0])
    elif average < 50:
      status.append(["Reprovado por Nota"])
      finalGrade.append([0])
    elif 50 <= average < 70:
      status.append(["Exame Final"])
      final_exam_grade = (50 * 2) - average
      finalGrade.append([final_exam_grade])
    elif average >= 70:
      status.append(["Aprovado"])
      finalGrade.append([0])

  # Updating Google Sheets with student status and final grades
  upDateSheets(status, finalGrade)
  logger.info("Operation completed.")
