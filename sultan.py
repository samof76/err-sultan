from errbot import BotPlugin, botcmd, arg_botcmd
from sultan.api import Sultan
from itertools import chain

username = 'root'

class SultanBot(BotPlugin):

  @arg_botcmd('hostname', type=str)
  def sultan_get_uptime(self, msg, hostname=None):
    """
    Get the uptime from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      uptime = s.sudo('uptime')
    
    rtn = uptime.run()
    
    return "``` {}\n```".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_tail_dmesg(self, msg, hostname=None):
    """
    Get the tail dmesg from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      tail_dmesg = s.sudo('dmesg | tail')
    
    rtn = tail_dmesg.run()
    return "``` {}\n```".format("\n".join(rtn.stdout))



  @arg_botcmd('hostname', type=str)
  def sultan_get_mount_points(self, msg, hostname=None):
    """
    Get the mount points from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      mnt_points = s.sudo('mount')
    
    rtn = mnt_points.run()
    
    return "``` {}\n".format("\n".join(rtn.stdout))


  @arg_botcmd('hostname', type=str)
  def sultan_get_disk_usage(self, msg, hostname=None):
    """
    Get the disk usage from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      disk_usage = s.sudo('df -h')
    
    rtn = disk_usage.run()
    
    return "``` {}\n```".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_memory_usage(self, msg, hostname=None):
    """
    Get the memory usage from the host
    """
    username = self.config['username']
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      mem_free = s.sudo('free -m')
    
    rtn = mem_free.run()
    
    return "``` {}\n```".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_top_memory_hoggers(self, msg, hostname=None):
    """
    Get the top memory hoggers from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      top_mem_hoggers = s.sudo('ps -eo pid,ppid,cmd,%mem,%cpu --sort -rss | head')
    
    rtn = top_mem_hoggers.run()
    
    return " ``` {}\n``` ".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_top_cpu_hoggers(self, msg, hostname=None):
    """
    Get the top CPU hoggers from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname,user=username) as s:
      top_cpu_hoggers = s.sudo('ps -eo pid,ppid,cmd,%mem,%cpu --sort -%cpu | head')
    
    rtn = top_cpu_hoggers.run()
    
    return "``` {}\n```".format("\n".join(rtn.stdout))

