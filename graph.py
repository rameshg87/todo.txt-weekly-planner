#!/usr/bin/python

import sys
import os

if sys.argv[ 1 ].endswith( ";" ):
    sys.argv[ 1 ] = sys.argv[ 1 ][ : -1 ]
numbersToPlot = [ ( int( x.split( "," )[ 0 ] ),
                    int( x.split( "," )[ 1 ] ),
                    x.split( "," )[ 2 ] )
                  for x in sys.argv[ 1 ].split( ";" ) ]
maxNumberRef = max( x[ 1 ] for x in numbersToPlot )
_, columns = os.popen('stty size', 'r').read().split()
sizeOfMaxNumberRef = int( columns ) / 2

# maxNumberRef will correspond to columns / 2
convertedNumbersToPlot = [ ( ( x[ 0 ] * sizeOfMaxNumberRef ) / maxNumberRef ,
                             ( x[ 1 ] * sizeOfMaxNumberRef ) / maxNumberRef ,
                             x[ 2 ] )
                             for x in numbersToPlot ]

for index, values in enumerate( convertedNumbersToPlot ):
    act, ref, task = values
    print task
    print '=' * act, " ( %s ) " % numbersToPlot[ index ][ 0 ]
    print '=' * ref, " ( %s ) " % numbersToPlot[ index ][ 1 ]
    print ''
