import requests
import multiprocessing
import os.path
import time
from concurrent.futures import ProcessPoolExecutor
def downloadFile(url, id):
    print(f'Started Downloading {id}')

    response = requests.get(url)
    if not os.path.exists('Picsum/'):
        os.mkdir('Picsum')
    open(f'Picsum/{id}.jpg', 'wb').write(response.content)

    print(f'Finished Downloading {id}')

url = 'https://picsum.photos/4000/5000'
url_2 = f'https://picsum.photos/id/{id}/5000/3333'

def delete_all_files_in_folder(folder_path):
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            delete_all_files_in_folder(item_path)
    # print('All files deleted')

def main():
    pros = []
    for i in range(60):
        p = multiprocessing.Process(target=downloadFile, args=[url,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

if  __name__ == '__main__':

    time1 = time.perf_counter()
    # main()
    delete_all_files_in_folder('Picsum')

    # l1 = [url for i in range(15)]
    # l2 = [i for i in range(15)]
    # with ProcessPoolExecutor() as executor:
    #     results = executor.map(downloadFile, l1, l2)
    # for r in results:
    #     print(r)







    time2 = time.perf_counter()
    print(time2 - time1)