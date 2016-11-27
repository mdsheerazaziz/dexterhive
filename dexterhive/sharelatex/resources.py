import requests
from dexterhive.settings import latex_url
from dexterhive.sharelatex.constants import latex_project_url, latex_new_project_url, latex_rename_project_url, \
    latex_restore_project_url


def fetch_project_from_sharelatex(latex_user_id):
    """

    Args:
        latex_user_id: Latex user id of the user

    Returns:
        Project Details

    """
    project = requests.get("{0}/{1}/".format(latex_url, latex_project_url), params={'id': latex_user_id}).json()
    return project


def create_new_project(latex_user_id, project_name):
    project = requests.post('{0}/{1}/'.format(latex_url, latex_new_project_url),
                            data={'projectName': project_name, 'id': latex_user_id}).json()
    return project


def delete_project(latex_user_id, project_id):
    """

    Args:
        latex_user_id: latex user id of the user
        project_id: project id for the project to be deleted

    Returns:
        response ok if the project is deleted
    """
    # TODO DELETE MULTIPLE PROJECTS
    response = requests.delete('{0}/{1}/{2}?id={3}'.format(latex_url, latex_project_url, project_id, latex_user_id))
    return response.content


def rename_project(latex_user_id, project_id, new_project_name):
    """

    Args:
        latex_user_id: latex user id of the user
        project_id: project id for the project to be deleted
        new_project_name: New name of the project

    Returns:
        response ok if the project is renamed
    """
    response = requests.post(
        '{0}/{1}/{2}/{3}'.format(latex_url, latex_project_url, project_id, latex_rename_project_url),
        data={'id': latex_user_id, 'newProjectName': new_project_name})
    return response.content


def restore_project(latex_user_id, project_id):
    """

    Args:
        latex_user_id: latex user id of the user
        project_id: project id for the project to be deleted

    Returns:
        response ok if the project is restored
    """
    response = requests.post(
        '{0}/{1}/{2}/{3}'.format(latex_url, latex_project_url, project_id, latex_restore_project_url),
        data={'id': latex_user_id})
    return response.content


def delete_forever(latex_user_id, project_id):
    """

    Args:
        latex_user_id: latex user id of the user
        project_id: project id for the project to be deleted

    Returns:
        response ok if the project is deleted forever
    """
    response = requests.delete(
        '{0}/{1}/{2}?id={3}&forever={4}'.format(latex_url, latex_project_url, project_id, latex_user_id, True))
    return response.content
