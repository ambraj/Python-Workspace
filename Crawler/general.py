import os

# this method will create new directory whenever you will start crawling new website
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating new project '+directory)
		os.makedirs(directory)

# create data files
def create_data_files(project_name, base_url):
	queue = project_name+'/queue.txt'
	crawled = project_name + '/crawled.txt'

	if not os.path.isfile(queue):
		write_file(queue, base_url)

	if not os.path.isfile(crawled):
		write_file(crawled, '')

# create new file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

# add data onto an existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data+"\n")

# Delete the contents of file
def delete_file_content(path):
	with open(path, 'w'):
		pass

