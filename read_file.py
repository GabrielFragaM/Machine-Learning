from turtle import bgcolor
import pandas as pd
from colors import bcolors
from machine_larning import applyMachineLarning
from treatment_values import treatmentValues


def main(nameFile: str, path: str, columnBaseClass: str, StandScaler: bool,
         OneHotEncoder: bool, testSize: float, machineLarningType: str, saveBaseData: bool, applyFilesTrainingAndTest: bool,
         predictValues: list
         ):
    csv = pd.read_csv(path)
    baseX, baseY = treatmentValues(
        csv, columnBaseClass, StandScaler, OneHotEncoder)
    result = applyMachineLarning(nameFile, baseX, baseY,
                                 testSize, machineLarningType, saveBaseData, applyFilesTrainingAndTest, predictValues)

    print(bcolors.OKGREEN + 'resultado da previsão:' + bcolors.ENDC, result)


main(nameFile='census', path='census.csv', columnBaseClass='income',
     StandScaler=True, OneHotEncoder=True, testSize=0.15,
     machineLarningType='NaiveBayes', saveBaseData=False, applyFilesTrainingAndTest=True,
     predictValues=[])
