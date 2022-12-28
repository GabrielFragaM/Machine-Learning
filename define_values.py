from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from helpers import getIndexColumn, getMessageOk, getMessageWarning, getMessageError


class DefineData:
    def __init__(self):
        pass

    def checkColumnsToEncoder(csv, columnBaseClass):
        try:
            getMessageOk('buscando por valores em strings...')

            def columnContainsStrings(columnName):
                for v in csv[columnName]:
                    if type(v) == str:
                        return columnName
                    else:
                        return None

            columnsToEncoder = []

            for column in csv.axes[1]:
                if(column != columnBaseClass):
                    if columnContainsStrings(column) != None:
                        columnsToEncoder.append(column)

            return columnsToEncoder
        except:
            getMessageError('busca por valores em strings...')
            return

    def defineStandScalerValues(base):
        try:
            getMessageOk(
                'aplicando fórmula de padronização de valores númericos...')
            base = StandardScaler().fit_transform(base)
            return base
        except:
            getMessageError(
                'falha ao aplicar fórmula de padronização de valores númericos...')
            return

    def defineEncode(csv, base, columns):
        try:
            getMessageOk(
                'aplicando o OneHotEncoder para valores transformados em números...')
            columnsIndexs = []

            for c in columns:
                columnsIndexs.append(getIndexColumn(csv, c))

            oneHotEncoded = ColumnTransformer(
                transformers=[('OneHot', OneHotEncoder(), columnsIndexs)], remainder='passthrough')

            try:
                base = oneHotEncoded.fit_transform(base).toarray()
            except:
                base = oneHotEncoded.fit_transform(base)

            return base
        except:
            getMessageError(
                'falha ao aplicar OneHotEncoder para valores transformados em números...')
            return

    def defineForecasters(csv):
        try:
            getMessageOk('definindo precisores base...')
            xValues = csv.iloc[:, 0:(len(csv.axes[1]) - 1)].values
            return xValues
        except:
            getMessageError('falha ao definir precisores base...')
            return

    def defineClass(csv, columnBaseClass):
        try:
            getMessageOk('definindo classe base...')
            xValues = csv.iloc[:, getIndexColumn(csv, columnBaseClass)].values
            return xValues
        except:
            getMessageError('falha ao definir classe base...')
            return

    def defineStringValuesToNumber(csv, base, columns):
        try:
            if(len(columns) != 0):
                getMessageWarning(
                    'transformando valores em strings para números...')
                for c in columns:
                    base[:, getIndexColumn(csv, c)] = LabelEncoder(
                    ).fit_transform(base[:, getIndexColumn(csv, c)])

                return base
        except:
            getMessageError(
                'falha para transformar valores em strings para números...')
            return

    def defineTrainingAndTestValues(baseX, baseY, testSize):
        try:
            getMessageOk('definindo dados de treinamento e test...')
            return train_test_split(baseX, baseY, test_size=testSize, random_state=0)
        except:
            getMessageError('falha ao definir dados de treinamento e test...')
            return
