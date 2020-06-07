# sbs
Slackware Build System

## Description

For the Slackware64-riscv port, because of limited resources and normal changes of the main slackware64-current, I need a way to **queue** package compilation.

This will allow me to flag what packages I need rebuilt, and out of that:
- [ ] If SlackBuild ran without error, copy the package to a temporary place for review
- [ ] In any case, keep a log of the SlackBuild so any errors can be studied
- [ ] Allow to automate some manual checks done on completed packages, suck a checking how many files are in the generate package vs the previous or the main amd64 one, strips, etc
- [ ] A way to signal which packages have been inspected, for uploading to git.
- [ ] Slackware repo automation such as Changelog.txt, Checksums, MANIFESTs, etc
