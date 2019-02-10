'''cmd virtual chess game'''


class Pieces:
    def __init__(self, colour, location):
        self.colour = colour
        self.location = location
        self.vectorMap = {'A8': (8, 1), 'B8': (8, 2), 'C8': (8, 3), 'D8': (8, 4), 'E8': (8, 5), 'F8': (8, 6),
                        'G8': (8, 7), 'H8': (8, 8),
                        'A7': (7, 1), 'B7': (7, 2), 'C7': (7, 3), 'D7': (7, 4), 'E7': (7, 5), 'F7': (7, 6),
                        'G7': (7, 7), 'H7': (7, 8),
                        'A6': (6, 1), 'B6': (6, 2), 'C6': (6, 3), 'D6': (6, 4), 'E6': (6, 5), 'F6': (6, 6),
                        'G6': (6, 7), 'H6': (6, 8),
                        'A5': (5, 1), 'B5': (5, 2), 'C5': (5, 3), 'D5': (5, 4), 'E5': (5, 5), 'F5': (5, 6),
                        'G5': (5, 7), 'H5': (5, 8),
                        'A4': (4, 1), 'B4': (4, 2), 'C4': (4, 3), 'D4': (4, 4), 'E4': (4, 5), 'F4': (4, 6),
                        'G4': (4, 7), 'H4': (4, 8),
                        'A3': (3, 1), 'B3': (3, 2), 'C3': (3, 3), 'D3': (3, 4), 'E3': (3, 5), 'F3': (3, 6),
                        'G3': (3, 7), 'H3': (3, 8),
                        'A2': (2, 1), 'B2': (2, 2), 'C2': (2, 3), 'D2': (2, 4), 'E2': (2, 5), 'F2': (2, 6),
                        'G2': (2, 7), 'H2': (2, 8),
                        'A1': (1, 1), 'B1': (1, 2), 'C1': (1, 3), 'D1': (1, 4), 'E1': (1, 5), 'F1': (1, 6),
                        'G1': (1, 7), 'H1': (1, 8),
                        }
        self.coordinate = self.vectorMap.get(self.location)

    def checkMoveTo(self, newLocation, newVector, availablePieces, notAvailableCoord):

        if notAvailableCoord.get(newVector) is None:
             self.location = newLocation
             self.coordinate = newVector
             print('super: valid move, empty new location')

        else:
            i = notAvailableCoord.get(newVector)
            if newVector == i.coordinate:
                if self.colour == i.colour:
                    print('super: invalid move, eating self')
                else:
                    self.location = newLocation
                    self.coordinate = newVector
                    availablePieces.remove(i)
                    print('super: valid move, eating enemy')

        return(availablePieces)


class Rook(Pieces):
    def __init__(self, colour, location, type='Rook'):
        super().__init__(colour, location)
        if self.colour == 'b':
            self.ucode = chr(9820)
        elif self.colour == 'w':
            self.ucode = chr(9814)

    def moveTo(self, newLocation, availablePieces):
        currentVector = self.coordinate
        newVector = self.vectorMap.get(newLocation)
        x = newVector[0] - currentVector[0]
        y = newVector[1] - currentVector[1]

        if x == 0:
            notAvailableCoord = {}
            for i in availablePieces:
                notAvailableCoord.update({i.coordinate: i})
            absY = abs(y)
            scale = int(y/absY)
            for i in range(1,absY):
                if notAvailableCoord.get((currentVector[0],currentVector[1]+i*scale)) is not None:
                    print('invalid move: some piece in the way')
                    return
            availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)

        elif y == 0:
            notAvailableCoord = {}
            for i in availablePieces:
                notAvailableCoord.update({i.coordinate: i})
            absX = abs(x)
            scale = int(x/absX)
            for i in range(1,absX):
                if notAvailableCoord.get((currentVector[0]+i*scale,currentVector[1])) is not None:
                    print('invalid move: some piece in the way')
                    return
            availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)
        else:
            print('invalid move, illegal for piece')

        return(availablePieces)


class King(Pieces):

    def __init__(self, colour, location):
        super().__init__(colour, location)
        if self.colour == 'b':
            self.ucode = chr(9818)
        elif self.colour == 'w':
            self.ucode = chr(9812)

    def moveTo(self, newLocation, availablePieces):
        currentVector = self.coordinate
        newVector = self.vectorMap.get(newLocation)
        x = newVector[0] - currentVector[0]
        y = newVector[1] - currentVector[1]
        if abs(x) < 2 and abs(y) < 2:
            notAvailableCoord = {}
            for i in availablePieces:
                notAvailableCoord.update({i.coordinate: i})
            availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)
        else:
            print('invalid move, illegal for piece')
        return (availablePieces)


class Bishop(Pieces):

    def __init__(self, colour, location, type='Bishop'):
        super().__init__(colour, location)
        if self.colour == 'b':
            self.ucode = chr(9821)
        elif self.colour == 'w':
            self.ucode = chr(9815)
    def moveTo(self, newLocation, availablePieces):
        currentVector = self.coordinate
        newVector = self.vectorMap.get(newLocation)
        x = newVector[0] - currentVector[0]
        y = newVector[1] - currentVector[1]

        if abs(x) == abs(y):
            notAvailableCoord = {}
            for i in availablePieces:
                notAvailableCoord.update({i.coordinate: i})
            absY = abs(y)
            scaleX = int(x / absY)
            scaleY = int(y / absY)
            for i in range(1, absY):
                if notAvailableCoord.get((currentVector[0]+ i * scaleX, currentVector[1] + i * scaleY)) is not None:
                    print('invalid move: some piece in the way')
                    return (availablePieces)
            availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)


        else:
            print('invalid move, illegal for piece')
        return (availablePieces)


class Queen(Rook, Bishop):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        if self.colour == 'b':
            self.ucode = chr(9819)
        elif self.colour == 'w':
            self.ucode = chr(9813)

    def moveTo(self, newLocation, availablePieces):
        currentVector = self.coordinate
        newVector = self.vectorMap.get(newLocation)
        x = newVector[0] - currentVector[0]
        y = newVector[1] - currentVector[1]

        if abs(x) == abs(y):
            Bishop.moveTo(self, newLocation, availablePieces)

        elif x == 0 or y == 0:
            Rook.moveTo(self, newLocation, availablePieces)

        else:
            print('invalid move, illegal for piece')

        return (availablePieces)


class Knight(Pieces):

    def __init__(self, colour, location):
        super().__init__(colour, location)
        if self.colour == 'b':
            self.ucode = chr(9822)
        elif self.colour == 'w':
            self.ucode = chr(9816)

    def moveTo(self, newLocation, availablePieces):
        currentVector = self.coordinate
        newVector = self.vectorMap.get(newLocation)
        x = newVector[0] - currentVector[0]
        y = newVector[1] - currentVector[1]

        if abs(x) == 2*abs(y) or abs(y) == 2*abs(x):
            notAvailableCoord = {}
            for i in availablePieces:
                notAvailableCoord.update({i.coordinate: i})
            availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)

        else:
            print('invalid move, illegal for piece')
        return (availablePieces)


class Pawn(Pieces):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        if self.colour == 'b':
            self.ucode = chr(9823)
        elif self.colour == 'w':
            self.ucode = chr(9817)

    def moveTo(self, newLocation, availablePieces):
        currentVector = self.coordinate
        newVector = self.vectorMap.get(newLocation)
        x = newVector[0] - currentVector[0]
        y = newVector[1] - currentVector[1]
        notAvailableCoord = {}
        for i in availablePieces:
            notAvailableCoord.update({i.coordinate: i})
        if self.colour == 'b':
            if newVector not in notAvailableCoord:
                if currentVector[0] != 7:
                    if x == -1 and y == 0:
                        self.coordinate = newVector
                        self.location = newLocation
                    else:
                        print('illegal move')
                elif currentVector[0] == 7:
                    if x == -1 and y == 0:
                        self.coordinate = newVector
                        self.location = newLocation
                    elif x == -2 and y == 0:
                        self.coordinate = newVector
                        self.location = newLocation
                    else:
                        print('illegal move')
            elif x == -1 and abs(y) == 1:
                availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)
            else:
                print('illegal move')
        elif self.colour == 'w':
            if newVector not in notAvailableCoord:
                if currentVector[0] != 2:
                    if x == 1 and y == 0:
                        self.coordinate = newVector
                        self.location = newLocation
                    else:
                        print('illegal move')
                elif currentVector[0] == 2:
                    if x == 1 and y == 0:
                        self.coordinate = newVector
                        self.location = newLocation
                    elif x == 2 and y == 0:
                        self.coordinate = newVector
                        self.location = newLocation
                    else:
                        print('illegal move')
            elif x == 1 and abs(y) == 1:
                availablePieces = super().checkMoveTo(newLocation, newVector, availablePieces, notAvailableCoord)
            else:
                print('illegal move')
        return (availablePieces)


''' promotion of pawn is not improvised '''
    # def promotion(self, vectorMap):
    #     currentVector = self.coordinate
    #     if self.colour == 'b' and currentVector[0]==1:
    #         availablePieces.remove(self)
    #         return(availablePieces)
    #     elif self.colour == 'w' and currentVector[0]==8:
    #         availablePieces.remove(self)
    #         return(availablePieces)
    #     else:
    #         print('pawn promotion illegal call')


''' initialise the chess pieces '''
pw1 = Pawn('w', 'A2')
pw2 = Pawn('w', 'B2')
pw3 = Pawn('w', 'C2')
pw4 = Pawn('w', 'D2')
pw5 = Pawn('w', 'E2')
pw6 = Pawn('w', 'F2')
pw7 = Pawn('w', 'G2')
pw8 = Pawn('w', 'H2')
rw1 = Rook('w', 'A1')
rw2 = Rook('w', 'H1')
kw1 = Knight('w', 'B1')
kw2 = Knight('w', 'G1')
bw1 = Bishop('w', 'C1')
bw2 = Bishop('w', 'F1')
qw = Queen('w', 'D1')
kw = King('w', 'E1')
pb1 = Pawn('b', 'A7')
pb2 = Pawn('b', 'B7')
pb3 = Pawn('b', 'C7')
pb4 = Pawn('b', 'D7')
pb5 = Pawn('b', 'E7')
pb6 = Pawn('b', 'F7')
pb7 = Pawn('b', 'G7')
pb8 = Pawn('b', 'H7')
rb1 = Rook('b', 'A8')
rb2 = Rook('b', 'H8')
kb1 = Knight('b', 'B8')
kb2 = Knight('b', 'G8')
bb1 = Bishop('b', 'C8')
bb2 = Bishop('b', 'F8')
qb = Queen('b', 'D8')
kb = King('b', 'E8')

''' kept track of pieces '''
availablePieces = [pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8, rw1, rw2, kw1, kw2, bw1, bw2, qw, kw,
                   pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, rb1, rb2, kb1, kb2, bb1, bb2, qb, kb]


''' a function to print the chess board/ chr(9930) has been used as a place holder'''


def printBoard(availablePieces):
    a = {'A8': chr(9930), 'B8': chr(9930), 'C8': chr(9930), 'D8': chr(9930), 'E8': chr(9930), 'F8': chr(9930),
         'G8': chr(9930), 'H8': chr(9930),
         'A7': chr(9930), 'B7': chr(9930), 'C7': chr(9930), 'D7': chr(9930), 'E7': chr(9930), 'F7': chr(9930),
         'G7': chr(9930), 'H7': chr(9930),
         'A6': chr(9930), 'B6': chr(9930), 'C6': chr(9930), 'D6': chr(9930), 'E6': chr(9930), 'F6': chr(9930),
         'G6': chr(9930), 'H6': chr(9930),
         'A5': chr(9930), 'B5': chr(9930), 'C5': chr(9930), 'D5': chr(9930), 'E5': chr(9930), 'F5': chr(9930),
         'G5': chr(9930), 'H5': chr(9930),
         'A4': chr(9930), 'B4': chr(9930), 'C4': chr(9930), 'D4': chr(9930), 'E4': chr(9930), 'F4': chr(9930),
         'G4': chr(9930), 'H4': chr(9930),
         'A3': chr(9930), 'B3': chr(9930), 'C3': chr(9930), 'D3': chr(9930), 'E3': chr(9930), 'F3': chr(9930),
         'G3': chr(9930), 'H3': chr(9930),
         'A2': chr(9930), 'B2': chr(9930), 'C2': chr(9930), 'D2': chr(9930), 'E2': chr(9930), 'F2': chr(9930),
         'G2': chr(9930), 'H2': chr(9930),
         'A1': chr(9930), 'B1': chr(9930), 'C1': chr(9930), 'D1': chr(9930), 'E1': chr(9930), 'F1': chr(9930),
         'G1': chr(9930), 'H1': chr(9930),
         }

    for k in availablePieces:
        a[k.location] = k.ucode
    print(' ', '|', a['A8'], '|', a['B8'], '|', a['C8'], '|', a['D8'], '|', a['E8'], '|', a['F8'], '|', a['G8'], '|',
          a['H8'], '|', '8', '\n'
                             '  ---------------------------------------\n',
          '', '|', a['A7'], '|', a['B7'], '|', a['C7'], '|', a['D7'], '|', a['E7'], '|', a['F7'], '|', a['G7'], '|',
          a['H7'], '|', '7', '\n'
                             '  ---------------------------------------\n',
          '', '|', a['A6'], '|', a['B6'], '|', a['C6'], '|', a['D6'], '|', a['E6'], '|', a['F6'], '|', a['G6'], '|',
          a['H6'], '|', '6', '\n'
                             '  ---------------------------------------\n',
          '', '|', a['A5'], '|', a['B5'], '|', a['C5'], '|', a['D5'], '|', a['E5'], '|', a['F5'], '|', a['G5'], '|',
          a['H5'], '|', '5', '\n'
                             '  ---------------------------------------\n',
          '', '|', a['A4'], '|', a['B4'], '|', a['C4'], '|', a['D4'], '|', a['E4'], '|', a['F4'], '|', a['G4'], '|',
          a['H4'], '|', '4', '\n'
                             '  ---------------------------------------\n',
          '', '|', a['A3'], '|', a['B3'], '|', a['C3'], '|', a['D3'], '|', a['E3'], '|', a['F3'], '|', a['G3'], '|',
          a['H3'], '|', '3', '\n'
                             '  ---------------------------------------\n',
          '', '|', a['A2'], '|', a['B2'], '|', a['C2'], '|', a['D2'], '|', a['E2'], '|', a['F2'], '|', a['G2'], '|',
          a['H2'], '|', '2', '\n'
                             '  ---------------------------------------\n'
                             ' ', '|', a['A1'], '|', a['B1'], '|', a['C1'], '|', a['D1'], '|', a['E1'], '|', a['F1'],
          '|', a['G1'], '|', a['H1'], '|', '1', '\n'
                                                '  ---------------------------------------\n'
                                                ' ', '|', 'A ', '|', 'B ', '|', 'C ', '|', 'D ', '|', 'E ', '|', 'F ', '|',
          'G ', '|', 'H ', '|', '\n')
    return ()


''' main function '''


def main(availablePieces):
    move = input('make your move (Capital): current location, new location \n-help for help:')
    move = move.split(',') #now a list
    for i in availablePieces:
        if i.location == move[0]:
            availablePieces = i.moveTo(move[1], availablePieces)
            print(i.location)
            printBoard(availablePieces)
            return(availablePieces)
    if move[0]=='-help':
        print('\nhelp: use capital, enter current location and new location separated by ","',
              '\ngame end when you capture opponent\'s king.'
              '\nadvanced movements of the pieces are not supported',
              '\npawn promotion is not supported'
              '\nwhite moves first\n')
    else:
        print('piece not found')
    return(availablePieces)


''' print the chess board '''

printBoard(availablePieces)
while kw in availablePieces and kb in availablePieces:
    try:
        availablePieces = main(availablePieces)
    except TypeError:
        print('please check entry')
    except IndexError:
        print('please check entry')
    except:
        print('please check entry')

print('///////game over/////////')
if kw in availablePieces:
    print('white win')
elif kb in availablePieces:
    print('black win')

