# ass-pdf

Just a command line tool to automate the creatation & handing my assignment, which is a very tedious task for me to do.



## How it works?

1- clone the repo.
```bash
git clone git@github.com:yassa-alqess/ass-pdf.git
```
2- make sure that u have the dependencies (use pip pkg manager to get those dependencies).

3- add assignments images to `.img` dir.

4- finally run the script with some required arguments **in order**.
```bash
python3 init.py <title> <name> <id>
```

or if u own current repo, or u have an exec permission on it, u can just run `./init.py` + **arguments in order** for sure.

and to have such a permission, run the following shell command.
```bash
chmod +x init.py
```

=> The output is a pdf file on the same dir.
