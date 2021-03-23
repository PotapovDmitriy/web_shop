import os
from datetime import datetime


def save_image(file, name):
    f_name_arr = file.filename.split('.')
    str_date = str(datetime.now().microsecond)
    # print(os.listdir('./'))
    file.filename = "name_" + str(name) + "_" + str_date + '.' + f_name_arr[len(f_name_arr) - 1]
    sfname = './admin_web/images/' + str(file.filename)
    file.save(sfname)
    return sfname


def delete_image(path):
    if os.path.exists(path):
        os.remove(path)
