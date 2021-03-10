import os,zipfile,json,datetime
from common.log.logger import gather_logger


def get_root_path():
    root_path = os.path.dirname(os.path.abspath(__file__))
    return root_path


# put_in = open(becopyed_file,"w+",encoding= 'utf-8')
# put_in.write(str(data.encode('utf-8').decode('utf-8')))
# 解决中文乱码的2个方式
# import codecs
# f = codecs.open(becopyed_file,"w+",encoding= 'utf-8')
# f.write(content)


def write2file(contents, output_file=None):
    if not contents or len(contents) == 0:
        return []
    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write("\n".join(contents))


# 按行读取文件
def load_address_from_file(self, path: str):
    path_map = {}
    with open(path) as fi:
        for each in fi:
            address, path = each.split()
            path_map[address] = path
    return path_map


def create_write_file(dir,currency,ts,file_name,data):
    try:
        dirs = dir + '/' + currency + '_' + ts
        gather_logger.info("ready to write {}/{}".format(dirs, file_name))
        if os.path.isdir(dirs):
            pass
        else:
            os.makedirs(dirs)

        file = "{}/{}".format(dirs, file_name)
        #gather_logger.info("file={}".format(file))
        #gather_logger.info("data={}".format(data))
        fd = open(file, "w")
        fd.write(json.dumps(data))

    except Exception as e:
        gather_logger.error(str(e))
        raise e

def create_write_btc_series_file(dirs_file_name,data):
    dirs = os.path.dirname(dirs_file_name)
    if os.path.isdir(dirs):
        pass
    else:
        os.makedirs(dirs)
    with open(dirs_file_name, "w+") as fd:
        fd.write("\n".join(data))

#打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):
  zipf = zipfile.ZipFile(output_filename, 'w')
  pre_len = len(os.path.dirname(source_dir))
  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      pathfile = os.path.join(parent, filename)
      arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
      zipf.write(pathfile, arcname)
  zipf.close()

def make_zip_with_filename(output_filename, *args):
    z = zipfile.ZipFile(output_filename, 'w')
    for file in args:
        z.write(file)
    z.close()

def remove_file(file_name):

    if os.path.exists(file_name) and os.path.isfile(file_name):
        os.remove(file_name)
    else:
        err_data = "[{}] not file!".format(file_name)
        raise Exception(err_data)