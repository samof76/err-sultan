from errbot import BotPlugin, botcmd, arg_botcmd
from sultan.api import Sultan


class SultanBot(BotPlugin):

  @arg_botcmd('hostname', type=str)
  def sultan_get_uptime(self, msg, hostname=None):
    """
    Get the uptime from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('uptime').run()
    
    return "/code {}".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_tail_dmesg(self, msg, hostname=None):
    """
    Get the tail dmesg from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('dmesg | tail').run()
    
    return "/code {}".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_monit_status(self, msg, hostname=None):
    """
    Get the monit status from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('monit status').run()
    
    return "/code {}".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_passenger_status(self, msg, hostname=None):
    """
    Get the passenger status from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('passenger-status').run()
    
    return "/code {}".format("\n".join(rtn.stdout))


  @arg_botcmd('hostname', type=str)
  def sultan_get_mount_points(self, msg, hostname=None):
    """
    Get the mount points from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('mount').run()
    
    return "/code {}".format("\n".join(rtn.stdout))


  @arg_botcmd('hostname', type=str)
  def sultan_get_disk_usage(self, msg, hostname=None):
    """
    Get the disk usage from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('df -h').run()
    
    return "/code {}".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_memory_usage(self, msg, hostname=None):
    """
    Get the memory usage from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('free -m').run()
    
    return "/code {}".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_top_memory_hoggers(self, msg, hostname=None):
    """
    Get the top memory hoggers from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('ps -eo pid,ppid,cmd,%mem,%cpu --sort -rss | head').run()
    
    return "/code {}".format("\n".join(rtn.stdout))

  @arg_botcmd('hostname', type=str)
  def sultan_get_top_cpu_hoggers(self, msg, hostname=None):
    """
    Get the top CPU hoggers from the host
    """
    if not hostname:
      return 'Sultan will only respond, if you provide a hostname'
    
    with Sultan.load(hostname=hostname) as s:
      rtn = s.sudo('ps -eo pid,ppid,cmd,%mem,%cpu --sort -%cpu | head').run()
    
    return "/code {}".format("\n".join(rtn.stdout))
