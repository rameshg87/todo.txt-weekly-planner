The basic idea of this planning mechanism is that on a per-week basis, we want
to dedicate a certain percentage of time for various task groups. Total amount
of time available for each task groups is mentioned in the JSON file. This
addon can help in doing the following:
* Displaying the allocations for each project and the time remaining for each
  one of them.
  todo.sh wp allocations
* Displaying the summary for this week.
  todo.sh wp summary
* The remaining tasks that need to completed in the week.
  todo.sh wp ls "+office" 
* A report of actual duration planned vs actual duration spend (Use in 
  conjunction with donow addon to track how much time we actually spent on the
  task). TODO

Requirements:
* All tasks need to have an estimate. This should be with the "est:" tag and
  time should be mentioned in minutes. Example:
  "Prepare design doc +office est:60"
* For weekly report, the actual duration taken for the task should be either
  populated with donow addon or should be added manually. If it doesn't exist
  then it is assumed that the task took the estimate time exactly. Example:
  "Prepare design doc +office est:60 min:90"
