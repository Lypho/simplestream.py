#! /usr/bin/env python
import subprocess
import urllib.request
import json
from colorama import Fore, Back, Style, init

init()
print(Style.BRIGHT)

while (1):
   print('\nA) ' + Style.NORMAL + 'EXIT' + Style.BRIGHT)
   print('B) ' + Style.NORMAL + 'REFRESH' + Style.BRIGHT)
   print('C) ' + Style.NORMAL + 'SETTINGS' + Style.BRIGHT)
   print('D) ' + Style.NORMAL + 'SEARCH BY STREAMER\'S NAME' + Style.BRIGHT)

   req = urllib.request.Request('https://api.twitch.tv/kraken/streams/followed?limit=100', None, {'Accept':'application/vnd.twitch.tv.v5+json', 'Authorization':'OAuth $YOUR_TOKEN'})
   res =  urllib.request.urlopen(req)
   res_str = (res.read().decode('UTF-8'))
   res_dict = json.loads(res_str)
   live_total = res_dict['_total']
   streamers = {}

   for i in range(live_total):
      name = res_dict['streams'][i]['channel']['display_name']
      viewers = str(res_dict['streams'][i]['viewers'])
      game = res_dict['streams'][i]['game']
      if (game is None):
         game = 'None'
      #status = str(res_dict['streams'][i]['channel']['status'].encode('ascii', errors='ignore'))
      #status = status.strip("b").strip("'").strip('"')
      status = ''
      streamers[i]={'name':name, 'viewers':viewers, 'game':game, 'status':status}

   for k, v in streamers.items():
      print(Fore.RESET + str(int(k)+1) + ') ' + Fore.GREEN + v['name'] + Fore.YELLOW + '(' + v['viewers'] + ')' + Fore.CYAN + ' ' + v['game'] + ' ' + Fore.MAGENTA + v['status']+ Fore.RESET)
   print('\nselect an option:')
   ans = input('--> ')

   if (ans == 'a' or ans == 'A'):
      raise SystemExit(0)
   elif (ans == 'b' or ans == 'B'):
      continue
   elif (ans == 'c' or ans == 'C'):
      while(1):
         print('\nA) ' + Style.NORMAL + 'BACK' + Style.BRIGHT)
         print('B) ' + Style.NORMAL + 'SET USERNAME' + Style.BRIGHT)
         print('C) ' + Style.NORMAL + 'SET OAUTH TOKEN' + Style.BRIGHT)
         print('\nselect an option:')
         ans = input('--> ')

         if(ans == 'a' or ans == 'A'):
            break
         elif(ans == 'b' or ans == 'B'):
            print('\nenter your username:')
            ans = input('--> ')
            continue
         elif(ans == 'c' or ans == 'C'):
            print('\nenter your OAuth token:')
            ans = input('--> ')
            continue
         else:
            print(Fore.RED + 'error: invalid input' + Fore.RESET)
            continue
      continue
   elif (ans == 'd' or ans == 'D'):
      print('Enter Streamer Name:')
      chosen_stream = 'twitch.tv/' + input('--> ')
   else:
      try:
         chosen_stream = "twitch.tv/" + streamers[int(ans)-1]['name']
      except:
         print(Fore.RED + 'error: invalid input' + Fore.RESET)
         continue
      
   subprocess.Popen(
      ["streamlink", "--config", "/Users/ben/.config/livestreamer/twitch", "-Q", chosen_stream],
      bufsize=-1,
      executable=None,
      stdin=None,
      stdout=None,
      stderr=None,
      preexec_fn=None,
      close_fds=True,
      shell=False,
      cwd=None,
      env=None,
      universal_newlines=False,
      startupinfo=None,
      restore_signals=True,
      start_new_session=False,
      pass_fds=()
   )
