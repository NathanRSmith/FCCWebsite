import os, shutil

from jinja2 import Environment, FileSystemLoader

import ipdb as pdb

def build():
    env = Environment(loader=FileSystemLoader('templates'))
    PAGES_DIR = os.path.join('templates', 'pages')
    BUILD_DIR = 'build'
    BOWER_DIR = 'bower_components'
    STATIC_DIR = 'static'
    MEDIA_DIR = 'media'
    
    # make build directory
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    root, dirs, files = next(os.walk(BUILD_DIR))
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
    	shutil.rmtree(os.path.join(root, d))

    # render templates
    for root, dirs, files in os.walk(PAGES_DIR):
        sroot = root.split(os.sep)
        for d in dirs:
            os.mkdir(os.path.join(BUILD_DIR, d))
            
        for template in files:
            path_rel_build = sroot[len(PAGES_DIR.split(os.sep)):]
            root_url_list = [os.pardir]*len(path_rel_build)
            root_url = '/'.join(root_url_list)
            
            context = {
                'root': root_url+'/' if len(root_url)>0 else root_url,
                'static': '/'.join(root_url_list+[STATIC_DIR, '']),
                'media': '/'.join(root_url_list+[MEDIA_DIR, '']),
                'bower': '/'.join(root_url_list+[BOWER_DIR, '']),
            }
            
            # pdb.set_trace()
            with open(os.path.join(*([BUILD_DIR]+path_rel_build+[template])), 'w') as f:
                try:
                    f.write(
                        env.get_template(
                            os.path.join(
                                *(sroot[1:]+[template])
                            )
                        ).render(context)
                    )
                except:
                    print 'ERROR: %s'%os.path.join(root, template)
                    raise
    
    # copy static files
    shutil.copytree('static', os.path.join(BUILD_DIR, 'static'))
    
    # copy media files
    shutil.copytree('media', os.path.join(BUILD_DIR, 'media'))
    
    # copy bower resources
    if os.path.exists('bower_components'):
        shutil.copytree('bower_components', os.path.join(BUILD_DIR, 'bower_components'))


                          

if __name__ == '__main__':
    build()