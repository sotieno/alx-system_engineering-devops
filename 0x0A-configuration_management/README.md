# 0x0A Configuration management

In this project, I get familiar with confifuration managemen (CM) using Puppet. Configuration management refers to the process of systematically handling changes to a system in a way that it maintains integrity over time.

## Requirements

* All files are to be interpreted on Ubuntu 20.04 LTS
* All files are to end with a new line
* A README.md file at the root of the folder of the project is mandatory
* All Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* All Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* All Puppet manifests files must end with the extension .pp
* Ubuntu 20.04 VM should have Puppet 5.5 preinstalled

### Install Puppet

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

### Install puppet-lint

```
$ gem install puppet-lint
```

