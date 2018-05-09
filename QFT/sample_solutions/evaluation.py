def evaluate_patient(patient_data):
    """Decide on a patient's test result.

    Takes as its argument a sequence of four elements interpreted as
    the measured IFN-gamma levels from a single patient in the following
    order:
    test sample 1, test sample 2, negative control, positive control

    Returns:
      1  if the data suggests a POSITIVE test result,
      0  if the data suggests a NEGATIVE test result,
     -1  if the data is inconclusive
    """
    
    # lesbare Benennung aller im weiteren benötigten Werte
    neg_control = patient_data[2]
    delta1 = patient_data[0] - neg_control
    delta2 = patient_data[1] - neg_control
    delta_pos = patient_data[3] - neg_control

    # Entscheidungsbaum
    if neg_control > 8:
        return -1
    if delta1 >= 0.35 and 100*delta1/neg_control >= 25:
        return 1
    if delta2 >= 0.35 and 100*delta2/neg_control >= 25:
        return 1
    if delta_pos < 0.5:
        return -1
    return 0


def test_it(patient_data, expect):
    print('Testing with', patient_data, '...', end=' ')
    result = evaluate_patient(patient_data)
    if  result == expect:
        print('passed.')
    else:
        print('FAILED!', 'Expected', expect, ', got', result, '.')


if __name__ == '__main__':
    test_data_sets = [
        ((1.1, 1.1, 0.1, 1.9), 1),     # clearly positive test
        ((1.1, 1.1, 0.1, 0.1), 1),     # positive control irrelevant
        ((1.1, 0.0, 0.1, 1.9), 1),     # one positive sample sufficient
        ((0.0, 1.1, 0.1, 1.9), 1),     #  -"-
        ((0.0, 1.1, 0.1, 0.1), 1),     # positive control still irrelevant
        ((1.1, 1.1, -0.1, 1.9), 1),    # negative value for negative control
        ((1.1, 1.1, 0.0, 1.9), 1),     # zero value for negative control
        ((5, 5, 1, 5), 1),             # all-integer data

        ((0.0, 0.0, 0.1, 1.9), 0),     # clearly negative test
        ((0.0, 0.0, -0.1, 1.9), 0),    # negative value for negative control
        ((8.5, 8.5, 8.0, 10.0), 0),    # relative difference < 25%
        ((0.35, 0.35, 0.01, 10.0), 0), # difference < 0.35
        ((0.34, 0.34, 0.0, 10.0), 0),  # zero value for negative control
        
        ((20.0, 20.0, 8.1, 20.0), -1), # high negative control
        ((0.0, 0.0, 0.1, 0.49), -1)    # negative, but failed positive control
        ]

    for data, expect in test_data_sets:
        test_it(data, expect)
