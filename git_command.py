import sys
import os

def fetch_command():
  return 'git fetch'

def autoedit_command():
  return 'export GIT_MERGE_AUTOEDIT=no'

def pull_command():
  return 'git pull -q'

def checkout_command(param):
  if not param:
    return

  return 'git checkout %s' % param

def add_command(param):
  if not param:
    return

  return 'git add %s' % param

def commit_command(param):
  if not param:
    return

  return 'git commit -m "%s"' % param

def push_command():
  return 'git push'

def diff_command(param=None):
  if param:
    return 'git diff %s' % param
  return 'git diff'

def status_command(param=None):
  if param:
    return 'git status %s' % param
  return 'git status'

def init_command(param=None):
  if not param:
    return

  commands = ["touch README.md"]

  commands.append('git init')
  commands.append(add_command('README.md'))
  commands.append(commit_command('first commit'))
  commands.append('git branch -M main')
  commands.append('git remote add origin %s' % param)
  commands.append('git push -u origin main')

  return mix_command(commands)


def mix_command(commands):
  return ' && '.join(commands)

def run_command(command):
  os.system(command)

def get_option_params(params):
  result = list()

  for param in params:
    if param.startswith('-'):
      break
    result.append(param)

  return result

def show_help_message():
  message = """
  simple git command tool, made by bsangs

  [how to use]
    usage: g [options] [param]
    example: g -c index.ts"
      - running command: git checkout index.ts

  [how to multiple arguments]
    usage: g [options] [params...]
    example: g -amu index.ts "feat: Update index.ts"
      - running command: git add index.ts && git commit -m "feat: Update index.ts" && git push

  [help command]
    -h \t\t\t show git command help

  [initalize category arguments]
    -i <remote url> \t init new repository

  [pull category arguments]
    -f \t\t\t git fetch
    -c <branch | path> \t git checkout <branch | path>
    -p \t\t\t git fetch && git pull

  [commit category arguments]
    -a <path> \t\t git add <path>
    -m <commit title> \t git commit -m <commit title>
    -u \t\t\t git push

  [show category arguments]
    -d \t\t\t git diff <path | none>
    -s \t\t\t git status <path | none>
  """
  print(message[1:])

def process_options(options, option_params):
  commands = list()
  filtered_command = list()
  use_options = list()

  # pop?????? params ???????????? ????????? reverse
  params = option_params.copy()
  params.reverse()

  # ????????? ?????????
  commands.append(autoedit_command())

  # show category
  if len(options) == 1:
    option = options[0]

    if len(params) == 0:
      params.append(None)

    if option == 'd':
        commands.append(diff_command(params.pop()))
    if option == 's':
      commands.append(status_command(params.pop()))
    if option == 'i':
      commands.append(init_command(params.pop()))

  for option in options:
    # ?????? ????????? ???????????? ????????????
    if option in use_options:
      continue

    if option == 'f' or option == 'p':
      commands.append(fetch_command())
    elif option == 'c':
      commands.append(checkout_command(params.pop()))
    elif option == 'p':
      commands.append(pull_command())
    elif option == 'a':
      commands.append(add_command(params.pop()))
    elif option == 'm':
      commands.append(commit_command(params.pop()))
    elif option == 'u':
      commands.append(push_command())
    else:
      continue

    # ???????????? ????????? ???????????? ????????? ?????? ???????????? ??????
    if commands[len(commands) - 1] in commands[:len(commands) - 1]:
      commands.pop()

    use_options.append(option)

  for command in commands:
    if command:
      filtered_command.append(command)
  
  result_commands = mix_command(filtered_command)
  
  if len(result_commands) > 0 and len(filtered_command) > 1:
    run_command(result_commands)
  else:
    show_help_message()
      

if __name__ == '__main__':
  has_processed = False
  for i in range(len(sys.argv)):
    if sys.argv[i].startswith('-'):
      options = sys.argv[i].replace('-', '')
      option_params = get_option_params(sys.argv[i+1:])

      process_options(options, option_params)
      has_processed = True
  
  if not has_processed:
    show_help_message()
