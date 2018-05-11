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

    # Check if project directory already exists
    if os.path.isdir('{}/{}'.format(working_dir, project_name)):
        print '\nSkeleton {}:'.format(ver)
        print  'Error: Unable to create project as directory already exists.\n'
        quit()

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

    complete_template_file(
        '{}/{}/test/unit/README.md'.format(working_dir, project_name),
        {'Project': project_name}
    )

    complete_template_file(
        '{}/{}/test/smoke/README.md'.format(working_dir, project_name),
        {'Project': project_name}
    )

    complete_template_file(
        '{}/{}/test/regression/README.md'.format(working_dir, project_name),
        {'Project': project_name}
    )


    # Renaming files:

    os.rename(
        '{}/{}/project'.format(working_dir, project_name),
        '{}/{}/{}'.format(working_dir, project_name, project_name.lower())
    )

    os.rename(
        '{}/{}/gitattributes'.format(working_dir, project_name),
        '{}/{}/.gitattributes'.format(working_dir, project_name)
    )

    os.rename(
        '{}/{}/bin/Project.py'.format(working_dir, project_name),
        '{}/{}/bin/{}.py'.format(working_dir, project_name, project_name)
    )

    # Make scripts executable
    subprocess.call(["chmod", "+x", '{}/{}/install.sh'.format(working_dir, project_name)])
    subprocess.call(["chmod", "+x", '{}/{}/{}'.format(working_dir, project_name, project_name.lower())])
    subprocess.call(["chmod", "+x", '{}/{}/test/smoke/test_installation.sh'.format(working_dir, project_name)])

    print '\nSkeleton {}:'.format(ver)
    print 'New project named \"{}\" has been created.\n'.format(project_name)

