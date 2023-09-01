# generate-trance-songs
Generate a random trance playlist from `main.txt`.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
1. A complete install of `Python 3.x`.
2. Under `Notes\trance`, the `main.txt` file.

**Example**:
```
C:\Users\nso89\Notes\trance\main.txt
```

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract the `trancetools-main.zip`

**Example**:
```cmd
C:\Users\nso89\trancetools-main\generate-trance-songs
```

#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `generate-trance-songs` folder.

**Example**:
```cmd
C:\Users\nso89>cd trancetools-main\generate-trance-songs
```

2. Start the `main.py` script.

**Example**:
```cmd
C:\Users\nso89\trancetools-main\generate-trance-songs>python main.py
```

3. The output is displayed in the `cmd.exe`:
```
Benya With Shanokee - Sanctuary (Daniel Skyver Edit)      
Chicane ft. Moya Brennan - Saltwater (Kevin De Vries Edit)
Jones & Stephenson - The First Rebirth
Phynn ft. Jets Overhead - In Your Heart (Original Edit)   
Raz Nitzan ft. Jodie Knight - Eternally
```

4. If you want to write the songs to a `.txt` file, type `y`. It will be written to `YYYYMMDD-HHMMSS.txt` under `generate-trance-songs`.

```
Write to file (y/n): y

File Name: c:\Users\nso89\trancetools\generate-trance-songs\20230117-153150.txt 

Enjoy!
```

#### <a name="configuration"></a>Configuration
If you need to change the location of the `trance\main.txt`:
1. Open the `main.py` script in any text editor.
2. Locate the `MAIN_TXT` variable.

**Example**:
```python
MAIN_TXT = Path.home().joinpath("Notes\\trance\\main.txt")
```
3. When you finish changing the variables, save and close the editor.
