This folder contains scripts used to run various permission actions in bash
0-iam_betty changes user to betty
1-who_am_i prints effective username of current user
2-groups prints all groups of current user
3-new_owner changes owner of the file hello to user betty
4-groups creates an empty file called hello
5-execute adds execute permission to hello file
6-multiple_permissions script adds execute permission to the owner and group owner, and read permission to other users, to the file hello
7-everybody script adds execute permission to the owner, group owner and other users, to the file hello
8-James_Bond script sets no permission to owner and group and all permissions to others in the hello file
9-John_Doe script sets -rwxr-x-wx permission to hello file
10-mirror_permission script mirrors permissions of file named olleh to hello file
11-directories_permissions script adds execute permission to all subdirectories of current directory for owner, group and all others leaving files unchanged
12-directory_permissions creates a directory called my_dir and sets permissions to 751
13-change_group changes group owner to school for hello file
100-change_owner_and_group changes the owner to vincent and the group owner to staff for all the files and directories in the working directory
101-symbolic_link_permissions changes the owner and group owner of _hello to vincent and staff, _hello is a symbolic link
102-if_only changes owner of hello file to betty only if it is owned by guillaume
103-Star_Wars plays swar wars in the terminal
