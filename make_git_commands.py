from git import Repo


tempfile = 'textfile.txt'
print 'Writing to %s' % tempfile
with open(tempfile, 'wt') as fp:
    fp.write("changed by python")

print 'get git objects'
repo = Repo()
index = repo.index
origin = repo.remotes.origin

print 'Add file to be staged for commit'
index.add([tempfile])

print 'Commit'
index.commit("Commit through python")

print 'Push'
origin.push()

print 'Done!'
