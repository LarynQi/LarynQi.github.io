#!/bin/sh

# https://stackoverflow.com/questions/42368504/how-to-correctly-add-git-push-command-to-crontab-ubuntu
# https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx/
# https://medium.com/better-programming/https-medium-com-ratik96-scheduling-jobs-with-crontab-on-macos-add5a8b26c30

# PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin
PATH=/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin

GIT=`which git`
REPO_DIR=~/cs/LarynQi.github.io/
cd ${REPO_DIR}

# 9/14/23
${GIT} add fa23.html
${GIT} add assets/fa23/disc03-sol.pdf
${GIT} commit -m "autorelease cs61a fa23 disc03 sols"
${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 9/7/23
# ${GIT} add fa23.html
# ${GIT} add assets/fa23/disc02-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa23 disc02 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 8/28/23
# ${GIT} add fa23.html
# ${GIT} add assets/fa23/disc01-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa23 disc01 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/17/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc08.pdf
# ${GIT} add assets/sp23/disc08-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc08 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/7/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc07.pdf
# ${GIT} add assets/sp23/disc07-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc07 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/2/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc06.pdf
# ${GIT} add assets/sp23/disc06-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc06 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/17/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc04.pdf
# ${GIT} add assets/sp23/disc04-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc04 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/10/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc03-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc03 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 1/27/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc02-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc02 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# 1/26/23
# ${GIT} add sp23.html
# ${GIT} add assets/sp23/disc01-sol.pdf
# ${GIT} commit -m "autorelease cs61a sp23 disc01 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/18/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc12-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/4/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc10-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc10 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/21/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc08-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc08 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/14/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc07-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc07 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/6/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc06-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc06 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 9/30/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc05-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc05 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 9/23/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc04-sol.pdf
# ${GIT} commit -m "autorelease cs61a fa21 disc04 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 9/16/21
# ${GIT} add fa21.html
# ${GIT} add assets/fa21/disc03-sol.pdf
# ${GIT} commit -m "auto release cs61a fa21 disc03 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 9/2/21
# ${GIT} add assets/fa21/disc01-sol.pdf
# ${GIT} commit -m "auto release cs61a fa21 disc01 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 8/26/21
# ${GIT} add assets/fa21/disc00-sol.pdf
# ${GIT} commit -m "auto release cs61a fa21 disc00 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 8/11/21
# ${GIT} add assets/su21/mentor13_sol.pdf
# # ${GIT} add assets/su21/mentor12_sol.sql
# ${GIT} commit -m "auto release cs61a tut13 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 8/6/21
# ${GIT} add assets/su21/mentor12_sol.sql
# ${GIT} add assets/su21/mentor12_sol.sql
# ${GIT} commit -m "auto release cs61a tut12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 8/4/21
# ${GIT} add assets/su21/mentor11_sol.scm
# ${GIT} add assets/su21/mentor11_sol.pdf
# ${GIT} commit -m "auto release cs61a tut11 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 7/28/21
# ${GIT} add assets/su21/mentor09_sol.scm
# ${GIT} add assets/su21/mentor09_sol.pdf
# ${GIT} commit -m "auto release cs61a tut09 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 7/23/21
# ${GIT} add assets/su21/mentor08_sol.py
# ${GIT} add assets/su21/mentor08_sol.pdf
# ${GIT} commit -m "auto release cs61a tut08 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 7/21/21
# ${GIT} add assets/su21/mentor07_sol.py
# ${GIT} add assets/su21/mentor07_sol.pdf
# ${GIT} commit -m "auto release cs61a tut07 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 7/9/21
# ${GIT} add assets/su21/mentor05_sol.py
# ${GIT} add assets/su21/mentor05_sol.pdf
# ${GIT} commit -m "auto release cs61a tut05 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 7/7/21
# ${GIT} add assets/su21/mentor04_sol.py
# ${GIT} add assets/su21/mentor04_sol.pdf
# ${GIT} commit -m "auto release cs61a tut04 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 6/30/21
# ${GIT} add assets/su21/mentor02_sol.py
# ${GIT} add assets/su21/mentor02_sol.pdf
# ${GIT} commit -m "auto release cs61a tut02 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 6/25/21
# ${GIT} add assets/su21/mentor_01_sol.py
# ${GIT} add assets/su21/mentor_01_sol.pdf
# ${GIT} commit -m "auto release cs61a tut01 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/29/21
# ${GIT} add assets/sp21/sol14.zip
# ${GIT} commit -m "auto release cs61a disc14 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/27/21
# ${GIT} add assets/sp21-csm/61a-15-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol15.zip
# ${GIT} commit -m "auto release csm61a week15 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/22/21
# ${GIT} add assets/sp21/sol13.zip
# ${GIT} commit -m "auto release cs61a disc13 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/15/21
# ${GIT} add assets/sp21/sol12.zip
# ${GIT} commit -m "auto release cs61a disc12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/8/21
# ${GIT} add assets/sp21/sol11.zip
# ${GIT} commit -m "auto release cs61a disc11 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/6/21
# ${GIT} add assets/sp21-csm/61a-12-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol12.zip
# ${GIT} commit -m "auto release csm61a week12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 4/1/21
# ${GIT} add assets/sp21/sol10.zip
# ${GIT} commit -m "auto release cs61a disc10 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/30/21
# ${GIT} add assets/sp21-csm/61a-11-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol11.zip
# ${GIT} commit -m "auto release csm61a week11 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/16/21
# ${GIT} add assets/sp21-csm/61a-09-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol09.zip
# ${GIT} commit -m "auto release csm61a week09 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/11/21
# ${GIT} add assets/sp21/sol07.zip
# ${GIT} commit -m "auto release cs61a disc07 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/9/21
# ${GIT} add assets/sp21-csm/61a-08-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol08.zip
# ${GIT} commit -m "auto release csm61a week08 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/4/21
# ${GIT} add assets/sp21/sol06.zip
# ${GIT} commit -m "auto release cs61a disc05 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 3/2/21
# ${GIT} add assets/sp21-csm/61a-07-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol07.zip
# ${GIT} commit -m "auto release csm61a week07 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/14/21
# ${GIT} add assets/sp21-csm/sol05.zip
# ${GIT} commit -m "auto release cs61a disc05 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/23/21
# ${GIT} add assets/sp21-csm/61a-06-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol06.zip
# ${GIT} commit -m "auto release csm61a week06 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/11/21
# ${GIT} add assets/sp21-csm/sol03.zip
# ${GIT} commit -m "auto release cs61a disc03 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/9/21
# ${GIT} add assets/sp21-csm/61a-04-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol04.zip
# ${GIT} commit -m "auto release csm61a week04 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io


# # 2/3/21
# ${GIT} add assets/sp21/sol02.zip
# ${GIT} commit -m "auto release cs61a disc02 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 2/1/21
# ${GIT} add assets/sp21-csm/61a-03-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol03.zip
# ${GIT} commit -m "auto release csm61a week03 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 1/27/21
# ${GIT} add assets/sp21/sol01.zip
# ${GIT} commit -m "auto release cs61a disc01 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 1/25/21
# ${GIT} add assets/sp21-csm/61a-02-sol.pdf
# ${GIT} add assets/sp21-csm/mentor_sol02.zip
# ${GIT} commit -m "auto release csm61a week02 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 12/4/20
# ${GIT} add fa20-csm.html
# ${GIT} add assets/fa20-csm/61b-15-sol.pdf
# ${GIT} add assets/fa20-csm/kClosestSol.java
# ${GIT} commit -m "auto release csm61b week15 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 12/3/20
# ${GIT} add assets/fa20-csm/61a-15-sol.pdf
# ${GIT} add assets/fa20-csm/sol15.zip
# ${GIT} commit -m "auto release csm61a week15 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/20/20
# ${GIT} add fa20-csm.html
# ${GIT} add assets/fa20-csm/61b-13-sol.pdf
# ${GIT} commit -m "auto release csm61b week13 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/19/20
# ${GIT} add assets/fa20-csm/sol13.zip
# ${GIT} add assets/fa20-csm/61a-13-sol.pdf
# ${GIT} commit -m "auto release csm61a week13 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/18/20
# ${GIT} add assets/fa20/sol12.zip
# # ${GIT} add fa20.html
# ${GIT} commit -m "auto release tut12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/13/20
# ${GIT} add assets/fa20-csm/61b-12-sol.pdf
# # ${GIT} add assets/fa20-csm/mentor12_sol.zip
# ${GIT} commit -m "auto release csm61b week12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/12/20
# ${GIT} add assets/fa20-csm/61a-12-sol.pdf
# ${GIT} add assets/fa20-csm/mentor12_sol.zip
# ${GIT} commit -m "auto release csm61a week12 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/6/20
# ${GIT} add assets/fa20-csm/61b-11-sol.pdf
# # ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61b week11 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 11/5/20
# ${GIT} add assets/fa20-csm/61a-11-sol.pdf
# ${GIT} add assets/fa20-csm/mentor11_sol.zip
# # ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61a week11 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/27/20
# ${GIT} add assets/fa20-csm/61a-10-sol.pdf
# # ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61a week10 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/23/20
# ${GIT} add assets/fa20-csm/61b-9-sol.pdf
# ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61b week09 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/22/20
# ${GIT} add assets/fa20-csm/61a-9-sol.pdf
# # ${GIT} add assets/fa20-csm/mentor09_sol.py
# ${GIT} commit -m "auto release csm61a week09 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/21/20
# ${GIT} add assets/fa20/tut08-sol.py
# # ${GIT} add assets/fa20-csm/mentor09_sol.py
# ${GIT} commit -m "auto release cs61a tut09 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/16/20
# ${GIT} add assets/fa20-csm/61b-8-sol.pdf
# # ${GIT} add assets/fa20-csm/mentor08_sol.py
# ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61b week08 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/15/20
# ${GIT} add assets/fa20-csm/61a-8-sol.pdf
# ${GIT} add assets/fa20-csm/mentor08_sol.py
# # ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61a week08 sols"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/8/20
# ${GIT} add assets/fa20-csm/61a-7-sol.pdf
# ${GIT} add assets/fa20-csm/mentor07_sol.py
# ${GIT} add fa20-csm.html
# ${GIT} commit -m "auto release csm61a week07 sol"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io

# # 10/1/20
# ${GIT} add assets/fa20-csm/61a-6-sol.pdf
# ${GIT} commit -m "auto release csm61a week06 sol"
# ${GIT} push git@github.com:LarynQi/LarynQi.github.io
