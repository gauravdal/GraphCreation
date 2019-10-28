import pandas as pd
from networkx import draw, Graph, MultiGraph
from matplotlib.pyplot import show

graph = MultiGraph()
#Reading the excel file
#Setting index_col = 0, which takes first column as index
with open('excel_files','r') as ef:

    for each_excel_file in ef:
        each_excel_file = each_excel_file.strip()

        excel_file_object = pd.read_excel(r'C:\\Network Programmability and Automation\network_diagram\\' + each_excel_file)
        #print(excel_file_object)
        #filter specific columns from excel sheet
        remote_device_id = pd.DataFrame(excel_file_object, columns=['remote device-Id'])
        Local_device_id = pd.DataFrame(excel_file_object, columns=['Local device-Id'])

        #print(list(remote_device_id))
        #print('\n\n')
        #print(remote_device_id)
        #print('\n\n\n')
        #print(Local_device_id)
        #print('test')
        #print()

        local_device_name = Local_device_id.values[0][0]
        remote_device_list = remote_device_id.values

        for i in remote_device_list:
            graph.add_edge(local_device_name, i[0])
        draw(graph, with_labels=True)
        show()



