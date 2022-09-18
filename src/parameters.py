# parameters.py - Parameter resolving
import os
import sys
import json

DEFAULT_IMPORT_PARAMETER = "parameter.json"

# _dictionary_overwrite - Overwriting corresponding entries in old with entries in new

def _dictionary_overwrite(old, new):
	if not isinstance(new, dict):
		return new
	if not isinstance(old, dict):
		return new
	for key in new:
		old[key] = _dictionary_overwrite(old.get(key), new[key])
	return old

# dictionary_overwrite - Merge all of dicts
def dictionary_overwrite(*dicts):
	result = [{}]
	for i in dicts:
		result = _dictionary_overwrite(result, i)
	return result

# resolve_parameters - Parse special string within json data structure
def resolve_parameters(params):
	if isinstance(params, dict):
		return {key : resolve_parameters(value) for key, value in params.items()}
	elif isinstance(params, list):
		return [resolve_parameters(i) for i in params]
	elif isinstance(params, str):
		if params.startswith('env:'):
			return os.environ.get(params[4:])
		if params.startswith('escape:'):
			return params[7:]
	return params

# _load_json_file - Load json data structure from filename
def _load_json_file(filename):
	with open(filename) as f:
		return json.load(f)

# Load all sources and parameters file into empty json data structure
def load_parameters():
	default = _load_json_file(DEFAULT_IMPORT_PARAMETER)
	dictionary = resolve_parameters(dictionary_overwrite(default))
	return Parameters(dictionary)

# Parameters class - Abstract class for dictionary path searching
class Parameters:
	def __init__(self,dictionary):
		self.dictionary = dictionary
	
	# Search as a path
	# Path format as python module
	def get(self, path:str):
		pieces = path.split('.')
		result = self.dictionary
		for i in pieces:
			result = result.get(i)
			if result is None:
				break
		return result
	
	# Search as a path but provide a default value
	# In case it is not detected
	def get_def(self, path:str, default):
		pieces = path.split('.')
		result = self.dictionary
		for i in pieces:
			result = result.get(i)
			if result is None:
				return default
		return result
	