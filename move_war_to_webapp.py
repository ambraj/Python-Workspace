import shutil,os
import psutil
import signal

file_name = ""

for file in os.listdir("html/target/"):
    if file.endswith(".war"):
        file_name = file
        

print 'moving "'+file_name+'" to webapp.....'
shutil.copy2('html/target/' + file_name, 'C:/Program Files (x86)/jetty-6.1.3/webapps')

for prefix in file_name.split('-', 1):
    break

os.chdir('C:/Program Files (x86)/jetty-6.1.3/webapps')

for file in os.listdir("C:/Program Files (x86)/jetty-6.1.3/webapps"):
    if file == prefix + '.war':
        os.remove(prefix + '.war')
        print 'deleted ' + prefix + '.war'

os.rename(file_name, prefix + '.war')

print 'Successfully moved to webapps...... now restart your webserver !!'
