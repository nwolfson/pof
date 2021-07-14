import nidmm
with nidmm.Session("Dev1") as session:
    session.configure_measurement_digits(nidmm.Function.AC_VOLTS, 10, 5.5)
    print("Measured Volts: " + str(session.read())) * 100
    session.configure_measurement_digits(nidmm.Function.AC_CURRENT, 1, 5.5)
    print("Measured Current: " + str(session.read())) * 100
