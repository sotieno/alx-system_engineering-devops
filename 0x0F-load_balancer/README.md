# 0x0F. Load balancer

In this project, I work with 3 web servers and use HAProxy (a TCP software load balancer) to distribute the workload on my servers. The goal is to improve my web stack so that there is redundancy for my web servers. This will allow me to be able to accept more traffic by doubling the number of web servers, and to make my infrastructure more reliable. If one web server fails, I will still have a second one to handle requests.

Project tasks are executed by writing Bash scripts to automate the work of configuring a brand new Ubuntu server to match the task requirements.
