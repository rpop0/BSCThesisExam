# BSC Exam test giver
Prerequisites:
- Python 3.9
- A terminal capable of showing colors and unicode characters (Git Bash, WSL)

When running main.py, you will be prompted to enter a file.
Simply give the name of the subject you want to be tested for (E.g, "ads.json").
Another alternative is to input the string "all", which uses the questions from all of the JSON files in the root folder.

The JSON files are under the following format:
```
{
  "In which of the following data structures does searching an item have worst-case complexity Θ(log n)? There may be more than one.": {
    "Linked lists.": false,
    "Heaps.": false,
    "Red-black trees, ": true,
    "Splay trees": false
  },
}
```
