# http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html
import os
from subprocess import check_call

c = get_config()

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['ipython', 'nbconvert', '--to', 'script', fname], cwd=d)
    #check_call(['ipython', 'nbconvert', '--to', 'html', fname], cwd=d)

c.FileContentsManager.post_save_hook = post_save



c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.FileNotebookManager.save_script = True
