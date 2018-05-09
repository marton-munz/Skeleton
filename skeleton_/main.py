import os
import datetime
import shutil


def complete_template_file(fn, kvs):
    """..."""

    out_tmp = open(fn + '_tmp', 'w')

    for line in open(fn):
        line = line.strip()
        for k, v in kvs.iteritems():
            key = '[{}]'.format(k)
            if key in line:
                line = line.replace(key, v)
        out_tmp.write(line + '\n')

    os.remove(fn)
    out_tmp.close()
    os.rename(fn + '_tmp', fn)


def run(ver, project_name):
    """..."""

    project_name = project_name.replace(' ', '')
    year = str(datetime.datetime.today().year)
    working_dir = os.getcwd()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = script_dir[:script_dir.find('env/lib/')] + '/template'

    # Copy over content of template directory:

    shutil.copytree(template_dir, '{}/{}'.format(working_dir, project_name))

    # Completing template files:

    complete_template_file(
        '{}/{}/LICENCE'.format(working_dir, project_name),
        {'Year': year}
    )

    complete_template_file(
        '{}/{}/setup.py'.format(working_dir, project_name),
        {'Project': project_name, 'project': project_name.lower()}
    )

    complete_template_file(
        '{}/{}/bin/project'.format(working_dir, project_name),
        {'Project': project_name}
    )

    complete_template_file(
        '{}/{}/bin/Project.py'.format(working_dir, project_name),
        {'Project': project_name, 'project': project_name.lower()}
    )

    # Renaming files:

    os.rename(
        '{}/{}/bin/project'.format(working_dir, project_name),
        '{}/{}/bin/{}'.format(working_dir, project_name, project_name.lower())
    )

    os.rename(
        '{}/{}/bin/Project.py'.format(working_dir, project_name),
        '{}/{}/bin/{}.py'.format(working_dir, project_name, project_name)
    )

    # Renaming directory:

    os.rename(
        '{}/{}/project'.format(working_dir, project_name),
        '{}/{}/{}'.format(working_dir, project_name, project_name.lower())
    )

    print 'Skeleton {}: New project named \"{}\" has been created.'.format(ver, project_name)