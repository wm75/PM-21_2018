import sys
import os

from qft import standardize
from qft import evaluate
from qft import parse_input


fname = sys.argv[1]
if os.path.isdir(fname):
    fname = [os.path.join(fname, f) for f in sorted(os.listdir(fname))]
else:
    fname = [fname]
    
for f in fname:
    print('Ergebnisse fuer Datei', f)
    data_in = open(f, 'r')
    data, layout = parse_input.parse_input(data_in)
    data_in.close()
    
    conc, status = standardize.transform_to_concs(
            data, layout
            )
    
    patientrecords = parse_input.get_patient_records(
            conc, layout
            )
    
    for patient, record in sorted(patientrecords.items()):
        test_result = evaluate.evaluate_patient(record)
        if '--exclude-negative' in sys.argv:
            if test_result == 0:
                continue
        if test_result == 1:
            outcome = 'positiv'
        elif test_result == 0:
            outcome = 'negativ'
        else:
            outcome = 'nicht beurteilbar'
        print(
                'Ergebnis für Patient {0} ist {1}.'
                .format(patient, outcome)
                )
    
