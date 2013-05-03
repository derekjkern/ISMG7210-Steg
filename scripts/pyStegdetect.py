import subprocess
import getopt
import sys

#
# Process the incoming arguments and options
#
options, files_to_process = getopt.getopt( sys.argv[1:], "s:p:t:n:c:h?" )

#
# Turn the options into a dictionary
#
options = { options[i][0]:options[i][1] for i in range( 0, len( options ) ) }

#
# If the user called for help, then give it to them and quit
#
if "-h" in options or "-?" in options:
    print "pyStegdetect: Runs stegdetect and captures ROC coordinates and AUC"
    print "  Command Line:  python pyStegdetect.py  [options]  <files>"
    print ""
    print "  Options:"
    print "    -h            = Display this help"
    print "    -?            = Display this help"
    print "    -s <float>    = The initial sensitivity for stegdetect (default: 1.0)"
    print "    -p <float>    = The step to be added to sensitivity after each iteration"
    print "                    (default: 0.1)"
    print "    -n <int>      = The number of data points on the ROC to capture"
    print "                    (default: 10)"
    print "    -t <chars>    = The tests to run during analysis (default: p)."
    print "                    Tests:"
    print "                      j - jsteg"
    print "                      o - outguess"
    print "                      p - jphide"
    print "                      i - invisible secrets"
    print "                      f - F5"
    print "                      a - camoflage"
    print "    -c <filename> = Save the ROC coordinates within a CSV file."
    print ""
    print "  Notes:"
    print "    - The files passed may either be a series of file names or a wildcard,"
    print "      like *.jpg"
    print "    - The default test is only to look for outguess so this is not blind"
    print "      steganography"
    print "    - The default test setting for stegdetect is jopifa, which means that it"
    print "      tests for everything"

    sys.exit()

#
# Setup defaults
#
sensitivity = 1.0 if "-s" not in options else float( options['-s'] )
step = 0.1 if "-p" not in options else float( options['-p'] )
number_of_steps = 10 if "-n" not in options else int( options['-n'] )
tests = "p" if "-t" not in options else options['-t']

#
# Hold the ROC curve data points and the AUC
#
data = {
    "points": [],
    "AUC": 0
}

for i in range( 0, number_of_steps ):
    #
    # Setup the stegdetect args
    #
    stegdetect_args = [ "stegdetect", "-s", str( sensitivity + ( i * step ) ), "-t", tests ] + files_to_process
    
    #
    # Run stegdetect with the provided arguments. Capture the output so that it can be analyzed.
    #
    stegdetect_output = subprocess.check_output( stegdetect_args )
    
    #
    # Prepare to capture the confusion matrix.
    #
    confusion = { "TP": 0, "FP": 0, "TN": 0, "FN": 0, "P": 0, "N": 0 }
    
    #
    # Process the output line by line in order to populate the matrix.
    #
    for a_line in stegdetect_output.splitlines():
        predicted_positive = "negative" not in a_line and "skipped" not in a_line
        actual_positive = "cover" not in a_line
        
        #
        # Add to the matrix values
        #
        if predicted_positive:
            if actual_positive:
                confusion['TP'] += 1
            else:
                confusion['FP'] += 1
        else:
            if actual_positive:
                confusion['FN'] += 1
            else:
                confusion['TN'] += 1

        #
        # Record the actuals
        #
        if actual_positive:
            confusion['P'] += 1
        else:
            confusion['N'] += 1

    #
    # Calculate the data point for this step.
    #
    data['points'].append(
        (
            round( float( confusion['FP'] ) / float( confusion['N'] ), 4 ),
            round( float( confusion['TP'] ) / float( confusion['P'] ), 4 )
        )
    )

#
# Add first and last data points
#
data['points'] = [ ( 0.0, 0.0 ) ] + data['points'] + [ ( 1.0, 1.0 ) ]

#
# Calculate AUC using all of the data points
#
G = 0
for k in range( 1, len( data['points'] ) ):
    G += ( data['points'][k][0] - data['points'][k - 1][0] ) * ( data['points'][k][1] + data['points'][k - 1][1] )
data['AUC'] = 1 - ( ( 2.0 - G ) / 2.0 )

#
# Finally, output the data
#
if "-c" not in options:
    print data
else:
    #
    # First, simply output the AUC
    #
    print "AUC =", data['AUC']

    #
    # Next, write the data points to a CSV file
    #
    roc_file = open( options['-c'], "wb" )
    try:
        for k in range( 0, len( data['points'] ) ):
            #
            # Write each data point with a tab between
            #
            roc_file.write( str( data['points'][k][0] ) + "\t" + str( data['points'][k][1] ) + "\n" )
    finally:
        #
        # Make sure that the file gets closed.
        #
        roc_file.close()
