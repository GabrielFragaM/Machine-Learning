from sklearn.metrics import classification_report, accuracy_score
from define_values import DefineData
import pickle
from helpers import getMessageOk, getMessageError
from sklearn.naive_bayes import GaussianNB


class MachineLearning:
    def __init__(self):
        pass

    def startMachineLearning(nameFile, baseX, baseY, testSize, machineLarningType, saveBaseData, applyFilesTrainingAndTest, predictValues):

        def saveBaseTrainingAndTestValues(self, nameFile, xTraining, xTest, yTraining, yTest):
            try:
                getMessageOk('salvando dados de trainamento e teste...')
                with open(nameFile, mode='wb') as f:
                    pickle.dump([xTraining, yTraining, xTest, yTest], f)
            except:
                getMessageError(
                    'salvamento de dados de trainamento e teste...')
                return

        def algorithmNaiveBayes(applyFilesTrainingAndTest, baseX, baseY, testSize, saveBaseData, nameFile, predictValues):
            def getPredict(xTraining, yTraining, yTest, predictValues):
                result = GaussianNB().fit(xTraining, yTraining)
                result = result.predict(predictValues)

                return {
                    'percentual_acerto': '%.2f' % (accuracy_score(yTest, result) * 100) + '%',
                    'report': classification_report(yTest, result),
                    'resultado': result
                }

            if(applyFilesTrainingAndTest == True):
                xTraining, xTest, yTraining, yTest = DefineData.defineTrainingAndTestValues(
                    baseX, baseY, testSize)
                if(saveBaseData == True):
                    saveBaseTrainingAndTestValues(
                        nameFile, xTraining, xTest, yTraining, yTest)
                if(len(predictValues) == 0):
                    return getPredict(xTraining, yTraining, yTest, xTest)
                else:
                    return getPredict(xTraining, yTraining, yTest, predictValues)
            else:
                result = GaussianNB().fit(baseX, baseY)
                return result.predict(predictValues)

        def algorithmTreeDecision():
            return

        try:
            getMessageOk('iniciado machine larning algoritmo de ' +
                         machineLarningType)
            if(machineLarningType == 'NaiveBayes'):
                return algorithmNaiveBayes(applyFilesTrainingAndTest, baseX, baseY, testSize, saveBaseData, nameFile, predictValues)
            if(machineLarningType == 'TreeDecision'):
                return algorithmTreeDecision()
        except:
            getMessageError('falha ao iniciar machine larning algoritmo de ' +
                            machineLarningType + '...')
            return
