#!/usr/bin/env python3
import shelve
blogshelf = shelve.open('blogfile.txt', writeback=True)
print("The keys are:")
print(list(blogshelf.keys()))
for k in blogshelf:
    print(k, "=>", blogshelf[k])

blogshelf.close()

