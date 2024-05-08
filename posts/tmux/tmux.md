---
title: Tmux
author: Kartik Srinivas
---

## Using tmux



- Use `ctrl + b , ` to rename a window
- use the same with " for horizontal window
- use same with %  for a new vertical window
- Use the same with d to detach from the session running 

Use to re-attach to the session 

 `tmux ls &&  tmux attach -t [name]`

Use the following to rename a session 

`tmux  rename-session -t [prev_name]  [new_name]`


To start a new tmux session with a name

`tmux new -s [name]`


to delete a session 

`tmux kill-session -t [session_name]`

to kill a channel in the session 

`<Ctrl + B> + &`

