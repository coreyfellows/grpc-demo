import argparse
import os
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('service_name')
    args = parser.parse_args()


    service_name = args.service_name + "_service"
    ServiceName = ''.join(map(str.capitalize, service_name.split("_")))
    
    shutil.copytree('service_template', service_name)
    os.chdir(service_name)
    os.mkdir('grpc_gen')
    for filename in os.listdir('.'):
        if not os.path.isfile(filename):
            continue
        with open(filename, "r") as f:
            content = f.read()
            content = content.replace("%SERVICE_NAME%", service_name)
            content = content.replace("%SERVICE_NAME_CAMEL_CASE%", ServiceName)
        with open(filename, "w") as f:
            f.write(content)
        new_filename = filename.replace("%SERVICE_NAME%", service_name)
        if new_filename == filename:
            continue
        os.rename(filename, new_filename)
    


