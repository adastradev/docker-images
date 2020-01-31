# CSV Conversion mapping script

## Usage Examples
On the command line, move to the directory with your data file ```input.csv```. Once completed, your current directory will contain a file ```output.json``` containing your data.

### Running on Linux
```docker run --rm -it -v $(pwd):/data adastradev/map_csv /data/input.csv -o /data/output.json```

### Running on Windows (cmd)
```docker run --rm -it -v %cd%:/data adastradev/map_csv /data/input.csv -o /data/output.json```


### Running on Windows (PowerShell)
```docker run --rm -it -v $(PWD):/data adastradev/map_csv /data/input.csv -o /data/output.json```
