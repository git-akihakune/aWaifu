from .utils import Waifus

def main():
    waifuGen = Waifus(numberOfProfiles=5, verbose=True, bigWaifu=True)
    waifuGen.generateProfiles()

if __name__ == '__main__':
    main()