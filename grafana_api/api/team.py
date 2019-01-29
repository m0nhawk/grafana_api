from .base import Base


class Teams(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api

    def search_teams(self, query=None, page=None, perpage=None):
        """

        :return:
        """
        list_of_teams = []
        teams_on_page = None
        search_teams_path = '/teams/search'
        params = []

        if query:
            params.append('query=%s' % query)

        if page:
            iterate = False
            params.append('page=%s' % page)
        else:
            iterate = True
            params.append('page=%s')
            page = 1

        if perpage:
            params.append('perpage=%s' % perpage)

        search_teams_path += '?'
        search_teams_path += '&'.join(params)

        if iterate:
            while True:
                teams_on_page = self.api.GET(search_teams_path % page)
                list_of_teams += teams_on_page["teams"]
                if len(list_of_teams) == teams_on_page["totalCount"]:
                    break
                page += 1
        else:
            teams_on_page = self.api.GET(search_teams_path)
            list_of_teams += teams_on_page["teams"]

        return list_of_teams

    def get_team(self, team_id):
        """

        :param team_id:
        :return:
        """
        get_team_path = '/teams/%s' % team_id
        r = self.api.GET(get_team_path)
        return r

    def add_team(self, team):
        """

        :param team:
        :return:
        """
        add_team_path = '/teams'
        r = self.api.POST(add_team_path, json=team)
        return r

    def update_team(self, team_id, team):
        """

        :param team_id:
        :param team:
        :return:
        """
        update_team_path = '/teams/%s' % team_id
        r = self.api.PUT(update_team_path, json=team)
        return r

    def delete_team(self, team_id):
        """

        :param team_id:
        :return:
        """
        delete_team_path = '/teams/%s' % team_id
        r = self.api.DELETE(delete_team_path)
        return True

