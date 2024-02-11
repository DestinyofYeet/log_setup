I am thinking of this as a sort of library.

`git submodule add https://github.com/DestinyofYeet/log_setup`

To update: `git submodule update --remote` 

To use:


```
import logging

from log_setup import main as log_setup  # pick a alias of your choosing

def main():  # main entrypoint of your program
  log_setup.setup_logging()  # if you have the folder in another subfolder, you can specify parent_multiplier as a depth counter
  logger = logging.get_logger(__name__)
  logger.info("Hello")


if __name__ == "__main__":
  # just a personal touch to log the exception that crashed your program
  try:
    main()
  except Exception as e:
    log_setup.log_traceback()
    raise e
```
