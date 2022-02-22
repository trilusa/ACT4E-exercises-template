

## Setup

Install VS Code.

Select File -> Open and select *the entire folder*.

VS Code will propose to install "Dev Container". Click "install".

VS Code will give you a message similar to:

> Folder contains a Dev Container configuration file. Reopen folder to develop in a container.

Select "Reopen in container".

Now you should have the folder open while VS Code is in "container development mode".

Create a new terminal using Terminal -> New Terminal.

Run the following:

    make check-TestSimpleIntro

This will have created a file `out-results/result-TestSimpleIntro.html`.

From the file tree to the left, right-click the file and select "open preview". You will see the results of the testing.

Now browse the Python files in `src/`. Verify that autocompletion works..



