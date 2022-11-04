from define_values import defineClass, defineForecasters, defineStandScalerValues, defineStringValuesToNumber, checkColumnsToEncoder, defineEncode
from helpers import getColumns, getMessageOk, getMessageWarning, getMessageError


def fillValuesNull(csv):
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


def treatmentValues(csv, columnBaseClass, StandScaler, OneHotEncoder):
    csv = fillValuesNull(csv)

    x = defineForecasters(csv)
    y = defineClass(csv, columnBaseClass)

    columnsToEncoder = checkColumnsToEncoder(csv, columnBaseClass)

    if(len(columnsToEncoder) != 0):
        x = defineStringValuesToNumber(csv, x, columnsToEncoder)
        if(OneHotEncoder == True):
            x = defineEncode(csv, x, columnsToEncoder)

    if(StandScaler == True):
        x = defineStandScalerValues(x)

    return x, y
