import sys
import glob
import matplotlib.pyplot as plt
from natsort import natsorted, ns
from time import time
from Algorithms import kmp, dynamic_lcss, naive_lcss

sys.setrecursionlimit(15000)

kmp_times = []
naive_lcss_times = []
dynamic_lcss_times = []

src_dataset = natsorted(
    glob.glob("Data\external-detection-corpus\source-documents\*.txt"), alg=ns.IGNORECASE)

sus_dataset = natsorted(
    glob.glob("Data\external-detection-corpus\suspicious-documents\*.txt"), alg=ns.IGNORECASE)


def testAlgorithm(myFunction, time_array: list, algoName: str):
    for i in range(10):
        src_file = src_dataset[i]
        sus_file = sus_dataset[i]

        # length of source file + length of sus file
        input_size = len(open(src_file, encoding="utf-8").read()) + \
            len(open(sus_file, encoding="utf-8").read())

        print("Running " + algoName + " on documents number " + str(i+1))
        # Run algorithm and measure running time
        t0 = time()
        myFunction(src_file, sus_file)
        t1 = time()

        time_array.append([t1-t0, input_size])

    # Running time sorted by input size
    time_array.sort(key=lambda x: x[1])

    # Plotting the running times
    running_times = [x[0] for x in time_array]
    input_sizes = [x[1] for x in time_array]

    plt.plot(input_sizes, running_times, label=algoName)
    plt.xlabel("Input size")
    plt.ylabel("Running time")
    plt.legend()
    plt.savefig("Plots/" + algoName + ".png")


# TODO: Add new algorithm and add comparison functions

testAlgorithm(kmp.runKMP, kmp_times, "KMP")
testAlgorithm(naive_lcss.runLCSS_naive, naive_lcss_times, "Naive LCSS")
testAlgorithm(dynamic_lcss.runLCSS_dynamic, dynamic_lcss_times, "Dynamic LCSS")
