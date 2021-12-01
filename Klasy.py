# coding: utf-8

import numpy as np
from math import *
from random import choice

class Macierz( object ):
    """ Klasa abstrakcyjna """
    def __init__( self, macierz = None, wsp = 0.001 ): 
        self.macierz = macierz
        self.wsp = wsp # wsp oznacza maksymalny dopuszczalny błąd przy definiowaniu unitarnych bramek i kubitów 

    def IloczynKronekera( self, macierz ):
        """  Zmodyfikowana funkcja np.kron() """
        if len( self.macierz.shape ) == 1 or self.macierz.shape[ 0 ] == 1:
            self.macierz = self.macierz.reshape( max( self.macierz.shape ), 1 )
        if len( macierz.shape ) == 1 or macierz.shape[ 0 ] == 1:
            macierz = macierz.reshape( max( macierz.shape ), 1 )
        Kroneker = np.zeros( ( self.macierz.shape[ 0 ] * macierz.shape[ 0 ],
                               self.macierz.shape[ 1 ] * macierz.shape[ 1 ] ), 
                               dtype = np.complex128 )
        temp = []
        for m in range( self.macierz.shape[ 0 ] ):
            for n in range( self.macierz.shape[ 1 ] ):
                for k in range( macierz.shape[ 0 ] ):
                    for l in range( macierz.shape[1] ):
                        temp.append(self.macierz[ m, n ] * macierz [ k, l ])
                for k in range( macierz.shape[ 0 ] ):
                    for l in range( macierz.shape[ 1 ] ):
                        Kroneker[ m * macierz.shape[ 0 ] + k, n * macierz.shape[ 1 ] + l ] = temp.pop( 0 )
        return Kroneker
    def wyczyscSzum( self, macierz = None ):
        """ Poprawia proste odchylenia od teoretycznego wyniku"""
        wsp = self.wsp
        if macierz is None:
            macierz = self.macierz
        stanyDoPoprawy = [ -1, -0.25, -0.5, 0, 0.25, 0.5, 1 ] 
        for i, x in np.ndenumerate( macierz ): 
            #print( x, i )
            for j in stanyDoPoprawy:
                if j - wsp <  x.real < j + wsp and x != j:
                    x -= x.real
                    x += j
                    break
            for j in stanyDoPoprawy:
                if j - wsp < x.imag < j + wsp and x.imag != j:
                    x -= x.imag * 1.j
                    x += j * 1.j
                    break
            macierz[ i ] = x
        self.macierz = macierz
        return self.macierz
    def __str__( self ):
        if len( self.macierz.shape ) == 1:
            self.macierz = self.macierz.reshape( self.macierz.shape[ 0 ], 1 )
        wsp = 1
        for i in range( self.macierz.shape[ 0 ] ):
            for j in range( self.macierz.shape[ 1 ] ):
                if wsp == 1 and self.macierz[ i, j ] != 0: wsp = abs( self.macierz[ i, j ] )
                if wsp != abs( self.macierz[ i, j ] ) and self.macierz[ i, j ] != 0:
                    wsp = None
                    #print ( i, j )
                    break
            if wsp == None:
                wsp = 1
                break
        return str( wsp ) + '*\n' + str( self.macierz / wsp )
class Baza( Macierz ):
    def __init__( self, wejscie, symbol = None ):
        Macierz.__init__( self )
        if type( wejscie ) == np.ndarray and len( wejscie.shape ) == 2 and wejscie.shape[ 0 ] == wejscie.shape[ 1 ]:
            self.macierz = wejscie 
            self.rozmiar = int( log( self.macierz.shape[ 0 ], 2 ) )
            if not self.czyUnitarna():# or not self.Samosprzezona():
                self.rozmiar = 0
                self.macierz = None
                return
        else:
            print ( "Error input", wejscie.shape, 'and:' ,symbol )
            self.rozmiar = 0
            self.macierz = None
            self.symbol = 'Failed init'
            return 
        if len( self.macierz.shape ) == 1:
            self.macierz = self.macierz.reshape( self.macierz.shape[ 0 ], 1 )
        self.symbol = symbol
        self.wyczyscSzum()
    def czyUnitarna( self ):
        """ Sprawdza, czy self.macierz reprezentuje bramkę unitarną."""
        for e in self.macierz:
            if abs( sum( abs( e * e ) ) - 1 ) > self.wsp:
                print( 'macierz:', self.macierz )
                print( 'wiersz bledny:', e )
                return False
        return True
    def Sprzegnij( self, parametr = None ):
        """ Zwraca sprzężoną macierz znajdującą się w zmiennej self.macierz """
        if parametr != None:
            if type( parametr ) in [ complex, np.complex128 ] and parametr.imag != 0: 
                return parametr.real - parametr.imag * 1j
            return parametr
        macierz = self.macierz.T.copy()
        for i, el in np.ndenumerate( macierz ):
                if i[ 0 ] == i[ 1 ]: continue
                macierz[ i ] = self.Sprzegnij( el )
        return macierz
    def Samosprzezona( self ):
        """ Zwraca True jeśli zmienna self.macierz jest samosprzężona, lub Fasle, jeśli nie jest. """
        if ( self.Sprzegnij() == self.macierz ).all():
            return True
        print( 'niesamosprzezona' )
        return False
    def __mul__( self, obj ):
        return Baza( self.IloczynKronekera( obj.macierz ) )

class Kubit( Macierz ):
    def __init__( self, alfa, beta = None, symbol = None ):
        self.kubity = 1
        Macierz.__init__( self, None ) # definiuje domyślny wsp znajdujący się w macie Macierz
        types = [ int, float, complex, np.complex128 ] 
        if type( alfa ) == list and type( alfa[ 0 ] ) == Kubit:
            #print ("Kubit Base Creator")
            self.macierz = alfa[ 0 ].Wektor()
            self.kubity = alfa[ 0 ].kubity
            for i in range( 1, len( alfa ) ):
                self.macierz = self.IloczynKronekera( alfa[ i ].Wektor() )
                self.kubity += alfa[ i ].kubity
        elif type( alfa ) == np.ndarray and ( min( alfa.shape ) == 1 or len( alfa.shape ) == 1 ):
            self.macierz = alfa  
            self.kubity = int( log( max( alfa.shape ), 2 ) )
        elif type( alfa ) == list and log( len( alfa ), 2 ) == int( log( len( alfa ), 2 ) ):
            self.macierz = np.array( alfa, dtype = np.complex128 )
            self.kubity = int( log( len( alfa ), 2 ) )
        
        elif type( alfa ) in types and type( beta ) in types:
            self.macierz = np.array( [ [ alfa, beta ] ], dtype = np.complex128 )
        else:
            print ( "Error input: ", alfa )
            self.kubity = 0
            self.macierz = None
            return
        #self.dlugosc = abs( 1 - np.sum( abs( self.macierz ** 2 ) ) )
        self.wyczyscSzum()
        if not self.DlugoscJeden():
            self.macierz = None
        self.symbol = symbol
    def __eq__( self, p2 ):
        """ Porównywuje zmienne self.macierz """
        if type( p2 ) == Kubit and self.kubity == p2.kubity and ( self.macierz == p2.macierz ).all():
            return True
        return False
    def Wektor( self ):
        return self.macierz
    def pomiar( self, kolejnosc = None, ilePomiarow = 1 ):
        """ Zwraca 0, lub 1 zależnie od wylosowanej liczby z odpowiednim prawdopodobieństwem, 
        oraz poprawia zmienną self.kubity i self.macierz tj. wektor skraca o połowe, 
        a pozostałe wartości odpowiednio przeskalowuje"""
        self.macierz = self.macierz.ravel()
        wynik = []
        if kolejnosc is None:
            kolejnosc = list( range( ilePomiarow ) )
        if ilePomiarow < self.kubity:
            for i in range( ilePomiarow ):
                mierzonyKubit = kolejnosc[ 0 ] + 1
                kolejnosc.pop( 0 )
                bag = []
                nowyMacierz0 = []
                nowyMacierz1 = []
                for ind, el in enumerate( self.macierz ):
                    wekt =  ( 2 ** mierzonyKubit ) * ind // ( 2 ** self.kubity ) % 2 
                    bag.extend( [ wekt ] * int( abs( el ** 2 ) * 1000 ) )  
                    if wekt == 1:
                        nowyMacierz1.append( el )
                    else:
                        nowyMacierz0.append( el )
                zmierzonyStan = choice( bag )
                print( zmierzonyStan )
                self.kubity -= 1
                k_0 = np.array( nowyMacierz0, dtype = np.complex128 ).ravel()
                k_0sum = sum( abs( k_0 ) ** 2 )
                k_1 = np.array( nowyMacierz1, dtype = np.complex128 ).ravel()
                k_1sum = sum( abs( k_1 ) ** 2 )
                if zmierzonyStan == 0:
                    for liczn, wart in enumerate( k_0 ):
                        k_0[ liczn ] =  wart * sqrt( k_0sum ** -1 )
                    self.macierz = k_0
                else:
                    for liczn, wart in enumerate( k_1 ):
                        k_1[ liczn ] =  wart * sqrt( k_1sum ** -1 )
                    self.macierz = k_1
                if self.kubity == 0:
                    self.macierz = None
                    return [ zmierzonyStan ]

                if self.DlugoscJeden() != True:
                    print( 'error in', self.macierz )
                    #self.macierz = None
                    return False

                wynik.append( zmierzonyStan )
            return wynik
        elif ilePomiarow == self.kubity:
            bag = []
            for e, i in enumerate( self.macierz ):
                bag.extend( [ e ] * int( abs( i * i ) * 1000 ) )  
            wektor = choice( bag )
            stanZmiezony = str( bin( wektor ) )[ 2: ]
            wynik = stanZmiezony[ : : -1 ]
            self.macierz = None
            return wynik + '0' * ( self.kubity - len( wynik ) )

    def DlugoscJeden( self ):    
        """ Zwraca prawdę jeśli suma kwadratów zmiennej self.macierz nie różni się od 1 o więcej niż self.wsp """
        kwadraty = abs( self.macierz.reshape( -1 ) ** 2 ) 
        if abs( 1 - sum( kwadraty ) ) > self.wsp:
            print ( "Error: kubit length 1 != :", sum( kwadraty ) )
            return False
        return True
    
    def __mul__( self, obj ): 
        return self.IloczynKronekera( obj.Wektor() )

class Bramka( object ):
    """ Klasa przechowująca tworząca bramki z Baz, przeznaczone dla klasy System """
    def __init__( self, bazy ):  
        self.bazy = bazy
        self.Buduj()
        
    def Buduj( self ):
        """ Ze zmiennej self.bazy tworzy macierz iloczynem Kroneckera """
        macierz = self.bazy[ 0 ]
        self.ile_kubitow = self.bazy[ 0 ].rozmiar
        for i in range( 1, len( self.bazy ) ):
            macierz = macierz * self.bazy[ i ]
            self.ile_kubitow += self.bazy[ i ].rozmiar
        self.macierz = macierz.macierz
    def Przejdz( self, kubity ):
        """ Mnoży produktowo zmienną self.macierz i zmienną macierz instancji wejściowej """
        if 2 ** self.ile_kubitow != max( kubity.macierz.shape ):
            print( self.ile_kubitow,'bramka i', kubity.macierz.shape, 'kubit' ) 
            print( "awaria" ) 

            return False
        if len( kubity.macierz ) == len( self.macierz ): 
            kubity.macierz = kubity.macierz.T
        kubity.macierz = np.dot( kubity.macierz, self.macierz )
        kubity.wyczyscSzum()
        return kubity
    
#SPRAWDZENIE KLASY REALIZUJĄC SWAP
def test1():
    """ Wzór operacji, przygotowany do testów klas z pominięciem interfejsu i systemu"""
    bram1 = Bramka( [ CNOT ] )
    bram2 = Bramka( [ XCNOT ] )
    bram3 = Bramka( [ CNOT ] )
    k1 = K_1
    k2 = K_1
    kub = [ k1, k2 ]
    x1 = Kubit( kub )
    print( x1.macierz.T )
    x1 = bram1.Przejdz( x1.macierz ) 
    x1 = bram2.Przejdz( x1 )
    print( bram3.Przejdz( x1 ) )
    
class System( object ): 
    """ Klasa, która przy pomocy listy kubitów i listy list bramek wykonuje obliczenia i zwraca kubit po przejściu przez bramki """
    def __init__( self, gates, Kinput = None ):
        self.gates = gates #list of Baza
        self.input = Kinput 
        self.qubits = None
        for i, el in enumerate( gates ):   
            for j in el:
                print( j.symbol )
            self.gates[ i ] = Bramka( el )
    def UstawKubity( self, inp ): 
        self.input = inp   #list of Kubit or wektor

    def Symuluj( self ):
        """ Tworzy instancję kubitu początkowego i mnoży z elementami zmiennem self.gates """

        if type( self.input ) != Kubit:
            self.input = Kubit( self.input )
        for i in self.gates:
            if self.input == False:
                return False
            self.input = i.Przejdz( self.input )
        if self.input.DlugoscJeden():
            return self.input
        print( 'Błąd odpowiedzi sieci dla: ', self.input.macierz )
        return False


#przykład użycia
def example():
    """ Do testów klas bez użycia interfejsu  """
    
    print ("""Tworzymy instancję klasy System podając jako argument listę;
    Każdy element listy to lista instancji klasy 'Baza' zawierających porządane macierze
    (np.  [ [ CNOT, I ], [ XCNOT, I ], [ CNOT, H ] ] )
    Następnie funkcją UstawKubity podajemy listę instancji klasy kubit, zawierające 
    stan kubitów wejściowych (puki co, tylko niesplątane)
    macierz wyjściową otrzymamy jako wynik funkcji Symuluj
    """)

    setup = System( [ [ CNOT ], [ XCNOT ], [ CNOT ] ] )

    Kinput = [ K_plus, K_minus ]

    setup.UstawKubity( Kinput )
    print("kubity na wejściu")
    print(  Kubit( Kinput, None ) )
    result = setup.Symuluj()
    print( Kubit( Kinput, None ).macierz )
    print()
    print("kubity na wyjściu")
    print( result )
    
def boolGate( zm, boolGFor, name = None ):
    boolGMacierz = np.eye( 2 ** boolGFor ) 
    for i in range( boolGMacierz.shape[ 0 ] ):
        definition = eval( zm )
        boolGMacierz[ i, i ] =  ( -1 ) ** int( definition + 1 )
    return Baza( boolGMacierz, name )

