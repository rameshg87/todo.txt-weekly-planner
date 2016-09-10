# Weekly planner addon

## Overview

The basic idea of this planning mechanism is that on a per-week basis, we want
to dedicate a certain percentage of time for various task groups. Total amount
of time available for each task groups is mentioned in the allocations.conf
file. This addon and its associated commands help to make sure that we spend
the desired amount of time in various task groups. It displays the tasks as
per priority until we run of time this week for the task group. A task group
is a particular combination of a +project and @context. For example:

```
+office @reviews
+office @learn
+personal
```

Some important points:
* All units of time are in minutes. 
* Week starts on Sunday.

## Installing the addon

```
cd ~/.todo.actions.d
git clone https://github.com/rameshg87/todo.txt-weekly-planner wp
```

## allocations.conf

A sample is provided in allocations.conf.sample.

Something like below can be mentioned if we want to allocate 5 hours for
review, 25 hours for ProjectX, 5 hours for maintenance and 10 hours to learn.
All units are in minutes.

```
+office @review:300
+office +projectX @code:1500
+office @maintenance:300
+office @learn:600
```

## Commmands

* Displaying the allocations for each project and the time remaining for each
  one of them. This is same as doing a cat on allocations.conf file.

  ```
  todo.sh wp alloc[ations]
  ```

* Displaying the summary for this week.

  ```
  todo.sh wp sum[mary]
  ```

* The remaining tasks that need to completed in the week.

  ```
  todo.sh wp ls
  ```

* The remaining tasks is reviews that need to completed in the week.

  ```
  todo.sh wp ls "+office @reviews" 
  ```

* Add the tasks using wp to prevent adding tasks without estimates.

  ```
  todo.sh wp add "review code +office @reviews" 
  ```

## Requirements:

* All tasks need to have an estimate. This should be with the "est:" tag and
  time should be mentioned in minutes. Use "todo.sh wp add" to make sure
  we always add tasks with estimates. Example:
  ```
  Prepare design doc +office est:60
  ```

* The actual duration taken for the task should be either
  populated with [donow addon](https://github.com/clobrano/todo.txt-cli/blob/master/todo.actions.d/donow)
  or should be added manually. If it doesn't exist, then it is assumed that the task 
  took the estimate time exactly. For example a completed task can look like either
  of the below:
  ```
  Complete task Y +office est:60
  Prepare design doc +office est:60 min:90
  ```
