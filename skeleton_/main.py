import os
import datetime
import shutil
import subprocess


def complete_template_file(fn, kvs):
    """Replace fields in the template file with values from the given dictionary"""

    out_tmp = open(fn + '_tmp', 'w')

    for line in open(fn):
        line = line.rstrip()
        for k, v in kvs.iteritems():
            key = '[{}]'.format(k)
            if key in line:
                line = line.replace(key, v)
        out_tmp.write(line + '\n')

    os.remove(fn)
    out_tmp.close()
    os.rename(fn + '_tmp', fn)


def run(ver, project_name):
    """Run process of creating project skeleton"""

    project_name = project_name.replace(' ', '')
    year = str(datetime.datetime.today().year)
    working_dir = os.getcwd()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = script_dir[:script_dir.find('env/lib/')] + '/template'

    # Copy over content of template directory:

    shutil.copytree(template_dir, '{}/{}'.format(working_dir, project_name))

    # Completing template files:

    complete_template_file(
        '{}/{}/LICENCE.md'.format(working_dir, project_name),
        {'Year': year}
    )

    complete_template_file(
        '{}/{}/setup.py'.format(working_dir, project_name),
        {'Project': project_name}
    )

    complete_template_file(
        '{}/{}/project'.format(working_dir, project_name),
        {'Project': project_name}
    )

    complete_template_file(
        '{}/{}/main/cli.py'.format(working_dir, project_name),
        {'Project': project_name, 'project': project_name.lower()}
    )

    complete_template_file(
        '{}/{}/CHANGELOG.md'.format(working_dir, project_name),
        {'Project': project_name}
    )

    complete_template_file(
        '{}/{}/test/smoke/test_installation.sh'.format(working_dir, project_name),
        {'Project': project_name, 'project': project_name.lower(), 'version': ver}
    )

    complete_template_file(
        '{}/{}/install.sh'.format(working_dir, project_name),
        {'Project': project_name, 'version': ver}
    )

    # Renaming files:

    os.rename(
        '{}/{}/project'.format(working_dir, project_name),
        '{}/{}/{}'.format(working_dir, project_name, project_name.lower())
    )

    os.rename(
        '{}/{}/bin/Project.py'.format(working_dir, project_name),
        '{}/{}/bin/{}.py'.format(working_dir, project_name, project_name)
    )

    # Make scripts executable
    subprocess.call(["chmod", "+x", '{}/{}/install.sh'.format(working_dir, project_name)])
    subprocess.call(["chmod", "+x", '{}/{}/{}'.format(working_dir, project_name, project_name.lower())])
    subprocess.call(["chmod", "+x", '{}/{}/test/smoke/test_installation.sh'.format(working_dir, project_name)])

    print '\nSkeleton {}: New project named \"{}\" has been created.\n'.format(ver, project_name)