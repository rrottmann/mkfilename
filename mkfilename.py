# This script creates filenames according to my personal taste of naming markdown files for documentation
import os
import re
import click
import logging
import datetime
import pyperclip

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime('%y%m%d')

def get_clipboard():
    return pyperclip.paste()

def set_clipboard(s):
    pyperclip.copy(s)

@click.command()
@click.option('--string', 's', default=None, help='Convert given string to filename')
@click.option('--clipboard', default=False, is_flag=True, help='Convert string from clipboard to filename')
@click.option('--stdout', default=False, is_flag=True, help='Print filename to stdout instead of saving it to clipboard')
def mkfilename(s, clipboard, stdout):
    if s and clipboard:
        logging.error('Ambiguous choice. Exiting.')
        return None
    if not s and clipboard:
        logging.debug('Working on clipboard contents.')
        s = get_clipboard()
    if not s and not clipboard:
        logging.debug('No input selected. Exiting.')
        return None
    if not s:
        logging.error('Cannot convert an empty string. Exiting.')
        return None
    logging.debug('Got string: ' + s)
    _, file_extension = os.path.splitext(s)
    if file_extension and not file_extension == '.':
        logging.debug(f'Got file extension: {file_extension}.')
        s = _
    logging.debug('Stripping spaces.')
    s = s.strip()
    logging.debug('Removing quotes from string.')
    s = s.strip('\"').strip('\'')
    logging.debug('Converting string to lowercase.')
    s = s.lower()
    logging.debug('Replacing German umlauts.')
    s = s.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'sz')
    logging.debug('Replacing spaces and special characters with a dash "-".')
    s = re.sub('[^0-9a-zA-Z]+', '-', s)
    logging.debug('Checking whether there already is a timestamp.')
    regex = re.compile('\d{6}-')
    if not regex.search(s):
        logging.debug('...there is none.')
        logging.debug('Prepending a timestamp')
        s = get_timestamp() + '-' + s
    else:
        logging.debug('...it is.')
    logging.debug('Appending file extension ".md".')
    if s.endswith('-md'):
        s = s[:-3]
    if s[-1] == '-':
        logging.debug('Last character before file extension should not be a "-".')
        s = s[:-1]
    logging.debug('Replacing multiple dashes to a single dash.')
    s = re.sub('\-+', '-', s)
    s = '-'.join(s.split('-'))
    if file_extension and not file_extension == '.':
        s = s + file_extension
    else:
        if not s.endswith('.md'):
            s = s + '.md'
    logging.debug('Resulting filename: ' + s)
    if stdout:
        logging.debug('Printing only to stdout as requested.')
        print(s)
    else:
        logging.debug('Pasting resulting string to clipboard.')
        set_clipboard(s)
    return s

if __name__ == '__main__':
    mkfilename()
