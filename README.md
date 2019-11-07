# AirBnB clone - The console

A shell is a command-line interpreter that provides a command line user interface for Unix-like operating systems. The shell is both an interactive command language and a scripting language, and is used by the operating system to control the execution of the system using shell scripts.

## Description

Our simple version of a shell, it takes a command as an input and check if it's a built-in or an alias, if it's, it'll proceed with the instructions given for each case, in case it's not, our shell will check into each address taken from the global variable PATH for a file who has the same name as the command entered into our program, once a file with the same name is found in any of the paths, the program will check if it's executable, in case it's, exceve will execute the command and the parameters passed

## Usage

This project should be compiled with the following command:
```bash
gcc -Wall -Wextra -Werror -pedantic -Wno-format *.c -o shell
```

Then you can easily run './shell' to enter the intractive mode, or you can also send an input to use the non-interactive mode (e.g. echo 'ls' | ./shell)

## Commands Samples

```c
#cisfun$ ls -l
#cisfun$ /bin/ls

```

## Contributors

* Monica Jaimes
* Jhon Arias

## Contributing
Pull requests are welcome.