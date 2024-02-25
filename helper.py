from sklearn.model_selection import train_test_split
import glob
import os



def get_list_of_files(source_path:str) -> list[str]:
	train_files= glob.glob(source_path+'train*.png')
	train_files = [(int(i[len(source_path)+5:-4]), i) for i in glob.glob(source_path+'train*.png')]
	train_files.sort()
	return [i[1] for i in train_files]

def make_folder_if_not_exists(folder:str):
	if not os.path.exists(folder):
		os.makedirs(folder)

def y_int_to_str(y:int) -> str:
	match y:
		case 0: return "No Whale"
		case 1: return "Whale Present"
		case _: raise ValueError("Unrecognized label")

def split_data(x, y):
	return train_test_split( #x_train, x_test, y_train, y_test = ...
		x,
		y,
		test_size=0.33,
		random_state=4,
		stratify=y
	)
