import waifulabs
import time
import os
import requests
import shutil
import json
import random
import psutil
from . import species
from PIL import Image
from typing import Dict


class Waifus:
    def __init__(
        self,
        dataPath: str = "waifus/",
        numberOfProfiles: int = 10,
        verbose: bool = False,
        multiCultures: bool = True,
        bigWaifu: bool = False,
        noProfile: bool = False,
        noImage: bool = False,
        autoCloseImage:bool = True,
        faster: bool = False,
    ):
        self.dataPath = dataPath
        self.numberOfProfiles: int = numberOfProfiles
        self.verbose = verbose
        self.multiCultures = multiCultures
        self.bigWaifu = bigWaifu
        self.noProfile = noProfile
        self.noImage = noImage
        self.autoCloseImage = autoCloseImage
        self.timeLimitBreak = faster

    # Methods are arranged from more public -> more private ones
    # The last method is an exception, as it's the main method of this class

    @staticmethod
    def cleanUpPreviousRuns() -> None:
        """Delete data from previous executions"""
        defaultDataDir: str = "waifus"
        shutil.rmtree(defaultDataDir, ignore_errors=True)

    @staticmethod
    def showWaifuImages() -> None:
        waifuImageDir: str = "waifus"

        if os.path.isdir(waifuImageDir):
            for filename in os.listdir(waifuImageDir):
                if filename.startswith("waifu-") or filename.endswith(".png"):
                    imagePath: str = waifuImageDir + "/" + filename
                    print(f"Showing: {imagePath}\n")
                    img = Image.open(imagePath)
                    img.show()
                    print("\n\n\n")

        else:
            raise FileNotFoundError("Make sure that you've generated some profiles")

    @staticmethod
    def getAllInfo() -> None:
        """Download every generated information under zipped format"""
        print("Zipping files... Please patiently wait...", end="\r")
        try:
            shutil.make_archive("waifus", "zip", "waifus")
            print("Files successfullly archived in 'waifus.zip'")
        except FileNotFoundError:
            print("Please make sure that you have generated 'waifus' directory first.")
            return None

    @staticmethod
    def getRandomAge() -> None:
        """Generate completely random, unrelated age"""
        return random.choice(
            [
                random.randint(3, 25),  # age of human waifu
                random.randint(10 ** 3, 10 ** 5),  # age of non-human waifu
            ]
        )

    @staticmethod
    def getRandomRace(age: int) -> str:
        """Randomizing a race"""
        humanHighestAge: int = 25

        NON_HUMAN_RACES = species.RACE_NAMES

        if age > humanHighestAge:
            return random.choice(NON_HUMAN_RACES)

        return random.choice(["Human", random.choice(NON_HUMAN_RACES)])

    def _vbose(self, contextType: str, context) -> None:
        """Logging, verbose messages and image showing"""
        if self.verbose:
            if contextType == "text":
                print(context, end="\n")
            elif contextType == "image":
                img = Image.open(context)
                img.show()
                print("\n\n\n")
            elif contextType == "dictionary":
                print(json.dumps(context, indent=4, ensure_ascii=False))
                print()
            else:
                print(f"Unknown type logging: {context}")

    def _getRandomProfile(self, imagePath: str):
        """Generate random profile"""

        profileDataPath: str = self.dataPath + "profile.json"

        # Using free, no-authentication Name Fake API
        apiHost: str = "https://api.namefake.com"

        if self.multiCultures:
            endPoint: str = apiHost + "/random/female"
        else:
            endPoint: str = apiHost + "/japanese-japan/female"

        call = requests.get(endPoint)
        rawData = call.json()

        # Because randomizing race depends on life span
        waifuAge = self.getRandomAge()
        waifuRace = self.getRandomRace(waifuAge)

        waifuData: Dict[str:str] = {
            "image": imagePath,
            "name": rawData["name"],
            "code_name": rawData["email_u"],
            "age": waifuAge,
            "race": waifuRace,
            "current_location": rawData["address"].replace("\n", " "),
            "birthday": rawData["birth_data"][5:],
            "representative_color": rawData["color"],
            "blood_type": rawData["blood"],
        }

        self._vbose("dictionary", waifuData)

        with open(profileDataPath, "a+") as f:
            f.write(json.dumps(waifuData, indent=4, ensure_ascii=False))
            f.write("\n\n\n")

    def _getRandomImages(self, filename: str) -> None:
        """Getting waifu images from waifulabs"""

        # close previous opened images
        if self.autoCloseImage:
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
                    break

        if self.bigWaifu:
            waifu = waifulabs.GenerateWaifu().GenerateBigWaifu()
        else:
            waifu = waifulabs.GenerateWaifu()

        waifu.save(self.dataPath + filename)
        self._vbose("image", self.dataPath + filename)

    def generateProfiles(self) -> None:
        """Generate full waifu profiles"""

        # Set up data directory the first run
        if not os.path.isdir(self.dataPath):
            os.mkdir(self.dataPath)

        for i in range(self.numberOfProfiles):
            self._vbose("text", f"ID: {i + 1}/{self.numberOfProfiles}\n")

            if not self.noProfile:
                self._getRandomProfile(imagePath=self.dataPath + f"waifu-{i + 1}.png")
            if not self.noImage:
                self._getRandomImages(filename=f"waifu-{i + 1}.png")

            if not self.timeLimitBreak:
                time.sleep(0.75)  # try not to DOS Waifulab's servers
        
        # Clear remaining image
        if self.autoCloseImage:
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
                    break