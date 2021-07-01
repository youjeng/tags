# Tags - An Exercise for Practicing Project Collaboration in git

*Goal*: Your team will become comfortable collaborating with git by making changes to this code base and delivering them on `master`, eventually culminating in an app like the one on the `sample-solution` branch. 

*Objective*: The tags webapp will list tags and store more tags, using a SQLite database.  It will also display an image, woohoo.  However, right now this app doesn't even say "Hello, World!".  It needs you.  Using git, you and your team will collaborate to make it better.

As your team begins to deliver completed tasks, you will run into challenges (merge conflicts!) associated with working in parallel on a code base, and you will practice using git to solve them.

The `master` branch is a working version of an empty app.  To help keep things simple, the `sample-solution` branch is provided as a reference.  Each commit on the `sample-solution` branch is also a working version.  The goal here is not to learn new programming language material, but to learn new git-based code collaboration skills .

Keep the app working as you deliver each change to `master`. &nbsp;&nbsp;Don't "break the build"!

## Setting Up For Running The Webapp
Setup is covered in the [Prework for Session One](https://walquis.github.io/tags/session-1-prework).

## How To Run The Project Collaboration Exercise
To keep focused on git (as opposed to Github), we will not be using any Github workflow operations apart from the fork operation.
1. *Team Lead* - Fork this repo and grant read/write access to the rest of the team.
1. *Each Member* - `git clone` your team lead's forked copy to your local machine.
1. *Whole Team* - Take a look at the commits on `sample-solution`, and agree as a team how you'll divide each task.  (`git show` and `git diff` will come in handy here!)
1. *Each Member* - Implement your assigned features.  Below is a workflow description you may find useful.

## A Sample Collaborative Workflow
Start on `master`.  Catch up with your team's changes via a `git pull`. Start a new local branch, and implement your feature (which for this exercise you would do by replicating the changes from a commit on the `sample-solution` branch).  Test your changes.

Go back to `master` for merging.  Before merging, it's a good idea to do a `git pull` first, just in case changes have been delivered since you last branched from `master`. (In that case, you'll need to go back to your feature branch and  merge from `master` before delivering!)

Assuming you're back on `master`, go ahead and merge your feature.  After merging to `master` but before pushing up to the shared team repo, don't forget to test the website and make sure it still works.

Expressing this workflow in a list format:
1. `git checkout master` - The branch where your team will rendezvous with changes.
1. `git pull origin master` - Catch your local master up with latest changes from your team.
1. `git checkout -b mytask` - Create and go to a new task branch from `master`.
1. `git cherry-pick 38f2a98` - Replay a commit onto `mytask` (may require resolving conflicts).
1. `git checkout master` - Go to `master` in prep for bringing your stuff in.
1. `git pull origin master` (in case more changes have been pushed by teammates).
1. (If there *are* more changes, go back to `mytask` and merge 'em in.  Then tell your team to hold off, it's your turn now!).
1. `git merge mytask` - Assuming you're back on master at this point.
1. `git push origin master` - Share your scintillating creativity with your team.

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

