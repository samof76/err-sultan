## Sultan

Sultan is an errbot plugin to, to get information from a host on cetain aspects of the system. It is named so, because it's heavily dependent on the [Sultan](http://sultan.readthedocs.io/en/latest/), a great library to run remote commands.

Please note all these bot commands are read only commands, and do not really harm the system in anyway.

### Installation

As Errbot admin for your Chat client tell errbot to install sultan,

```
!repos install https://github.com/samof76/err-sultan.git
```

For all the commands to work, you would have setup your(errbot installation) `~/.ssh/config`, in such a way that you each of the `<hostname>` in defined with their connection parameters.

Also you will might want to configure the plugin, to use a specific user(to SSH), by default it is `root`, you could change this using the following command.

```
!plugin config Sultan {'username': 'samof76'}
```
### Usage

Sultan comes with the following bot commands prebuilt into it. 

#### Get Uptime

```
!sultan_get_uptime [-h] hostname
```
This command will run the `sudo uptime` on `<hostname>`, prints the output for you.

#### Get Disk Usage

```
!sultan_get_disk_usage [-h] <hostname>
```
This commands will run the `sudo df -h;` on `<hostname>`, prints the output for you.

#### Get Memory Usage

```
!sultan_get_memory_usage [-h] hostname
```
This command will run `sudo free -m` on `<hostname>`, prints the output for you.

#### Get Monit Status

```
!sultan_get_monit_status [-h] hostname
```
This command will run `sudo monit status` on `<hostname>`, prints the output for you.

#### Get Monit Summary

```
!sultan_get_monit_summary [-h] hostname
```
This command will run `sudo monit summary` on `<hostname>`, prints the output for you.

#### Get Mount Points

```
!sultan_get_mount_points [-h] hostname
```
This command will run `sudo mount` on `<hostname>`, prints the output for you.

#### Get Passenger Status

```
!sultan_get_passenger_status [-h] hostname
```
This command will run `sudo passenger-status` on `<hostname>`, prints the output for you.

#### Get Top CPU Hoggers

```
!sultan_get_top_cpu_hoggers [-h] hostname
```
This command will run `sudo ps -eo pid,ppid,cmd,%mem,%cpu --sort -%cpu | head` on `<hostname>`, prints the output for you.

#### Get Top Memory Hoggers

```
!sultan_get_top_memory_hoggers [-h] hostname
```
This command will run the `sudo ps -eo pid,ppid,cmd,%mem,%cpu --sort -rss | head` on `<hostname>`, prints the output for you.
