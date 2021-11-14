# aWaifu - Mass Waifu Profile generator
Python module to randomly generate waifus' profiles in mass scale.
<br>

## Wanna try it out?
<img src="https://github.com/git-akihakune/aWaifu-Colab/blob/main/img/random_example.png?raw=true">
<br>

If you'd like to try out the module with out any installation, I suggest <a href="https://github.com/git-akihakune/aWaifu-Colab">try the Google Colab notebook version first</a>.
<br>

## Installation
You can install directly from PyPi:
```bash
pip install aWaifu
```
<br>
Or get the `.whl` from https://github.com/git-akihakune/aWaifu/releases/tag/v0.1.1.

## Usage
To run with default options:
```bash
python -m aWaifu
```

## Scripting
First, create a `Waifus` object:

```python
from aWaifu.utils import Waifus

waifuGen = Waifus()
```
<br>

You can customize the script's behaviour from your object. Here is a quite self-explained list of options:
```python
numberOfProfiles: int = 10, # number of profiles going to generate
verbose: bool = False, # verbose mode 
multiCultures: bool = True, # False: limit to Japanese profiles only
bigWaifu: bool = False, # larger images, with watermark
noProfile: bool = False, # do not generate profiles
noImage: bool = False, # generate profiles without picture
autoCloseImage:bool = True, # automatically close opened images from verbose
faster: bool = False, # do not assert delays between requests
```
<br>

Therefore, the default script actually is:
```python
waifuGen = Waifus(numberOfProfiles=5, verbose=True, bigWaifu=True)
```
<br>

Next, generate the profiles:
```python
waifuGen.generateProfiles()
```
<br>

The results will be saved to `waifus/` directory. Previous results will be overwritten. If you want to save the results to a *zip* file:
```python
Waifus.getAllInfo()
```
<br>

## Development
This module is initially [a Google Colab Python Notebook](https://github.com/git-akihakune/aWaifu-Colab), with some added details. Therefore, it's not been carefully developed. Every issue, pull request or suggestion is deeply appreciated.
