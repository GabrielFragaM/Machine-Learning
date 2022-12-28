from define_values import DefineData
from helpers import getColumns, getMessageOk, getMessageWarning, getMessageError


class TreatmentData:
    def __init__(self, csv, columnBaseClass, standScaler, oneHotEncoder):
        self.csv = csv
        self.columnBaseClass = columnBaseClass
        self.standScaler = standScaler
        self.oneHotEncoder = oneHotEncoder

    def checkValuesEmpty(self, csv):
        try:
            getMessageOk('procurando por valores em nulo...')
            columns = getColumns(csv)
            columnsNull = csv.isnull().sum()
            index = 0
            for c in columnsNull:
                if(c != 0):
                    getMessageWarning('corrigindo valores em nulo...')
                    try:
                        csv.fillna(csv[columns[index]].mean(), inplace=True)
                    except:
                        csv = csv[csv[columns[index]].notna()]
                        csv = csv.reset_index(drop=True)
                index += 1
            return csv
        except:
            getMessageError('falha ao corrigir valores em nulo...')
            return

    def getFormattedData(self):

        if(self.columnBaseClass == ''):
            cols = [c for c in self.csv.columns]
            self.columnBaseClass = cols[-1]

        self.csv = self.checkValuesEmpty(self.csv)

        x = DefineData.defineForecasters(self.csv)
        y = DefineData.defineClass(self.csv, self.columnBaseClass)

        columnsToEncoder = DefineData.checkColumnsToEncoder(
            self.csv, self.columnBaseClass)

        if(len(columnsToEncoder) != 0):
            x = DefineData.defineStringValuesToNumber(
                self.csv, x, columnsToEncoder)
            if(self.oneHotEncoder == True):
                x = DefineData.defineEncode(self.csv, x, columnsToEncoder)

        if(self.standScaler == True):
            x = DefineData.defineStandScalerValues(x)

        return x, y
