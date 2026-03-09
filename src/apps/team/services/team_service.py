from apps.authentication.models import UserModel

from apps.team.models import TeamModel


class TeamService:
    @staticmethod
    def create_team(validated_data: dict, creator: UserModel) -> TeamModel:
        if not validated_data.get('manager'):
            validated_data['manager'] = creator

        team = TeamModel.objects.create(**validated_data)

        return team
