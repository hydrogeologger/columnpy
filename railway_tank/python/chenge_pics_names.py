import os
current_path=os.getcwd()
output_figure_path = current_path+'/railway_tank/output_figure/'
file_list = os.listdir(output_figure_path)
os.chdir(output_figure_path)
for idx,old_name in enumerate(file_list):
    #print(old_name)
    new_name = f'{idx}.jpg'
    os.rename(old_name, new_name)
    pass