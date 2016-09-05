from dexterhive.groups.models import Groups


def create_group(details):
    """
    Args:
        details: Details of the group to be created (name, about, group_type, visibility)
    """
    Groups(name=details.get('name'), description=details.get('about'), type=details.get('group_type'),
           visibility=details.get('group_visibility')).save()
