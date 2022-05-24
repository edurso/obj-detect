#!/usr/bin/env python3

import os
import argparse

def main():

	parser = argparse.ArgumentParser(description="Clean dataset of images by removing unlabeled images",
									 formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument(
		'-d', '--dir',
		help='Path to the folder where the image dataset is stored. If not specified, the CWD will be used.',
		type=str,
		default=os.getcwd()
	)
	
	args = parser.parse_args()
	dir = args.dir
	
	files = os.listdir(dir)
	removed = 0
	for i in range(len(files)):
		if os.path.splitext(files[i])[0] + '.xml' not in files:
			os.remove(files[i])
			removed += 1

	print('Successfully removed {} unlabeled files'.format(removed))

if __name__ == '__main__':
	main()
