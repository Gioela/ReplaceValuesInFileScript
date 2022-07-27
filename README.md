# **ReplaceValuesInCsv**

Replace Values in csv is a Python script that creates a new file from the first but with the replacement values.
This script could be executed from command line in two different ways: with default or custom list substitutions.

The input parameters are:

| Params | What it does |
| ------ | ------------ |
| **InPath** | with the file name and its extension, it is the input file path |
| **OutPath** | with the file name and its extension, it is the output file path, where the new file will be saved |
| **ValuesListToReplace** | Optional. If it is declared it must be a string with an even number of elements where previuos value will be substituted by its follow |


## **How to use**

### Default
From git shell:
```
python replace_values_in_csv.py "~\CsvFileName.csv" "~\CsvFileName.csv"
```

From CommandPrompt:
```
replace_values_in_csv.py "~\CsvFileName.csv" "~\CsvFileName.csv"
```

### Custom
From git shell:
```
python replace_values_in_csv.py "~\CsvFileName.csv" "~\CsvFileName.csv" "* x , ; ; ."
```

From CommandPrompt:
```
replace_values_in_csv.py "~\CsvFileName.csv" "~\CsvFileName.csv" "* x , ; ; ."
```

## Tested
It tested on Win on GitBash Shell and on CommandPrompt.


### Note
This project is licensed under the terms of the MIT license.
