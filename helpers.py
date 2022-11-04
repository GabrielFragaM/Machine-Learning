from colors import bcolors


def getIndexColumn(csv, columnName):
    columns = []
    for c in csv.axes[1]:
        columns.append(c)

    return columns.index(columnName)


def getColumns(csv):
    columns = []
    for c in csv.axes[1]:
        columns.append(c)

    return columns


def getMessageOk(message):
    print(message + bcolors.OKGREEN + ' OK.' + bcolors.ENDC)


def getMessageError(message):
    print(message + bcolors.FAIL + ' Erro.' + bcolors.ENDC)


def getMessageWarning(message):
    print(bcolors.WARNING + message + bcolors.ENDC +
          bcolors.OKGREEN + ' OK.' + bcolors.ENDC)
