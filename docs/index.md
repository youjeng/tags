# Collaborating with git

## Introduction

In this two-session hands-on course, you will experience the essence of git by working in teams to improve a simple Python webapp, laying a foundation for collaborating in a professional environment.

This material has been presented to every CodePlatoon cohort since Bravo. Several graduates report that, equipped with a firm grasp of these git basics, they have become go-to git resources in their software engineering teams.

## About the instructor
As a devops professional with three-ish decades of experience in version control, I first experienced git in 2009 when developers insisted on bringing it into my company.  I learned a few basic survival commands, but it wasn't really clicking for me. Depressingly often, especially for a version control "expert", I got out of my depth and had to be rescued.  Eventually I tired of memorizing magic spells and decided to buckle down and learn the basics of git once-and-for-all.  Suddenly, git started making sense!  That feeling of enlightenment (and the jump in my productivity with git!) inspired this course.

## The Course In a Nutshell - Three objects, Three trees
You will get lots of practice expressing your changes in terms of git's data model - **three objects** - and moving them around in git's state model - **three trees**.
- The **three objects** - blob, tree, commit
- The **three trees** - HEAD, index, workspace

## Course Layout
- **[Prework](session-1-prework)** - Explore the Tags app's sample solution.  Your team will start from the `master` branch, and make changes to the app until it looks like the app on the `sample-solution` branch.  As prework, you will examine and run each of the commits from `master` (for each commit, the app is in a runnable although incomplete state), all the way to the tip of `sample-solution`.  These are the changes your team will collaborate on, dividing them up among the team and delivering them to `master`.
- **Session One** - Set up your team and environment.  Some basic Git, and some Linux/Bash.  See the [Syllabus](session-1-syllabus){:target="_blank"} and [Objects and Trees Handout](objects-and-trees-handout){:target="_blank"}.
- **Session Two** - Run the project with your team.  Handle merge conflicts.

## Homework - Between Session One and Session Two
In the Prework and Session One, you set up your development environment, got the webserver up and running, and went over the code.  You also likely considered the many contexts and nuances of the overloaded word 'environment'!  Finally, you got an oh-so-brief intro to The Three Objects and The Three Trees.  You have your project team together, and you're starting to think about how to tackle collaboratively the changes that need to be made.

To help you hit the ground running in Session Two, I suggest a bit of homework to more firmly embed the concepts we've covered: Familiarizing yourself with the Three Objects and Three Trees.  Work through the entire [Objects and Trees Handout](objects-and-trees-handout).  We'll have already touched on parts of it in Session One, but it's worth going all the way through.

The object of this homework is to familiarize with the two major concepts we touched upon at the end of Session One:
- The Three Objects - the git data model
- The Three Trees - managing local changes

Also, if for any reason you were not able to get your app up and running, *do the prework from the beginning.*  This includes deleting your fork on github.com, deleting or moving your local repo, and forking and cloning a fresh repo.  And please do let me know via Slack if anything is not working for you.

