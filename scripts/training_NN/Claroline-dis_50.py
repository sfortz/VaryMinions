import training_Model as minion

if __name__ == "__main__":

    for i in range(0, 10):
        print("Exécution " + str(i) + " : ")
        minion.main("claroline-dis_50.csv", "GRU", True, 50, 10, 128, 0.66, "sigmoid", "mse")

    #for i in range(0, 10):Claroline-dis_50-tensorflow.py
    #     print("Exécution " + str(i) + " : ")
    #     minion.main("claroline-dis_50.csv", "GRU", True, 20, 30, 128, 0.66, "sigmoid", "mse")

    # for i in range(0, 10):
    #      print("Exécution " + str(i) + " : ")
    #      minion.main("claroline-dis_50.csv", "LSTM", True, 20, 30, 128, 0.66)
    #
    # for i in range(0, 10):
    #      print("Exécution " + str(i) + " : ")
    #      minion.main("claroline-dis_50.csv", "GRU", True, 20, 10, 128, 0.66)
    #
    # for i in range(0, 10):
    #     print("Exécution " + str(i) + " : ")
    #     minion.main("claroline-dis_50.csv", "LSTM", True, 20, 10, 128, 0.66)
    #
    # for i in range(0, 10):
    #     prirun.shnt("Exécution " + str(i) + " : ")
    #     minion.main("claroline-dis_50.csv", "GRU", True, 20, 5, 128, 0.66)
    #
    # for i in range(0, 10):
    #     print("Exécution " + str(i) + " : ")
    #     minion.main("claroline-dis_50.csv", "LSTM", True, 20, 5, 128, 0.66)