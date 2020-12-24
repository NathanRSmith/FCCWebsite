import os, shutil
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from jinja2 import Environment, FileSystemLoader

ALLOWED_TEMPLATE_EXTENSIONS = [
    'html',
    'CNAME',
    'txt',
]

def check_extension(file):
    for ext in ALLOWED_TEMPLATE_EXTENSIONS:
        if file.endswith(ext):
            return True
    return False

def build():
    env = Environment(loader=FileSystemLoader('templates'))
    PAGES_DIR = os.path.join('templates', 'pages')
    sPAGES_DIR = PAGES_DIR.split(os.sep)
    BUILD_DIR = 'build'
    BOWER_DIR = 'bower_components'
    STATIC_DIR = 'static'
    MEDIA_DIR = 'media'

    # make build directory & remove existing files
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
            os.mkdir(os.path.join(*([BUILD_DIR]+sroot[len(sPAGES_DIR):]+[d])))

        for template in files:
            if check_extension(template):
                path_rel_build = sroot[len(PAGES_DIR.split(os.sep)):]
                root_url_list = [os.pardir]*len(path_rel_build)
                root_url = '/'.join(root_url_list)

                context = {
                    'root': root_url+'/' if len(root_url)>0 else root_url,
                    'static': '/'.join(root_url_list+[STATIC_DIR, '']),
                    'media': '/'.join(root_url_list+[MEDIA_DIR, '']),
                    'bower': '/'.join(root_url_list+[BOWER_DIR, '']),
                }

                with open(os.path.join(*([BUILD_DIR]+path_rel_build+[template])), 'w') as f:
                    try:
                        print('Rendering %s' % os.path.join( *(sroot[1:]+[template]) ))
                        f.write(
                            env.get_template(
                                os.path.join(
                                    *(sroot[1:]+[template])
                                )
                            ).render(context)
                        )
                    except:
                        print('ERROR: %s'%os.path.join(root, template))
                        raise

    # copy static files
    print('Copying static files')
    shutil.copytree('static', os.path.join(BUILD_DIR, 'static'))

    # copy media files
    print('Copying media files')
    shutil.copytree('media', os.path.join(BUILD_DIR, 'media'))

    # copy bower resources
    if os.path.exists('bower_components'):
        print('Copying bower files')
        shutil.copytree('bower_components', os.path.join(BUILD_DIR, 'bower_components'))

    print('Done')


if __name__ == '__main__':
    build()
