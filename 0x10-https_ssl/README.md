# 0x10. HTTPS SSL
## Learning Objectives:bulb:
This project is aimed at learning :

* The 2 main roles of HTTPS SSL
* The purpose encrypting traffic
* What SSL termination means

---
### [0. World wide web](./1-world_wide_web)
* Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01).
Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

### [1. HAproxy SSL termination](./1-haproxy_ssl_termination)
* “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.s
