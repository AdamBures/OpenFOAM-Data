import matplotlib.pyplot as plt


class CheckResidual(object):
    def __init__(self, file):
        super(CheckResidual, self).__init__()
        self.file = file
        self.lst = {}
        self.data = open(self.file, "r")

    def get_data(self):
        self.data = list(self.data.readlines())[583:]
        for i in range(len(self.data)):
            if self.data[i].startswith("Courant"):
                self.lst[self.data[i]] = [self.data[i + 3], self.data[i + 21].split(", ")[2],
                                          self.data[i + 23].split(", ")[2], self.data[i + 24].split(", ")[2]]
        return self.lst

    def plot_data(self):
        x = [float(self.lst[i][0].split(" ")[-1]) for i in self.lst]
        p_rgh = [float(self.lst[i][1].split(" ")[-1]) for i in self.lst]
        omega = [float(self.lst[i][2].split(" ")[-1]) for i in self.lst]
        k = [float(self.lst[i][3].split(" ")[-1]) for i in self.lst]

        plt.xlabel("Time")
        plt.ylabel("Final residual")
        plt.plot(x, p_rgh, color='r', label='p_rgh')
        plt.plot(x, omega, color='g', label='omega')
        plt.plot(x, k, color='b', label='k')
        plt.legend()
        plt.show()

    def save_data(self):
        with open("result.txt", "w") as f:
            for i in self.lst:
                f.write(i)
                f.write(self.lst[i][0])
                f.write(f"p_rgh: {self.lst[i][1]}\n")
                f.write(f"omega: {self.lst[i][2]}\n")
                f.write(f"k: {self.lst[i][3]}\n")
                f.write("\n")


if __name__ == '__main__':
    res = CheckResidual("log.run")
    res.get_data()
    res.save_data()
    res.plot_data()
