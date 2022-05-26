This folder contains scripts used to run various permission actions in bash
0-iam_betty changes user to betty
1-who_am_i prints effective username of current user
1-who_am_i prints all groups of current user
3-new_owner changes owner of the file hello to user betty
4-groups creates an empty file called hello
5-execute adds execute permission to hello file
6-multiple_permissions script adds execute permission to the owner and group owner, and read permission to other users, to the file hello
7-everybody script adds execute permission to the owner, group owner and other users, to the file hello
8-James_Bond script sets no permission to owner and group and all permissions to others in the hello file
9-John_Doe script sets -rwxr-x-wx permission to hello file
10-mirror_permission script mirrors permissions of file named olleh to hello file
