### csv to xlsx
This is a simple csv to xlsx converter focused on low memory usage.
For this I use lib [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) with [constant_memory](https://xlsxwriter.readthedocs.io/working_with_memory.html?highlight=constant) enabled

### requirements
- pipenv - https://pipenv.pypa.io/en/stable/

#### installing
```bash
make install
```

#### running
```bash
pipenv run python xlsx.py -i my_file.csv -o output.xlsx
```

Example - see the output in the `examples` folder
```bash
make run/example
```



