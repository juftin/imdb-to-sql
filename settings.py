import os


class DatabaseTypes:
    SQLITE		= 0
    MYSQL 		= 1
    POSTGRES	= 2


DATABASE_TYPE = os.getenv("DATABASE_TYPE", "SQLITE")               # database type, one of DatabaseTypes
DATABASE_DATABASE = os.getenv("DATABASE_DATABASE", "imdb_data")    # database name
DATABASE_ENCODING = os.getenv("DATABASE_ENCODING", "utf-8")        # used to pre-encode the queries to drop any invalid characters

DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")            # database host
DATABASE_USER = os.getenv("DATABASE_USER", "SQLITE")               # database username
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "SQLITE")       # database password
DATABASE_CLEAR_OLD_DB = os.getenv("DATABASE_CLEAR_OLD_DB", False)  # clear old database information if exists


# script configuration
# database options
class Database:
    type = getattr(DatabaseTypes, DATABASE_TYPE)
    database = DATABASE_DATABASE
    encoding = DATABASE_ENCODING
    host = DATABASE_ENCODING
    user = DATABASE_ENCODING
    password = DATABASE_ENCODING
    clear_old_db = True if str(DATABASE_CLEAR_OLD_DB).lower() in ["true", "1", "yes"] else False


# general options
class Options:
	list_dir 			= "./db_dump"	# directory of the imdb list files
	file_extension 		= ".list"		# file extension for the imdb list files
	query_debug 		= False			# show log of all sql queries at construction time
	show_progress 		= True			# show progress (at all)
	progress_count 		= 10000			# show progress every _n_ lines
	commit_count 		= 10000			# commit every _n_ lines, -1 means only on completion
										# database will commit on completion of each file regardless
	show_time 			= True			# show the total time taken to complete
	use_native			= False			# use native parsing operations instead of regex
	use_dict			= True			# use a dictionary to generate and cache db id's in program
	use_cache			= True			# cache the dictionaries to the disk, must be enabled if you 
										# you want to convert only some files and you want to use dict
	schema_dir			= "schemas"		# directory to load the db schemas from
	cache_dir			= "cache"		# directory to load the dictionary caches from if applicable
	proc_all			= True			# overrides the individual process directives

