from turtle import bgcolor
import pandas as pd
from colors import bcolors
from machine_learning import MachineLearning
from treatment_values import TreatmentData


def main(nameFile: str, path: str, columnBaseClass: str, standScaler: bool,
         oneHotEncoder: bool, testSize: float, machineLarningType: str, saveBaseData: bool, applyFilesTrainingAndTest: bool,
         predictValues: list):

    csv = pd.read_csv(path)
    treatmentData = TreatmentData(
        csv, columnBaseClass, standScaler, oneHotEncoder)

    baseX, baseY = treatmentData.getFormattedData()

    result = MachineLearning.startMachineLearning(nameFile, baseX, baseY,
                                  testSize, machineLarningType, saveBaseData, applyFilesTrainingAndTest, predictValues)

    print(bcolors.OKGREEN + 'resultado da previsão:' + bcolors.ENDC, result)


main(nameFile='census', path='census.csv', columnBaseClass='',
     standScaler=True, oneHotEncoder=True, testSize=0.15,
     machineLarningType='NaiveBayes', saveBaseData=False, applyFilesTrainingAndTest=True,
     predictValues=[])
