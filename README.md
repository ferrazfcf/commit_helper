# Commit Helper
![](https://github.com/ferrazfcf/commit_helper/blob/main/image.png)

## What is it?

This is a Python script to help on commits creation.
Inspired on Kugra's https://github.com/Kugra/branch_name_helper

## How to use (macOS)

1. Download *__main.py__* file
1. Rename the file extension to *__.app__*
1. On terminal run *__chmod +x main.app__*
1. Run the application

## What each field means?

* _Arguments_ choose which arguments to use
    1. _Add All_ add argument "-a" 
    1. _Amend_ add argument "--amend"
    1. _No Edit_ add argument "--no-edit"
* _Commit prefix_ set a prefix to commit "[prefix]", will be set to upper case
* _Commit Message_ set a message to commit

## E.G.

Label | Field
------------ | -------------
Arguments | _Add All_
Task prefix | jupiter-2020
Task name | got TO Jupiter

Result: **git commit -a -m "[JUPITER-2020] got TO Jupiter"**
```diff
- Once you hit the button the result will be shown on field under the button and will be on your clipboard.
```
