# Tags - An Exercise for Practicing Project Collaboration in git

*Goal*: Your team will become comfortable collaborating with git by making changes to this code base and delivering them on `master`, eventually culminating in an app like the one on the `sample-solution` branch. 

*Objective*: The tags webapp will list tags and store more tags, using a SQLite database.  It will also display an image, woohoo.  However, right now this app doesn't even say "Hello, World!".  It needs you.  Using git, you and your team will collaborate to make it better.

As your team begins to deliver completed tasks, you will run into challenges (merge conflicts!) associated with working in parallel on a code base, and you will practice using git to solve them.

The `master` branch is a working version of an empty app.  To help keep things simple, the `sample-solution` branch is provided as a reference.  Each commit on the `sample-solution` branch is also a working version.  The goal here is not to learn new programming language material, but to learn new git-based code collaboration skills .

Keep the app working as you deliver each change to `master`. &nbsp;&nbsp;Don't "break the build"!

## Setting Up For Running The Webapp
Setup is covered in the [Prework for Session One](https://walquis.github.io/tags/session-1-prework).

## The Curriculum
The [Curriculum Introduction](https://walquis.github.io/tags) describes the content of the course, and references the Prework, the Syllabus, the Homework, and other teaching material.


## Hints For Viewing Repo Changes With Git Diff
Note that these diff'ing methods only compare commits, that is, changes *already committed to the repo*.  They don't address contents of your working directory or index.
1. See a given commit's diffs relative to its parent commit...

In this form of `git show`, you see ONLY a single commit's diffs, even if you provide a branch name instead of a sha.
```
$ git show 3f29a16  # (Not a real commit sha)
```
`git show` can be handy whenever you just want to see a single commit's worth of diffs.  You can do this from anywhere--there is no need, for instance, to get your workspace into a clean state, checkout a particular branch, and "git diff".

2. To view diffs on an entire branch, relative to another branch...
```
$ git diff master..sample-solution  # In diff output, master is on the left, sample-solution on the right
```
3. For some branch comparisons, you may want to exclude one or more files from the `git diff` output. For instance, no need to see the entire jquery file when it's added to the code base. Also no need to view diffs in the "docs" directory ...
```
$ git diff master..sample-solution ':(exclude)*jquery*.js' ':(exclude)docs/'
```

## More ways to view changes
**Look at them on github.com.** Navigate to https://github.com/walquis/tags/tree/sample-solution (or visit https://github.com/walquis/tags and choose `sample-solution` from the branch dropdown).  Then click "Contribute", directly under the green "Code" button, then "Compare".  This will show diffs with respect to `master`.

**Download [SourceTree](https://www.sourcetreeapp.com)** (or another git GUI, such as Github Desktop--but SourceTree is quite good), and point it at your local tags repo.

SourceTree nicely displays the branches that label the changes along the `sample-solution` branch.

![Viewing the Tags Repo in SourceTree](/docs/images/tags-repo-in-sourcetree.png)

In SourceTree, browse the changes, and explore the options for viewing changes--for instance, highlighting multiple commits with shift-click will show diffs across those commits (so you can, for example, see the sum of changes to get from "empty django web service", all the way to "hello world!"); also, the file viewer can switch from flat list to tree view; etc.

Your project team will be implementing these changes and delivering to `master`, but keep in mind that it's not necessary to use these commits or branches "as-is" or even at all.  They are just there as an example of how one might accomplish the task.  When your project team gets going, feel free to make use of these branches as little or as much as you please.

