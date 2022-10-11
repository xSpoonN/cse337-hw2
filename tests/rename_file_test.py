import pytest
import sys
import os
sys.path.insert(1, os.getcwd())
from src.rename_files import rename
import shutil

class TestRenameFiles:
    def test_RenameFiles(self):
        testPath = "./snaptest/"
        if os.path.exists(testPath): shutil.rmtree(testPath)
        os.mkdir(testPath)
        os.mkdir(testPath + "dir/")
        with open(testPath + "snap000.txt", 'w') as f: pass
        with open(testPath + "snap001.txt", 'w') as f: pass
        with open(testPath + "snap002.txt", 'w') as f: pass
        with open(testPath + "snap004.txt", 'w') as f: pass
        with open(testPath + "snap005.txt", 'w') as f: pass
        with open(testPath + "snap008.txt", 'w') as f: pass
        with open(testPath + "snap01.txt", 'w') as f: pass
        with open(testPath + "nap002.txt", 'w') as f: pass
        with open(testPath + "asdf.txt", 'w') as f: pass
        with open(testPath + "dir/snap009.txt", 'w') as f: pass
        rename(testPath); outfiles = os.listdir(testPath); outfiles.sort()
        assert outfiles == ["asdf.txt","dir","nap002.txt","snap000.txt","snap001.txt","snap002.txt","snap003.txt","snap004.txt","snap005.txt","snap01.txt"]
        outfiles = os.listdir(testPath + "dir/"); 
        assert outfiles == ["snap009.txt"]
    def test_RenameFiles_EmptyDir(self):
        testPath = "./snaptest/"
        if os.path.exists(testPath): shutil.rmtree(testPath)
        os.mkdir(testPath)
        rename(testPath); outfiles = os.listdir(testPath);
        assert outfiles == []
    def test_RenameFiles_InvalidDir(self):
        testPath = "./snaptest/"
        if os.path.exists(testPath): shutil.rmtree(testPath)
        os.mkdir(testPath)
        assert rename("garbage") == None
        rename(testPath); outfiles = os.listdir(testPath);
        assert outfiles == []
