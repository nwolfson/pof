import nidmm
import matplotlib.pyplot as plt
import numpy as np
with nidmm.Session("Dev1") as session:
    session.configure_multi_point(trigger_count=1, sample_count=5, sample_trigger=nidmm.SampleTrigger.IMMEDIATE)
    Volts = session.read_multi_point(array_size=5)
    Volts = list(Volts)
    print("Measurement: " + str(Volts))

    time = np.linspace(0, 5, 5)
    plt.figure(dpi=170)
    plt.plot(time, Volts, color='r', linewidth=2)
    plt.xlabel('Time', fontsize=10)
    plt.ylabel('Volts', fontsize=10)
    plt.grid()
    plt.show()

    session.abort()