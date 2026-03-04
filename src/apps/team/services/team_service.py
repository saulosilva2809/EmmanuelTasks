from apps.authentication.models import UserModel

from apps.team.models import TeamModel


class TeamService:
    @staticmethod
    def create_team(validated_data: dict, creator: UserModel) -> TeamModel:
        if not validated_data.get('manager'):
            validated_data['manager'] = creator

        # remove membros temporariamente antes de criar o team
        members_data = validated_data.pop('members', [])
        team = TeamModel.objects.create(**validated_data)
        
        if members_data:
            team.members.set(members_data)
            
        return team
